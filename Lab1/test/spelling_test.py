import Lab1.parser.spelling as spelling


def create_hs_test():
    hs = spelling.create_hs()
    assert hs is not None, 'Creating hunspell spelling dictionary failed'
    return '\tfile_reader.spelling.create_hs test'


def base_form_test():
    hs = spelling.create_hs()
    test_word_base_form = spelling.base_form('пішов', hs)
    assert test_word_base_form == 'піти', 'For word: "пішов" returned test base form:"' + test_word_base_form + '" is not equal with expected base form for this word: "піти"'
    return '\tfile_reader.spelling.base_form test'
