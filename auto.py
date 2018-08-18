# -*- coding: utf-8 -*-
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

profile_path = os.path.dirname(os.path.realpath(__file__))

#

my_email = ""
my_pass = ""


def login():
    opts = FirefoxOptions()
    # opts.add_argument("--headless")
    profile = webdriver.FirefoxProfile(profile_path)
    profile.set_preference("dom.webnotifications.enabled", False);
    driver = webdriver.Firefox(firefox_profile=profile, firefox_options=opts)

    driver.get("https://www.facebook.com")
    print(f"access to facebook.... ")
    # sp2 = self.profile.find_element_by_xpath()
    # email = driver.find_element_by_id("email")
    email = driver.find_element(By.ID, 'email')

    email.send_keys(my_email)
    passw = driver.find_element(By.ID, 'pass')
    passw.send_keys(my_pass)

    submit = driver.find_element(By.XPATH,'//input[@type="submit"]')
    submit.click()
    time.sleep(2)
    stt = driver.find_element(By.XPATH, '//span[contains(text(),"Make Post")]')
    stt.click()
    stt_val = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']")))
    stt_val.send_keys("Hi there, This's post will be created by selenium itself");
    post = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//button[@data-testid="react-composer-post-button"]')))
    post.click()
    driver.close()
if __name__ == "__main__":

    login()
