import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager

from Controller.chapter_links import chapters_links
from Controller.translate_chapter import translate_chapter
from Controller.translate_chapter_name import translate_chapter_names
from Model.db import create_chapter_names_in_db, set_translation, load_links_db, clear_table
from Utils.log import single_log, log, done_log, tqdm_desc



def main(url):
    starting_chapter = 0

    log('Loading saved data')
    old_links = load_links_db()
    done_log()
    links = chapters_links(url)

    if len(links) != len(old_links):
        single_log('Loaded data is not complete. Clearing database and getting links again')
        clear_table()
        links = translate_chapter_names(links)
        create_chapter_names_in_db([(link[0], link[1]) for link in links])
    else:
        single_log('Loaded data is good. Finding how many links has been translated before')
        for index, link in enumerate(old_links):
            if link[2] == 0:
                starting_chapter = index
                break
        links = old_links

    # * Check if folder exists
    if not os.path.exists('./Chapters'):
        os.makedirs('./Chapters')

    # * Start translating chapters
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    for index in tqdm(range(0, len(links)), desc=tqdm_desc(f'Translating Chapters (Will start from {links[starting_chapter][0]})')):
        if index < starting_chapter:
            continue
        translate_chapter(driver, links[index])


if __name__ == "__main__":
    url = 'https://www.69shu.com/46488/'
    main(url)
