from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
import locale
import json
import time


class Bot(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")
        self.username = ""
        self.password = ""
        self.subjects = set()
        self.days_of_week = [
            "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
            "sexta-feira", "sábado"
        ]
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def get_text_stars_json(self, subject):
        with open('./user_config.json') as json_file:
            obj = json.load(json_file)
            return obj['subjects'][subject]['text']

    def load_subjects(self):
        week_day = date.today().weekday()
        number_of_subjects = 1
        count = 0
        for day in range(0, week_day):
            self.driver.find_element_by_link_text(
                self.days_of_week[day]).click()
            test = self.driver.find_element_by_id("tab-semana-" + str(day + 1))
            count += len(
                test.find_elements_by_xpath(".//ul[starts-with(@id,'aula-')]"))
            while number_of_subjects <= count:
                subject = self.driver.find_element_by_id(
                    "aula-" + str(number_of_subjects)).text.split("-")[0]
                self.subjects.update([subject])
                text = self.get_text_stars_json(subject)
                try:
                    self.driver.find_element_by_id(
                        'consideracao-' +
                        str(number_of_subjects)).send_keys(text)
                    self.driver.find_element_by_id(
                        "cadastrar-" + str(number_of_subjects)).click()
                    time.sleep(3)
                except:
                    print('Element not found')
                finally:
                    number_of_subjects += 1

    def load_config(self):
        try:
            with open('user_config.json') as json_file:
                data = json.load(json_file)
                self.username = data["user"]["username"]
                self.password = data["user"]["password"]
        except:
            print("Error reading json file")

    def login(self):
        self.driver.get(
            "https://interage.fei.org.br/secureserver/portal/graduacao/sala-dos-professores/aulas/presenca"
        )
        self.driver.find_element_by_id("Usuario").send_keys(self.username)
        self.driver.find_element_by_id("Senha").send_keys(self.password)
        self.driver.find_element_by_id("btn-login").click()

    def send_feedback(self):
        self.driver.close()
