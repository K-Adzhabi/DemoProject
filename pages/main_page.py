from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    LOCATOR_ADD_PRODUCT_BUTTON = "//button[@class='btn btn_primary btn_small btn_inventory']"
    LOCATOR_PRODUCT_NAME = "//*[@id='inventory_item_name']"
    LOCATOR_backpack_title = "//*[text()='Sauce Labs Backpack']"
    LOCATOR_jaket_title = "//*[text()='Sauce Labs Fleece Jacket']"
    LOCATOR_tshirt_title = "//*[text()='Test.allTheThings() T-Shirt (Red)']"
    LOCATOR_SHOPPING_CART_BUTTON = "//*[@id='shopping_cart_container']"

    def add_product(self, locator):
        self.driver.find_element(By.XPATH, locator).click()
        self.driver.find_element(By.XPATH, self.LOCATOR_ADD_PRODUCT_BUTTON).click()

    def remove_product_name(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def shopping_bag_button(self):
        self.driver.find_element(By.XPATH, self.LOCATOR_SHOPPING_CART_BUTTON).click()

    def get_shopping_page(self):
        from pages.shoping_cart import ShoppingCart
        return ShoppingCart(self.driver)
