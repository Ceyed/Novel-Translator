from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager

from Controller.chapter_links import chapters_links
from Controller.translate_chapter import translate_chapter
from Controller.translate_chapter_name import translate_chapter_names
from Model.db import create_chapter_names_in_db, set_translation



def main():
    url = 'https://www.69shu.com/46488/'
    links = chapters_links(url)
    links = translate_chapter_names(links)
    create_chapter_names_in_db([(link[0], ) for link in links])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    for index in tqdm(range(0, len(links))):
        translate_chapter(driver, links[index])


if __name__ == "__main__":
    main()
