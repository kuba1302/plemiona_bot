from selenium import webdriver
from time import sleep
import random
from password import login, password

class PlemionaBot:
    def __init__(self):
        path = r"C:\Users\Admin\Desktop\chromedriver.exe"
        self.driver = webdriver.Chrome(path)

    def wait(self):
        sleep(random.uniform(1, 2.5))

    def close_popup1(self):
        # The most common popup, daily
        try:
            self.driver.find_element_by_xpath('/html/body/div[11]/div[1]/div/a').click()
            print("Closing pop-up 1")
        except:
            print("Pop-up 1 not found")

    def close_popup2(self):
        # Are you sure, there wont be another chance popuo
        try:
            self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div/button[1]').click()
            print("Closing pop-up 2")
        except:
            print("Pop-up 2 not found")

    def close_popup3(self):
        # Getting award popuo
        try:
            self.driver.find_element_by_xpath('/html/body/div[11]/div[1]/div/div/div[2]/a').click()
            print("Closing pop-up 3")
        except:
            print("Pop-up 3 not found")
    def login(self):
        print("Loging in...")
        self.driver.get("https://www.plemiona.pl")
        self.wait()
        # input login and password
        self.driver.find_element_by_id('user').send_keys(login)
        self.wait()
        self.driver.find_element_by_id('password').send_keys(password)
        # click on login button
        self.wait()
        self.driver.find_element_by_class_name('btn-login').click()
        # select active world
        self.wait()
        self.driver.find_element_by_class_name('world_button_active').click()
        # close popup
        self.wait()
        self.close_popup1()
        self.close_popup2()

    # Whole village view
    def village_view(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[1]'
                                              '/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/a').click()
    # Views of particular buildings
    def ratusz_view(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/'
                                              'tbody/tr/td/table/tbody/tr/td[1]/div[1]/div/table/tbody/tr[1]/td/a').click()
    def koszary_view(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td[1]/div[1]/div/table/tbody/tr[2]/td/a').click()
    # functions to upgrade every building in town hole
    def ratusz_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody'
                                              '/tr/td/table/tbody/tr/td/div/table[1]/tbody/tr[2]/td[7]/a[2]').click()
    def koszary_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/'
                                          'tr/td/div/table[1]/tbody/tr[3]/td[7]/a[2]').click()
    def tartak_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/'
                                          'tr/td/div/table[1]/tbody/tr[2]/td[7]/a[2]').click()
    def cegielnia_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td/div/table[1]/tbody/tr[7]/td[7]/a[2]').click()
    def huta_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td/div/table[1]/tbody/tr[8]/td[7]/a[2]').click()
    def zagroda_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td/div/table[1]/tbody/tr[9]/td[7]/a[2]').click()
    def spichlerz_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td/div/table[1]/tbody/tr[10]/td[7]/a[2]').click()
    def schowek_build(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/'
                                          'tr/td/div/table[1]/tbody/tr[11]/td[7]/a[2]').click()
