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
        self.password = "admin123"
        self.username_locator_name_tag = "username"
        self.password_locator_name_tag = "password"
        self.wait = WebDriverWait(self.driver, timeout=20, poll_frequency=1,
                                  ignored_exceptions=[InvalidSelectorException, ElementClickInterceptedException,
                                                      NoSuchElementException])
        self.wait2 = WebDriverWait(self.driver, timeout=20)


    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def header_check(self):

        username_webelement = self.driver.find_element(By.NAME, self.username_locator_name_tag)
        username_webelement.send_keys(self.username)

        password_webelement = self.driver.find_element(By.NAME, self.password_locator_name_tag)
        password_webelement.send_keys(self.password)

        sleep(3)

        login_path_xpath = '//button[@type="submit"]'
        try:
            login_button_webelement = self.driver.find_element(By.XPATH, login_path_xpath)
        except:
            login_button_webelement = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_path_xpath)))
        login_button_webelement.click()
        sleep(3)

        admin_button = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        try:
            account_admin_webelement = self.driver.find_element(By.XPATH, admin_button)
        except:
            account_admin_webelement = self.wait2.until(EC.element_to_be_clickable((By.XPATH, self.admin_button)))
        account_admin_webelement.click()
        sleep(3)

        user_management_xpath = '//*[contains(text(), "User Management ")]'
        user_management_webelement = self.driver.find_element(By.XPATH, user_management_xpath)
        if user_management_webelement.is_displayed():
            print("The user management header is available")
        else:
            print("The user management header is not available")

        job_xpath = '//*[contains(text(), "Job ")]'
        job_webelement = self.driver.find_element(By.XPATH, job_xpath)
        if job_webelement.is_displayed():
            print("The job header is available")
        else:
            print("The job header is not available")

        organization_xpath = '//*[contains(text(), "Organization ")]'
        organization_webelement = self.driver.find_element(By.XPATH, organization_xpath)
        if organization_webelement.is_displayed():
            print("The organization header is available")
        else:
            print("The organization header is not available")

        qualification_xpath = '//*[contains(text(), "Qualifications ")]'
        qualification_webelement = self.driver.find_element(By.XPATH, qualification_xpath)
        if qualification_webelement.is_displayed():
            print("The qualification header is available")
        else:
            print("The qualification header is not available")

        nationalities_xpath = '//*[contains(text(), "Nationalities")]'
        nationalities_webelement = self.driver.find_element(By.XPATH, nationalities_xpath)
        if nationalities_webelement.is_displayed():
            print("The nationalities header is available")
        else:
            print("The nationalities header is not available")

        corporate_branding_xpath = '//*[contains(text(), "Corporate Branding")]'
        corporate_branding_webelement = self.driver.find_element(By.XPATH, corporate_branding_xpath)
        if corporate_branding_webelement.is_displayed():
            print("The corporate branding header is available")
        else:
            print("The corporate branding header is not available")

        configuration_xpath = '//*[contains(text(), "Configuration")]'
        configuration_webelement = self.driver.find_element(By.XPATH, configuration_xpath)
        if configuration_webelement.is_displayed():
            print("The configuration header is available")
        else:
            print("The configuration header is not available")



        sleep(6)

obj = OrangeHrm()
obj.browse()
sleep(2)
obj.header_check()