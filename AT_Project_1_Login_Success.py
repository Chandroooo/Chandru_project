from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class OrangeHrm:

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com"
        self.driver = webdriver.Chrome()
        self.username = "Admin"
        self.password = "admin123"
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
        if login_button_webelement.is_displayed():
            login_button_webelement.click()
            print("The user is logged in successfully")
        else:
            print("Invalid Employee login to OrangeHRM portal")
        sleep(6)



obj = OrangeHrm()
obj.browse()
sleep(2)
obj.input_credentials()