from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class OrangeHrm:

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com"
        self.driver = webdriver.Edge()
        self.username = "Admin"
        self.username_locator_name_tag = "username"
        self.wait = WebDriverWait(self.driver, timeout=20, poll_frequency=1,
                                  ignored_exceptions=[InvalidSelectorException, ElementClickInterceptedException,
                                                      NoSuchElementException])
        self.wait2 = WebDriverWait(self.driver, timeout=20)


    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def reset_password(self):

        forgot_button = '//*[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]'
        try:
            forgot_button_webelement = self.driver.find_element(By.XPATH, forgot_button)
        except:
            forgot_button_webelement = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.forgot_button)))
        forgot_button_webelement.click()
        sleep(3)

        username_webelement = self.driver.find_element(By.NAME, self.username_locator_name_tag)
        username_webelement.send_keys(self.username)
        sleep(3)

        reset_password = '//*[@class="oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset"]'
        try:
            reset_password_webelement = self.driver.find_element(By.XPATH, reset_password)
        except:
            reset_password_webelement = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.reset_password)))
        reset_password_webelement.click()
        sleep(3)



obj = OrangeHrm()
obj.browse()
sleep(2)
obj.reset_password()