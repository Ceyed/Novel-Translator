from time import sleep

import pyperclip
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from lxml import etree
from requests.adapters import HTTPAdapter
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm import tqdm
from urllib3.util.retry import Retry
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver_manager

from Model.db import create_chapter_names, set_translation

translator = Translator()


url = 'https://www.69shu.com/46488/'
xpath = """//*[(@id = "catalog")]//a"""
chapter_xpath = """//*[contains(concat( " ", @class, " " ), concat( " ", "txtnav", " " ))]"""

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

page = session.get(url)
page.raise_for_status()
page.encoding = "GBK"
soup = BeautifulSoup(page.text, 'html.parser')
dom = etree.HTML(str(soup))
links = dom.xpath(xpath)
print('Translating chapter titles and extracting their links')
new_links = []
for index in tqdm(range(0, round(len(links) / 80))):
    new_links.append((translator.translate(links[index].text).text, links[index].get('href')))
links = new_links

create_chapter_names([(link[0], ) for link in links])

google_translate_url = "https://translate.google.com/?hl=en&tab=TT&sl=auto&tl=en&op=translate"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for index in tqdm(range(len(links))):
    chapter_page = requests.get(links[index][1])
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
        ActionChains(driver).send_keys(sentence).perform()
        ActionChains(driver).send_keys(Keys.ENTER).perform()
    sleep(5)

    for _ in range(6):
        actions = actions.send_keys(Keys.TAB)
    actions = actions.send_keys(Keys.SPACE)
    actions.perform()

    with open(f'Chapters/{links[index][0]}.txt', 'w') as file:
        file.write(pyperclip.paste())
    
    set_translation(links[index][0])

    # break
