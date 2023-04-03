import requests
from bs4 import BeautifulSoup
from lxml import etree
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from Utils.log import log, done_log



def chapters_links(url):
    log('Getting all chapters links')

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

    done_log()
    return links
