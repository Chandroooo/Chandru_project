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

    def main_menu(self):

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

        admin_tab_xpath = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        admin_tab_webelement = self.driver.find_element(By.XPATH, admin_tab_xpath)
        if admin_tab_webelement.is_displayed():
            print("The admin tab is available")
        else:
            print("The admin tab is not available")

        pim_tab_xpath = '//a[@href="/web/index.php/pim/viewPimModule"]'
        pim_tab_webelement = self.driver.find_element(By.XPATH, pim_tab_xpath)
        if pim_tab_webelement.is_displayed():
            print("The pim tab is available")
        else:
            print("The pim tab is not available")

        leave_tab_xpath = '//a[@href="/web/index.php/leave/viewLeaveModule"]'
        leave_tab_webelement = self.driver.find_element(By.XPATH, leave_tab_xpath)
        if leave_tab_webelement.is_displayed():
            print("The leave tab is available")
        else:
            print("The leave tab is not available")

        time_tab_xpath = '//a[@href="/web/index.php/time/viewTimeModule"]'
        time_tab_webelement = self.driver.find_element(By.XPATH, time_tab_xpath)
        if time_tab_webelement.is_displayed():
            print("The time tab is available")
        else:
            print("The time tab is not available")

        recruitment_tab_xpath = '//a[@href="/web/index.php/recruitment/viewRecruitmentModule"]'
        recruitment_tab_webelement = self.driver.find_element(By.XPATH, recruitment_tab_xpath)
        if recruitment_tab_webelement.is_displayed():
            print("The recruitment tab is available")
        else:
            print("The recruitment tab is not available")

        my_info_tab_xpath = '//a[@href="/web/index.php/pim/viewMyDetails"]'
        my_info_tab_webelement = self.driver.find_element(By.XPATH, my_info_tab_xpath)
        if my_info_tab_webelement.is_displayed():
            print("The my info tab is available")
        else:
            print("The my info tab is not available")

        performance_tab_xpath = '//a[@href="/web/index.php/performance/viewPerformanceModule"]'
        performance_tab_webelement = self.driver.find_element(By.XPATH, performance_tab_xpath)
        if performance_tab_webelement.is_displayed():
            print("The performance tab is available")
        else:
            print("The performance tab is not available")

        dashboard_tab_xpath = '//a[@href="/web/index.php/dashboard/index"]'
        dashboard_tab_webelement = self.driver.find_element(By.XPATH, dashboard_tab_xpath)
        if dashboard_tab_webelement.is_displayed():
            print("The dashboard tab is available")
        else:
            print("The dashboard tab is not available")

        directory_tab_xpath = '//a[@href="/web/index.php/directory/viewDirectory"]'
        directory_tab_webelement = self.driver.find_element(By.XPATH, directory_tab_xpath)
        if directory_tab_webelement.is_displayed():
            print("The directory tab is available")
        else:
            print("The directory tab is not available")

        maintenance_tab_xpath = '//a[@href="/web/index.php/maintenance/viewMaintenanceModule"]'
        maintenance_tab_webelement = self.driver.find_element(By.XPATH, maintenance_tab_xpath)
        if maintenance_tab_webelement.is_displayed():
            print("The maintenance tab is available")
        else:
            print("The maintenance tab is not available")

        claim_tab_xpath = '//a[@href="/web/index.php/claim/viewClaimModule"]'
        claim_tab_webelement = self.driver.find_element(By.XPATH, claim_tab_xpath)
        if claim_tab_webelement.is_displayed():
            print("The claim tab is available")
        else:
            print("The claim tab is not available")

        buzz_tab_xpath = '//a[@href="/web/index.php/buzz/viewBuzz"]'
        buzz_tab_webelement = self.driver.find_element(By.XPATH, buzz_tab_xpath)
        if claim_tab_webelement.is_displayed():
            print("The buzz tab is available")
        else:
            print("The buzz tab is not available")


        sleep(6)

obj = OrangeHrm()
obj.browse()
sleep(2)
obj.main_menu()