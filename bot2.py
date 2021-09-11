from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
import locale
import json
import glob
import time


class Bot(object):
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        #chrome_options.add_argument('--window-size=1280x1696')
        #chrome_options.add_argument('--user-data-dir=/tmp/user-data')
        #chrome_options.add_argument('--hide-scrollbars')
        #chrome_options.add_argument('--enable-logging')
        #chrome_options.add_argument('--log-level=0')
        #chrome_options.add_argument('--v=99')
        #chrome_options.add_argument('--single-process')
        #chrome_options.add_argument('--data-path=/tmp/data-path')
        #chrome_options.add_argument('--ignore-certificate-errors')
        #chrome_options.add_argument('--homedir=/tmp')
        #chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
        #chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        self.driver = webdriver.Chrome(executable_path=str(
            glob.glob("./chromedriver*")[0]),
                                       chrome_options=chrome_options)
        self.username = 'unifhcarvalho'
        self.password = 'hc65013'
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
