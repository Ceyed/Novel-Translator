from googletrans import Translator
from tqdm import tqdm



def translate_chapter_names(links):
    translator = Translator()
    new_links = []
    for index in tqdm(range(0, len(links))):
        new_links.append((translator.translate(links[index].text).text, links[index].get('href')))
    return new_links
