
from autotets.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ShopingCart(BasePage):
    LOCATOR_PRODUCT_SHOP = "//*[text()='Sauce Labs Backpack']"
    LOCATOR_back_to_product_button = "//button[@class='btn btn_secondary back btn_large inventory_"\
                                     "details_back_button']"
    LOCATOR_CHECKOUT_BUTTON = "//button[@class='btn btn_action btn_medium checkout_button']"
    LOCATOR_REMOVE_BUTTON = "//button[@class='btn btn_secondary btn_small btn_inventory']"
    LOCATOR_COUNT_PRODUCT_3 = "//*[@class='shopping_cart_badge']"
    LOCATOR_COUNT_PRODUCT_2 = "//*[@class='shopping_cart_badge']"

    def back_to_products(self):
        self.driver.find_element(By.XPATH, self.LOCATOR_back_to_product_button).click()

    def remove_button(self):
        self.driver.find_element(By.XPATH, self.LOCATOR_REMOVE_BUTTON).click()

    def checkout_button(self):
        self.driver.find_element(By.XPATH, self.LOCATOR_CHECKOUT_BUTTON).click()

    def get_confirm_page(self):
        from autotets.pages.confirm_page import ConfirmPage
        return ConfirmPage(self.driver)

