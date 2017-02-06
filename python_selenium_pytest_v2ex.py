

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
driver.get("https://www.v2ex.com/")


#@pytest.mark.parametrize('username,password', (('betty200744','1234qwer')))
class TestV2ex:
    def setup_class(cls):
        print 'setup class=====>%s' %(cls.__name__)

    def teardown_class(cls):
       # driver.close()
        pass


    @pytest.fixture
    def login(self):
        driver.find_element_by_xpath("//a[@href='/signin']").click()
        WebDriverWait(driver, 1 ).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "sl")))
        driver.find_element_by_xpath("//*[@id='Main']/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input").send_keys('htzhao200744')
        driver.find_element_by_xpath("//input[@type='password']").send_keys('1234qwer')
        driver.find_element_by_xpath("//input[@type='submit']").click()

    @pytest.fixture
    def logout(self):
        driver.find_element_by_xpath("//*[@id='Top']/div/div/table/tbody/tr/td[3]/a[7]").click()
        Alert(driver).accept()


    def test_valid_login(self):
        driver.find_element_by_xpath("//a[@href='/signin']").click()
        WebDriverWait(driver, 1 ).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "sl")))
        driver.find_element_by_xpath("//*[@id='Main']/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input").send_keys('htzhao200744')
        driver.find_element_by_xpath("//input[@type='password']").send_keys('1234qwer')
        driver.find_element_by_xpath("//input[@type='submit']").click()
        assert driver.find_element_by_xpath("//a[@href='/member/htzhao200744']").text == "htzhao200744"
        driver.find_element_by_xpath("//*[@id='Top']/div/div/table/tbody/tr/td[3]/a[7]").click()
        Alert(driver).accept()




    @pytest.mark.parametrize('username, password', (
            ('abc', '123'),
            ('betty200744','456'),
    ))
    def test_invalid_login(self,username,password):
        driver.find_element_by_xpath("//a[@href='/signin']").click()
        WebDriverWait(driver, 1 ).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "sl")))
        driver.find_element_by_xpath("//*[@id='Main']/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input").send_keys(username)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        assert driver.find_element_by_class_name("problem").is_displayed()


    def test_action_favorite_it(self,login):
        login
        befor_favorite = driver.find_element_by_xpath("//*[@id='Rightbar']/div[2]/div[1]/table[2]/tbody/tr/td[2]/a/span[1]").text
        driver.find_element_by_xpath("//*[@id='Main']/div[2]/div[3]/table/tbody/tr/td[3]/span[1]/a").click()
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,"//*[@id='Main']/div[2]/div[3]/a[1]")))
        driver.find_element_by_xpath("//*[@id='Main']/div[2]/div[3]/a[1]").click()
        after_favorite = driver.find_element_by_xpath("//*[@id='Rightbar']/div[2]/div[1]/table[2]/tbody/tr/td[2]/a/span[1]").text
        assert int(after_favorite) != int(befor_favorite)



    def test_action_favorite_node(self,login):
        login
        befor_favo_node = driver.find_element_by_xpath("//*[@id='Rightbar']/div[2]/div[1]/table[2]/tbody/tr/td[1]/a/span[1]").text
        driver.find_element_by_xpath("//*[@id='Main']/div[2]/div[2]/a[1]").click()
        after_favo_node = driver.find_element_by_xpath("//*[@id='Rightbar']/div[2]/div[1]/table[2]/tbody/tr/td[1]/a/span[1]").text
        assert befor_favo_node != after_favo_node

















