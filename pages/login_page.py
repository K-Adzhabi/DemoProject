from pages.base_page import BasePage
from pages.config import TestData
from selenium.webdriver.common.by import By


class Login(BasePage):
    LOCATOR_USER_NAME = "//*[@id='user-name']"
    LOCATOR_USER_PASS = "//*[@id='password']"
    LOCATOR_LOGIN_BUTTON = "//*[@id='login-button']"

    def enter_login(self):
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_NAME).send_keys(TestData.standard_user_name)
        self.driver.find_element(By.XPATH, self.LOCATOR_USER_PASS).send_keys(TestData.user_password)
        self.driver.find_element(By.XPATH, self.LOCATOR_LOGIN_BUTTON).click()

    def get_main_page(self):
        from pages.main_page import MainPage
        return MainPage(self.driver)
