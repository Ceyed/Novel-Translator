from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utils.log import log

def wait_for_page_to_load(driver):
    # * Find chapter links
    delay = 3 # seconds

    log('Waiting for chapter list to load..')

    try:
        links = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, """//*[(@id = "catalog")]//a""")))
    except TimeoutException:
        print("Loading took too much time!")
        exit(1)

    log('Done', end=True)
