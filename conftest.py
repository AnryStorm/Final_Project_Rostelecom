import time
import pytest
from selenium import webdriver
from faker import Faker


@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome(executable_path='chrome.exe')

    yield driver
    driver.quit()