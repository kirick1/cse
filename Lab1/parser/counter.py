import re
import Lab1.parser.spelling as spelling
import functools


def count_words(string):
    def count_write(count_dic, word):
        if count_dic.get(word) is None:
            count_dic[word] = 1
        else:
            count_dic[word] += 1
        return count_dic
    words = re.sub('[^\w]', ' ', string).split()
    hs = spelling.create_hs()
    formatted = list(map(lambda word: spelling.base_form(word.lower(), hs), words))
    return functools.reduce(count_write, formatted, {})
