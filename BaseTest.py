import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome("executable_path="C:\Users\eugen\Downloads\chromedriver-win64.zip\chromedriver-win64"")
    yield driver
    driver.quit()







