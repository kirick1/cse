import hunspell
import os

dictionary_paths = ['Lab1/parser/dictionaries/Ukrainian_uk_UA.dic', 'Lab1/parser/dictionaries/Ukrainian_uk_UA.aff']
print(list(map(lambda path: os.path.join(os.getcwd(), path), dictionary_paths)))


def create_hs():
    return hunspell.HunSpell(*list(map(lambda path: os.path.join(os.getcwd(), path), dictionary_paths)))


def base_form(word, hs):
    bytes_array = hs.stem(word)
    forms = list(map(lambda bytes_word: bytes_word.decode('utf-8'), bytes_array))
    return word if len(forms) == 0 else forms[0]
