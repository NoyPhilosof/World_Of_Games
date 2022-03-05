# functions for testing the game's flask service
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_service = Service('./chromedriver')
chrome_driver = webdriver.Chrome(service=chrome_service)


def test_scores_service(url):
    """
    This function checks if the score element in a file is between 1 and 1000. if it is, the func returns True
    if it isn't, the return will be False. This function also checks whether the flask web service is indeed running
    :argument url address (string)
    :rtype boolean or -1 if server is not running
    """
    try:
        chrome_driver.get(url)

    except WebDriverException:
        print('Flask web server is not running')
        return -1

    else:
        whats_da_score = chrome_driver.find_element(By.XPATH, '//*[@id="score"]')
        value_as_int = int(whats_da_score.text)
        if 0 < value_as_int < 1001:
            return 0
        else:
            return -1


def main_function(url='http://localhost:5000/success'):
    """
    this function runs the pre-defined tests for the flask web service
    :argument url as a string
    :rtype 0 for success, -1 for failure
    """
    web_service_test = test_scores_service(url)
    return web_service_test
