from time import sleep

import pyperclip
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Model.db import set_translation
from Utils.log import done_log, log



def translate_chapter(driver, link):
    # log(f'Translate chapter: {link[0]}')

    google_translate_url = "https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&op=translate"

    chapter_page = requests.get(link[1])
    chapter_page.raise_for_status()
    chapter_page.encoding = "GBK"
    chapter_soup = BeautifulSoup(chapter_page.text, 'html.parser')

    sentences = chapter_soup.findAll('div', attrs={'class':'txtnav'})[0].text
    sentences = sentences.replace('\u2003', ' ').replace('  ', '').replace('\r', '').split('\n')
    sentences = list(filter(None, sentences))

    driver.get(google_translate_url)
    sleep(2)

    actions = ActionChains(driver)
    for sentence in sentences:
        pyperclip.copy(sentence)
        actions.key_down(Keys.CONTROL).perform()
        actions.send_keys('v').perform()
        actions.key_up(Keys.CONTROL).perform()

        # actions.send_keys(sentence).perform()
        actions.send_keys(Keys.ENTER).perform()
    sleep(5)

    actions = ActionChains(driver)
    for _ in range(6):
        actions.send_keys(Keys.TAB).perform()
        sleep(0.2)
    actions.send_keys(Keys.SPACE).perform()

    with open(f'Chapters/{link[0]}.txt', 'w') as file:
        file.write(pyperclip.paste())

    set_translation(link[0])
