from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class OrangeHrm:

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com"
        self.driver = webdriver.Chrome()
        self.username = "Admin"
        self.password = "Invalid password"
        self.username_locator_name_tag = "username"
        self.password_locator_name_tag = "password"


    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def input_credentials(self):

        username_webelement = self.driver.find_element(By.NAME, self.username_locator_name_tag)
        username_webelement.send_keys(self.username)

        password_webelement = self.driver.find_element(By.NAME, self.password_locator_name_tag)
        password_webelement.send_keys(self.password)

        sleep(3)

        login_path_xpath = '//button[@type="submit"]'
        login_button_webelement = self.driver.find_element(By.XPATH, login_path_xpath)
        login_button_webelement.click()
        sleep(3)
        login_failure_xpath = '//*[@class="oxd-alert-content oxd-alert-content--error"]'
        login_failure_xpath = self.driver.find_element(By.XPATH, login_failure_xpath)
        if login_failure_xpath.is_displayed():
            print("Invalid credentials")
        else:
            print("The user is logged in successfully")
        sleep(3)


obj = OrangeHrm()
obj.browse()
sleep(2)
obj.input_credentials()