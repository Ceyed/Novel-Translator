from Controller.scroll_to_bottom import scroll_to_bottom
from Controller.setup_driver import setup_driver
from Controller.wait_for_page_to_load import wait_for_page_to_load
from Controller.google_translate_link import google_translate_link
from Controller.get_chapter_links import get_chapter_links



if __name__ == "__main__":
    url = google_translate_link("https://www.69shu.com/46488/")
    driver = setup_driver(url)
    wait_for_page_to_load(driver)
    scroll_to_bottom(driver)  
    links = get_chapter_links(driver)

    links.sort()
    for link in links:
        print(link)
