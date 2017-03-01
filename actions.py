


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

driver = webdriver.Chrome()

def init_driver():
    return driver

def alert_accept():
    Alert(driver).accept()

def alert_dismiss():
    Alert(driver).dismiss()


def click_signin_element():
    driver.find_element_by_xpath("//table//a[@href='/signin']").click()
    WebDriverWait(driver, 1 ).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "sl")))

def click_submit():
        driver.find_element_by_xpath("//input[@type='submit']").click()


def click_signout_element():
    driver.find_element_by_xpath("//a[@href='#;']").click()


def click_first_item():
    driver.find_element_by_xpath("//span[@class='item_title'][1]").click()


def click_favorite_item_element():
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'favorite')]")))
    driver.find_element_by_xpath("//a[contains(@href,'favorite')]").click()

def click_first_node():
    driver.find_element_by_xpath("//a[contains(@href, '/go/')][1]").click()

def click_favorite_node_element():
    driver.find_element_by_xpath("//a[contains(@href,'favorite')]").click()

def click_create_topics_element_in_main():
    driver.find_element_by_xpath("//a[@href='/new']").click()



def get_my_nodes_value():
    text = driver.find_element_by_xpath("//a[@href='/my/nodes']//span[@class='bigger']").text
    return text

def get_my_topics_value():
    text = driver.find_element_by_xpath("//a[@href='/my/topics']//span[@class='bigger']")
    return text

def input_username(username):
        driver.find_element_by_xpath("//form[@method='post']//input[@type='text']").send_keys(username)


def input_password(password):
    driver.find_element_by_xpath("//input[@type='password']").send_keys(password)

def input_topic_title():
    driver.find_element_by_css_selector("textarea.msl").send_keys("test")

def input_topic_content():
    content = driver.execute_script('document.querySelectorAll("textarea#editor").style.visibility = "";')
    content.send_keys('test')



def select_topics_node():
    driver.find_element_by_css_selector("div.select2-container>a")
    driver.find_element_by_css_selector("input.select2-input").send_keys("python")
    driver.find_element_by_css_selector("div.select2-result-label").click()
    driver.find_element_by_css_selector("button[type=button]").click()




