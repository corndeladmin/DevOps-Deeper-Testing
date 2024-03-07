import os
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

@pytest.fixture(scope="module")
def driver():
    load_dotenv()
    browser = os.getenv("BROWSER", "chrome")
    if browser == "chrome":
        with webdriver.Chrome() as driver:
            yield driver
    elif browser == "firefox":
        with webdriver.Firefox() as driver:
            yield driver
    elif browser == "safari":
        with webdriver.Safari() as driver:
            yield driver
    else:
        raise Exception(f"Browser {browser} is not supported. Please select one of chrome, firefox or safari")

def test_chrome_open_google(driver):
    driver.get("https://google.com")

    # handle cookie pop up
    try:
        element = driver.find_element(By.XPATH, '//div[text()="Reject all"]')
        element.click()
    except:
        # continue onwards
        pass
    
    search_box = driver.find_element(By.XPATH, '//textarea')
    search_box.send_keys("Hey look, I'm using selenium!")
    search_box.send_keys(Keys.RETURN)

    # Leave the screen up for a few seconds
    # just while we're watching the tests directly
    sleep(3)
