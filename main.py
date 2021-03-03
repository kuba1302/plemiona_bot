from selenium import webdriver
from time import sleep
import random
from password import login, password

class PlemionaBot:
    def __init__(self):
        path = r"C:\Users\Admin\Desktop\chromedriver.exe"
        self.driver = webdriver.Chrome(path)

    def close_popup(self):
        self.driver.find_element_by_xpath('/html/body/div[11]/div[1]/div/a').click()

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
        self.close_popup()

    def village_view(self):
        self.bot.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[1]'
                                              '/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/a').click()

    def ratusz_view(self):
        self.bot.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/'
                                              'tbody/tr/td/table/tbody/tr/td[1]/div[1]/div/table/tbody/tr[1]/td/a').click()
    def ratusz_build(self):
        self.bot.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody'
                                              '/tr/td/table/tbody/tr/td/div/table[1]/tbody/tr[2]/td[7]/a[2]').click()
    def tartak_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/'
                                          'tr/td/div/table[1]/tbody/tr[2]/td[7]/a[2]').click()
    def cegielnia_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td/div/table[1]/tbody/tr[7]/td[7]/a[2]').click()
    def huta_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td/div/table[1]/tbody/tr[8]/td[7]/a[2]')