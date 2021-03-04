from selenium import webdriver
from time import sleep
import random
from password import login, password
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import pandas as pd

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
        except NoSuchElementException:
            print("Pop-up 1 not found")

    def close_popup2(self):
        # Are you sure, there wont be another chance popuo
        try:
            self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div/button[1]').click()
            print("Closing pop-up 2")
        except NoSuchElementException:
            print("Pop-up 2 not found")

    def close_popup3(self):
        # Getting award popuo
        try:
            self.driver.find_element_by_xpath('/html/body/div[11]/div[1]/div/div/div[2]/a').click()
            print("Closing pop-up 3")
        except NoSuchElementException:
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

    def handle_exception1(self,a):
        try:
            a
        except ElementNotInteractableException:
            print("Element cannot be clicked")

    # Whole village view
    def village_view(self):

        a = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[1]'
                                              '/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/a').click()
        self.handle_exception1(a)
    # Views of particular buildings
    def ratusz_view(self):
        a = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/'
                                              'tbody/tr/td/table/tbody/tr/td[1]/div[1]/div/table/tbody/tr[1]/td/a').click()
        self.handle_exception1(a)
    def koszary_view(self):
        a = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td[1]/div[1]/div/table/tbody/tr[2]/td/a').click()
        self.handle_exception1(a)

    def check_resources(self):
        resources = {
            'drewno': self.driver.find_element_by_id('wood').text,
            'glina' : self.driver.find_element_by_id('stone').text,
            'zelazo' : self.driver.find_element_by_id('iron').text,
        }
        global resources_df
        resources_df= pd.DataFrame(resources, index=[0])
        for x in resources:
            print(x, resources[x])

    # Recrouting diffrent units
    def recrout_pikinier(self, number):
        self.driver.find_element_by_id('spear_0').send_keys(number)
        a = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input').click()
        self.handle_exception1(a)


    # functions to upgrade every building in town hole
    def build_info(self):
        build_dict = {
            'ratusz' : 1,
            'koszary' : 2,
            'rynek' : 3,
            'tartak' : 4,
            'cegielnia' : 5,
            'huta' : 6,
            'zagroda' : 7,
            'spichlerz': 8,
            'schowek' : 9,
            'mur' : 10
                 }
        return build_dict

    def extract(self, driver_info):
        list = []
        for i in range(len(driver_info)):
            list.append(driver_info[i].text)
        return list

    def build_resources_needed(self):
        self.ratusz_view()
        global building_cost
        data = {
            'drewno' : self.extract(self.driver.find_elements_by_class_name('cost_wood')),
            'glina' : self.extract(self.driver.find_elements_by_class_name('cost_stone')),
            'zelazo' : self.extract(self.driver.find_elements_by_class_name('cost_iron'))

        }
        #self.driver.find_elements_by_class_name('cost_wood'
        building_cost = pd.DataFrame(data)
        names = ['ratusz', 'koszary', 'kuznia', 'rynek', 'tartak', 'cegielnia', 'huta', 'zagroda', 'spichlerz', 'schowek', 'mur']
        building_cost.insert(loc=0, column='buildings', value=names)
        print(building_cost)

    def building(self, name):
        build_btns = self.driver.find_elements_by_css_selector('a.btn.btn-build')
        a = build_btns[self.build_info()[name]]
        self.handle_exception1(a)
        print("Building {}".format(name))

    def robienie_darmowki(self):
        pass

