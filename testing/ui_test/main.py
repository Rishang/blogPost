from selenium import webdriver
import requests
from nncat import checkConnection

chrome_options = webdriver.ChromeOptions()

def test():

    # check connection before starting tests
    checkConnection("chrome_browser", 4444, 10)
    checkConnection("backend", 8000, 30)

    driver = webdriver.Remote(
        command_executor='http://chrome_browser:4444',
        options=chrome_options
    )
    driver.get("http://backend:8000")

    print('sucess')
    driver.quit()


test()