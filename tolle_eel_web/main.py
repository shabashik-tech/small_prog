from parser_book import random_citate
import eel


@eel.expose
def get_citate():
    citate = random_citate()
    return citate


eel.init('web')
eel.start('main.html', size=(400, 400))