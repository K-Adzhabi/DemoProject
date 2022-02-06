import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="H:\PyCharm\pythonProject\chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    yield driver
    time.sleep(10)
    driver.quit()
