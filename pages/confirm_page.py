import time

from pages.base_page import BasePage
from pages.config import TestData
from selenium.webdriver.common.by import By


class ConfirmPage(BasePage):
    LOCATOR_FIRST_NAME = "//*[@id='first-name']"
    LOCATOR_LAST_NAME = "//*[@id='last-name']"
    LOCATOR_ZIP_CODE = "//*[@id='postal-code']"
    LOCATOR_CONTINUE_BUTTON = "//*[@id='continue']"
    LOCATOR_FINISH_BUTTON = "//*[@id='finish']"

    def info_input(self):
        self.driver.find_element(By.XPATH, self.LOCATOR_FIRST_NAME).send_keys(TestData.FIRST_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_LAST_NAME).send_keys(TestData.LAST_NAME)
        self.driver.find_element(By.XPATH, self.LOCATOR_ZIP_CODE).send_keys(TestData.ZIP_code)

    def continue_button(self):
        self.driver.find_element(By.XPATH, self.LOCATOR_CONTINUE_BUTTON).click()

    def finish_button(self):
        self.driver.find_element(By.XPATH, self.LOCATOR_FINISH_BUTTON).click()
        time.sleep(5)

    def get_back_home_page(self):
        from pages.back_home_page import BackHomePage
        return BackHomePage(self.driver)
