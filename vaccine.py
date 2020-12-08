#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:10:04 2020

@author: jess
"""

import time

from tbselenium.tbdriver import TorBrowserDriver
from os.path import dirname, join, realpath, getsize

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def load(length=5):
    for i in range(0, length):
        print(". ", end=" ")
        time.sleep(1)
    print("")

while(True):
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {'images': 2, 'javascript': 2}}
    options.add_argument("headless")
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome("./chromedriver", options=options)
    driver.get('https://www.worldvaccinepoll.com/')
    
    iframes = driver.find_elements_by_tag_name("iframe")
    for iframe in iframes:
        driver.switch_to_frame(iframe)
        question = driver.find_element_by_xpath('//h1[@id="question"]').text
        answers = driver.find_elements_by_xpath('//span[@class="text"]')
        print(question)
        for answer in answers:
            if "Was Gov't reaction to COVID-19 worse than the virus?" in question:
                #click no
                if "No" in answer.text:
                    answer.click()
                    print(answer.text)
            else:
                #click yes
                if "Yes" in answer.text:
                    answer.click()
                    print(answer.text)
        driver.switch_to_default_content()
    driver.refresh()
driver.close()