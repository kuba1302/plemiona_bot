from selenium import webdriver
from time import sleep
import random
from passwords import login, password
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

class PlemionaBot:
    def __init__(self):
        path = r"C:\Users\Admin\Desktop\chromedriver.exe"
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(path)
        
    def wait(self):
        sleep(random.uniform(1, 1.5))

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

    def close_all_popups(self):
        self.close_popup1()
        self.close_popup2()
        self.close_popup3()

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
        # self.driver.find_element_by_class_name('world_button_active').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[10]/div[3]/div[2]/div[1]/a[2]/span').click()
        # close popup
        self.wait()
        self.close_popup1()
        self.close_popup2()

    def handle_exception1(self,a):
        try:
            a
        except ElementNotInteractableException:
            print("Element cannot be clicked")

    ### IMPORTANT VILLAGE, RATUSZ, KOSZARY AND PLAC VIEW WORK ONLY WITH NON GRAPHICAL VILLAGE VIEW
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

    def plac_view(self):
        a = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/'
                                              'tr/td/table/tbody/tr/td[1]/div[1]/div/table/tbody/tr[5]/td/a').click()
        self.handle_exception1(a)

    def farm_manager_view(self):
        a = self.driver.find_element_by_id('manager_icon_farm').click()
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

    def check_time(self, a, b, v):
        # a = your village coords
        # b = enemy village coords
        # v = speed of the slowest unit
        a = np.array(a)
        b = np.array(b)
        c = np.absolute(a - b)
        v = v / 60
        s = np.hypot(c[0], c[1])
        time_in_s = s / (v)
        time_in_s = np.around(time_in_s, 0)
        return time_in_s

    def hour_of_sending_attack(self, a, b, v, time):
        #("year, month, day, hour, minute, seconds, 1/100000 s ")
        travel_time = self.check_time(a, b, v)
        t_wejscia = datetime.datetime(time[0], time[1], time[2], time[3], time[4], time[5], time[6])
        t_wyjscia = t_wejscia - datetime.timedelta(seconds=travel_time)
        return t_wyjscia

    def enter_attack_details(self, armia):
        id_dict = {
            'pik' : ['spear', armia[0]],
            'miecz' : ['sword', armia[1]],
            'top' : ['axe', armia[2]],
            'zw' : ['spy', armia[3]],
            'lk' : ['light', armia[4]],
            'ck' : ['heavy', armia[5]],
            'tar' : ['ram', armia[6]],
            'kat' : ['catapult', armia[7]],
            'ryc' : ['knight', armia[8]],
            'szl' : ['snob', armia[9]],
        }
        for key in id_dict:
            self.driver.find_element_by_id('unit_input_{}'.format(id_dict[key][0])).send_keys(id_dict[key][1])

    def enter_coords(self, b):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table/'
                                          'tbody/tr/td/table/tbody/tr/td/form/div[1]/table/tbody/tr[1]/td/'
                                          'div[2]/input').send_keys('%%%s%%|%%%s%%' % (b[0], b[1]))
        self.wait()

    def click_first_attack(self):
        self.driver.find_element_by_id('target_attack').click()

    def send_attack(self):
        self.driver.find_element_by_id('troop_confirm_go').click()

    def szablon(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/table/tbody/'
                                          'tr/td/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td/a').click()
    def prepare_atack(self, b,army):
        self.wioska_graphic_view()
        self.wait()
        self.bot_plac_graphic_view()
        self.wait()
        # self.hour_of_sending_attack(a, b, v, time)
        self.enter_attack_details(army)
       # self.szablon()
        self.wait()
        self.enter_coords(b)
        self.wait()
        self.click_first_attack()


    def atack_bot(self, a, b, v, time, army):
        sched = BackgroundScheduler()
        sched.start()
        time_left_to_preparing = (self.hour_of_sending_attack(a, b, v, time) - datetime.timedelta(seconds=10))
        time_to_wait = (self.hour_of_sending_attack(a, b, v, time) + datetime.timedelta(seconds=5) - datetime.datetime.now())
        #correcting error
        send_time =  (self.hour_of_sending_attack(a, b, v, time) + datetime.timedelta(seconds=0.9))
        print('Preparation start: ', time_left_to_preparing)
        sched.add_job(self.prepare_atack, 'date', args=[b, army], next_run_time=time_left_to_preparing, timezone='Europe/Warsaw')
        sched.add_job(self.send_attack, 'date', next_run_time=send_time, timezone='Europe/Warsaw')
        print('Hour of sending attack: ', self.hour_of_sending_attack(a, b, v, time))
        sleep(time_to_wait.seconds)


    # click on skrypt
    def zbieractwo_skrypt(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[1]/tbody/tr/td/table/tbody/tr[2]/td[2]/ul/li[7]/span/a').click()

    def bot_plac_graphic_view(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[1]/tbody/tr/td/table/tbody/tr[2]/td[2]/ul/li[5]/span/a').click()


    def zbieractwo_screen(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table'
                                          '/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td[3]/a').click()

    def start_lvl3(self):
        self.driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div[3]/div[3]/div/div[2]/a[1]'
        ).click()
    def start_lvl2(self):
        self.driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div[2]/div[3]/div/div[2]/a[1]').click()

    def start_lvl1(self):
        self.driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div[1]/div[3]/div/div[2]/a[1]').click()

    def bot_wyloguj(self):
        pass

    def wioska_graphic_view(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[2]/'
                                          'tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/a').click()
    def wyloguj(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/a[6]').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[10]/div[3]/div[2]/p/a').click()

    def farmienie_asystent(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/table/tbody/tr/td[6]/a[1]').click()

    def jedno_zbieractwo(self):
        # sleep(random.uniform(15, 200))
        self.wait()
        self.bot_plac_graphic_view()
        self.wait()
        self.zbieractwo_screen()
        self.wait()
        self.zbieractwo_skrypt()
        self.wait()
        self.start_lvl3()
        self.wioska_graphic_view()
        self.wait()
        self.bot_plac_graphic_view()
        self.wait()
        self.zbieractwo_screen()
        self.wait()
        self.zbieractwo_skrypt()
        self.wait()
        self.start_lvl2()
        self.wioska_graphic_view()
        self.wait()
        self.bot_plac_graphic_view()
        self.wait()
        self.zbieractwo_screen()
        self.wait()
        self.zbieractwo_skrypt()
        self.wait()
        self.start_lvl1()

    def farmienie_asystentem(self):
        self.farmienie_asystent()
        self.wait()
        a_clics = self.driver.find_elements_by_css_selector('a.farm_icon_a')
        for click in a_clics:
            try:
                click.click()
                sleep(random.uniform(0.2, 0.4))
            except:
                break


    def farmienie_graczy(self, village_list,  army):
        for village in village_list:
            try:
                self.wait()
                self.prepare_atack(village, army)
                self.wait()
                self.send_attack()
            except:
                break 


    def perma_zbieranie_farmienie(self, village_list, army):
        for i in range(12):
            self.login()
            self.jedno_zbieractwo()
            self.farmienie_graczy(village_list, army)
            self.farmienie_asystentem()
            self.wyloguj()
            sleep(random.uniform(2900, 3000))


village_list = [
    [510, 537], [510, 541],
    [508, 543], [504, 537], [503, 536],
    [510, 532], [509, 545], [500, 539],
    [505, 531],
]
army = [0, 0, 0, 0, 3, 0, 0, 0, 0, 0,]

bot = PlemionaBot()
bot.perma_zbieranie_farmienie(village_list, army)
bot.close()