from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import date
import locale
import json
import glob
import time


class Bot(object):
    def __init__(self):
        self.options = Options()
        self.options.binary_location = '/opt/headless-chromium'
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome('/opt/chromedriver', options=self.options)
        self.username = 'username'
        self.password = 'password'
        self.subjects = set()
        self.days_of_week = [
            "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
            "sexta-feira", "sábado"
        ]
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def load_subjects(self):
        week_day = date.today().weekday()
        number_of_subjects = 1
        count = 0
        if week_day == 6:
            return
        for day in range(0, week_day + 1):
            self.driver.find_element_by_xpath(
                '//a[@href="#tab-semana-{}"]'.format(day + 1)).click()
            test = self.driver.find_element_by_id("tab-semana-" + str(day + 1))
            count += len(
                test.find_elements_by_xpath(".//ul[starts-with(@id,'aula-')]"))
            while number_of_subjects <= count:
                subject = self.driver.find_element_by_id(
                    "aula-" + str(number_of_subjects)).text.split("-")[0]
                self.subjects.update([subject])
                try:
                    self.driver.find_element_by_id(
                        "cadastrar-" + str(number_of_subjects)).click()
                except:
                    pass
                finally:
                    number_of_subjects += 1
        self.driver.close()

    def login(self):
        self.driver.get(
            "https://interage.fei.org.br/secureserver/portal/graduacao/sala-dos-professores/aulas/presenca"
        )
        self.driver.find_element_by_id("Usuario").send_keys(self.username)
        self.driver.find_element_by_id("Senha").send_keys(self.password)
        self.driver.find_element_by_id("btn-login").click()

def lambda_handler(event, context):
    bot = Bot()
    bot.login()
    bot.load_subjects()