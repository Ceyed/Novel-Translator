from googletrans import Translator
from tqdm import tqdm

from Utils.log import tqdm_desc



def translate_chapter_names(links):
    translator = Translator()
    new_links = []
    for index in tqdm(range(0, len(links)), desc=tqdm_desc("Translating chapters names to English: ")):
        new_links.append((translator.translate(links[index].text).text, links[index].get('href')))

    return new_links
