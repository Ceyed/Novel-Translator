from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver_manager
from Utils.log import log


def setup_driver(url):
    # * Setup driver
    log('Setting up driver..')

    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)           # * Not closing browser after job finished
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    log('Done', end=True)

    return driver
