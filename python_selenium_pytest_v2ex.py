

import pytest
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


#@pytest.mark.parametrize('username,password', (('betty200744','1234qwer')))
class TestV2ex:
    driver.get("https://www.v2ex.com/")

    def setup_class(cls):
        print 'setup class=====>%s' %(cls.__name__)

    def teardown_class(cls):
        pass

    @pytest.mark.parametrize('username, password', (
            ('abc', '123'),
            ('betty200744','456'),
    ))
    def test_invalid_login(self,username,password):
        driver.find_element_by_xpath("//table//a[@href='/signin']").click()
        WebDriverWait(driver, 1 ).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "sl")))
        driver.find_element_by_xpath("//form[@method='post']//input[@type='text']").send_keys(username)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        assert driver.find_element_by_class_name("problem").is_displayed()

    #TODO
    def test_switch_tab_subtab(self):
        pass
    #TODO
    def test_v2ex_search(self):
        pass
#

class TestMyV2ex:
    driver.get("https://www.v2ex.com/")

    @pytest.fixture
    def login(self):
        driver.find_element_by_xpath("//a[@href='/signin']").click()
        WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "sl")))
        driver.find_element_by_xpath("//form[@method='post']//input[@type='text']").send_keys(
            'htzhao200744')
        driver.find_element_by_xpath("//input[@type='password']").send_keys('1234qwer')
        driver.find_element_by_xpath("//input[@type='submit']").click()

    @pytest.fixture
    def logout(self):
        driver.find_element_by_xpath("//a[@href='#;']").click()
        Alert(driver).accept()

    def setup_class(cls):
        print 'setup class=====>%s' % (cls.__name__)
        driver.find_element_by_xpath("//a[@href='/signin']").click()
        WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "sl")))
        driver.find_element_by_xpath("//form[@method='post']//input[@type='text']").send_keys(
            'htzhao200744')
        driver.find_element_by_xpath("//input[@type='password']").send_keys('1234qwer')
        driver.find_element_by_xpath("//input[@type='submit']").click()


    def teardown_class(cls):
        driver.close()

    #use Xpath=//*[contains(@type,'sub')]
    #TODO Need add re pattern
    def test_action_favorite_it(self):
        befor_favorite = driver.find_element_by_xpath("//a[@href='/my/topics']//span[@class='bigger']").text
        driver.find_element_by_xpath("//span[@class='item_title'][1]").click()
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@href,'favorite')]")))
        driver.find_element_by_xpath("//a[contains(@href,'favorite')]").click()
        after_favorite = driver.find_element_by_xpath("//a[@href='/my/topics']//span[@class='bigger']").text
        assert int(after_favorite) != int(befor_favorite)


    def test_action_favorite_node(self):
        driver.get("https://www.v2ex.com/")
        befor_favo_node = driver.find_element_by_xpath("//a[@href='/my/nodes']//span[@class='bigger']").text
        driver.find_element_by_xpath("//a[contains(@href, '/go/')][1]").click()
        driver.find_element_by_xpath("//a[contains(@href,'favorite')]").click()
        after_favo_node = driver.find_element_by_xpath("//a[@href='/my/nodes']//span[@class='bigger']").text
        assert befor_favo_node != after_favo_node

    #TODO
    def test_check_my_favorite_summy(self):
        pass
    #TODO
    def test_check_my_favorite_node(self):
        pass






