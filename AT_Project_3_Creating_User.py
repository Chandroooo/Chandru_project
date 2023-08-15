from hashlib import new
import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        login_button_webelement.click()
        sleep(6)

    def account_creation(self):
        admin_button = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        account_admin_webelement = self.driver.find_element(By.XPATH, admin_button)
        account_admin_webelement.click()
        sleep(3)

        add_button = '//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        add_button_webelement = self.driver.find_element(By.XPATH, add_button)
        add_button_webelement.click()
        sleep(3)

        user_role = '//*[contains(text(), "User Role")]/../following-sibling::div//*[@class="oxd-select-wrapper"]'
        user_role_webelement = self.driver.find_element(By.XPATH, user_role)
        user_role_webelement.click()
        sleep(3)

        selectItem = 'ESS'
        userrole_dropdown = '//*[contains(text(), "User Role")]/../following-sibling::div//*[@class="oxd-select-wrapper"]//div[@role="listbox"]//*[text()="' + selectItem + '"]'
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, userrole_dropdown))).click()
        sleep(6)


        employee_name = '//*[contains(text(), "Employee")]/../following-sibling::div//input'
        employee_name_webelement = self.driver.find_element(By.XPATH, employee_name)
        self.Employee_name = "Ravi M B"
        employee_name_webelement.send_keys(self.Employee_name)
        sleep(3)

        status = '//*[contains(text(), "Status")]/../following-sibling::div//*[@class="oxd-select-wrapper"]'
        status_webelement = self.driver.find_element(By.XPATH, status)
        status_webelement.click()
        sleep(3)

        selectItem1 = 'Enabled'
        status_dropdown = '//*[contains(text(), "Status")]/../following-sibling::div//*[@class="oxd-select-wrapper"]//div[@role="listbox"]//*[text()="' + selectItem1 + '"]'
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, status_dropdown))).click()
        sleep(6)

        username = '//*[contains(text(), "Username")]/../following-sibling::div/input'
        username_webelement = self.driver.find_element(By.XPATH, username)
        self.username = "cndru040"
        username_webelement.send_keys(self.username)
        sleep(6)

        password = '//*[contains(text(), "Password")]/../following-sibling::div/input'
        password_webelement = self.driver.find_element(By.XPATH, password)
        self.password = "Password@123"
        password_webelement.send_keys(self.password)
        sleep(6)

        confirm_password = '//*[contains(text(), "Confirm Password")]/../following-sibling::div/input'
        confirm_password_webelement = self.driver.find_element(By.XPATH, confirm_password)
        self.confirm_password = "Password@123"
        confirm_password_webelement.send_keys(self.confirm_password)
        sleep(6)

        save_button = '//*[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        save_button_webelement = self.driver.find_element(By.XPATH, save_button)
        save_button_webelement.click()
        sleep(3)



obj = OrangeHrm()
obj.browse()
sleep(2)
obj.input_credentials()
obj.account_creation()