from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class BackHomePage(BasePage):
    LOCATOR_BACK_HOME_BUTTON = "/html/body/div/div/div/div[2]/button"

    def back_home(self):
        self.driver.find_element(By.XPATH, self.LOCATOR_BACK_HOME_BUTTON).click()
        time.sleep(3)
