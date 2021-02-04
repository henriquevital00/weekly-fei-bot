from selenium import webdriver
from datetime import date
import locale
import json

class Bot(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
        self.username = ""
        self.password = ""
        self.subjects = []

    def load_subjects(self):
        self.login()
        self.driver.find_element_by_link_text("quarta-feira").click()
        for i in range(0, 9):
            self.subjects.append(self.driver.find_element_by_id("aula-" + i).text.split("-")[0])

    def load_config(self):
        try:
            with open('user_config.json') as json_file:
                data = json.load(json_file)
                self.username = data["user"]["username"]
                self.password = data["user"]["password"]
        except:
            print("Error reading json file")

    def login(self):
        self.driver.get("https://interage.fei.org.br/secureserver/portal/graduacao/secretaria/temporarios-e-sazonais/avaliacoes-semanais")
        self.driver.find_element_by_id("Usuario").send_keys(self.username)
        self.driver.find_element_by_id("Senha").send_keys(self.password)
        self.driver.find_element_by_id("btn-login").click()

    def send_feedback(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        week_day = date.today().strftime('%A')
        self.driver.close()
