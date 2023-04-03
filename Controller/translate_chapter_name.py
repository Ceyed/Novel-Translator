from googletrans import Translator
from tqdm import tqdm

from Utils.log import single_log



def translate_chapter_names(links):
    single_log('Translating chapters names to English')

    translator = Translator()
    new_links = []
    for index in tqdm(range(0, len(links))):
        new_links.append((translator.translate(links[index].text).text, links[index].get('href')))

    return new_links
