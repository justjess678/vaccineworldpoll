#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:10:04 2020

@author: jess
"""

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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

reps = 0
start = time.time()
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'images': 2, 'javascript': 2}}
options.add_argument("headless")
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome("./chromedriver", options=options)
driver.get('https://www.worldvaccinepoll.com/')

while(True):
    
    iframes = driver.find_elements_by_tag_name("iframe")
    for iframe in iframes:
        driver.switch_to_frame(iframe)
        question = driver.find_element_by_xpath('//h1[@id="question"]').text
        answers = driver.find_elements_by_xpath('//span[@class="text"]')
        for answer in answers:
            if "Was Gov't reaction to COVID-19 worse than the virus?" in question and "No" in answer.text:
                #click no
                answer.click()
            else:
                #click yes
                if "Yes" in answer.text:
                    answer.click()
        driver.switch_to_default_content()
    reps+=1
    driver.refresh()
    print("Average time =", (time.time() - start)/reps )
driver.close()
