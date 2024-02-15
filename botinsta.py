from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username 
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\julio\OneDrive\Área de Trabalho\Projetos PY\gecko/geckdriver.exe')


#//name="username"
# name="password"
def login(self):
    drive.self = self.driver
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

bot = InstagramBot('conhecidojc', 'Juliomendes2020')
bot.login()