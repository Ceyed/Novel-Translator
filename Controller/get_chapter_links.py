from selenium.webdriver.common.by import By
from Utils.log import log


def get_chapter_links(driver):
    # * Get chapters links
    log('Extracting chapter links..')
    
    chapter_links = driver.find_elements(by=By.XPATH, value="""//*[(@id = "catalog")]//a""")
    links = []
    for link in chapter_links:
        title = link.text.split(' ')
        if len(title) > 1:
            title[1] = title[1].zfill(3)
        links.append((' '.join(title), link.get_attribute('href')))

    log('Done', end=True)
    return links
