import Lab1.parser.request as request
import Lab1.parser.counter as counter


def count_words_test():
    requested_content = request.read_links(['https://raw.githubusercontent.com/kirick1/cse/master/Lab1/test/test.txt'])
    counted_requested_content = counter.count_words(requested_content)['heroku']
    assert counted_requested_content == 14, 'Count of words "heroku" in requested content is not equal with expected count of them'
    return '\tfile_reader.counter.count_words test'
