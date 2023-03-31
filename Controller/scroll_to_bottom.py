from time import sleep
from Utils.log import log

def scroll_to_bottom(driver):
    # * Scroll down to bottom
    log('Scrolling down to bottom of page..')

    while True:
        driver.execute_script("window.scrollBy(0, 620)")

        sleep(1)

        pageHeight = driver.execute_script("return document.body.scrollHeight")
        totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")

        if (pageHeight-1) <= totalScrolledHeight:
            break

    log('Done', end=True)
