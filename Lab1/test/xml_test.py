import Lab1.parser.counter as counter
import Lab1.parser.xml as xml
import Lab1.parser.request as request
import os


def parse_links_test():
    parsed_links = xml.parse_links(os.path.join(os.getcwd(), 'Lab1', 'test', 'links.file_reader'))
    expected_test_links = ['https://www.python.org/', 'https://nodejs.org', 'https://github.com/']
    assert len(parsed_links) == 3, 'Count of parsed links from file: "links.file_reader" is not equal with expected count'
    assert parsed_links[0] == expected_test_links[0], 'First link parsed from file is not equal with expected link'
    assert parsed_links[1] == expected_test_links[1], 'Second link parsed from file is not equal with expected link'
    assert parsed_links[2] == expected_test_links[2], 'Third link parsed from file is not equal with expected link'
    return '\tfile_reader.file_reader.parse_links test'


def write_words_test():
    initial_content = request.read_links(['https://raw.githubusercontent.com/kirick1/cse/master/Lab1/test/test.txt'])
    counted_initial_content = counter.count_words(initial_content)
    xml.write_words(counted_initial_content, os.path.join(os.getcwd(), 'Lab1', 'test', 'counted.file_reader'))
    return '\tfile_reader.file_reader.write_words test'
