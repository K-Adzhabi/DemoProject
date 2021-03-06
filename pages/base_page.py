from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element_text(self, locator):
        element_text = self.driver.find_element(By.XPATH, locator)
        return element_text.text
