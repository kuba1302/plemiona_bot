from selenium import webdriver
from time import sleep
import random
from password import login, password

class Plemiona_bot:
    def __init__(self):
        path = r"C:\Users\Admin\Desktop\chromedriver.exe"
        self.driver = webdriver.Chrome(path)
    def login(self):
        self.driver.get("https://www.plemiona.pl")
        # input login and password
        self.driver.find_element_by_id('user').send_keys(login)
        self.driver.find_element_by_id('password').send_keys(password)
        # click on login button
        self.driver.find_element_by_class_name('btn-login').click()
        # select active world
        self.driver.find_element_by_class_name('world_button_active').click()
        # close popup
        self.driver.find_element_by_xpath('/html/body/div[11]/div[1]/div/a').click()
