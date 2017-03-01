
#coding=utf-8

import pytest
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from actions import *
from verificaton import *

driver = init_driver()


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
        click_signin_element()
        input_username(username)
        input_password(password)
        click_submit()
        check_is_login_failed()


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
        click_signin_element()
        input_username('htzhao200744')
        input_password('1q2w3e4r')
        click_submit()

    @pytest.fixture
    def logout(self):
        click_signout_element()
        alert_accept()

    def setup_class(cls):
        print 'setup class=====>%s' % (cls.__name__)
        click_signin_element()
        input_username('htzhao200744')
        input_password('1q2w3e4r')
        click_submit()


    def teardown_class(cls):
        driver.close()

    #use Xpath=//*[contains(@type,'sub')]
    #TODO Need add re pattern
    def test_action_favorite_it(self):
        befor_favorite = get_my_topics_value()
        click_first_item()
        click_favorite_item_element()
        after_favorite = get_my_topics_value()
        assert int(after_favorite) != int(befor_favorite)


    def test_action_favorite_node(self):
        driver.get("https://www.v2ex.com/")
        befor_favo_node = get_my_nodes_value()
        click_first_node()
        click_favorite_node_element()
        after_favo_node = get_my_nodes_value()
        assert befor_favo_node != after_favo_node

    #TODO
    def test_check_my_favorite_summy(self):
        pass

    #TODO
    def test_check_my_favorite_node(self):
        pass


    #TODO, bug,  the pre element can not use send_keys()
    def test_create_topics(self):
        driver.get("https://www.v2ex.com/")
        click_create_topics_element_in_main()
        input_topic_title()
        # content = driver.execute_script('document.querySelectorAll("textarea#editor").style.visibility = "";')
        # content.send_keys('test')
        select_topics_node()





