import Lab1.test.counter_test as counter_test
import Lab1.test.request_test as request_test
import Lab1.test.spelling_test as spelling_test
import Lab1.test.xml_test as xml_test

if __name__ == '__main__':
    print('Tests for package: "file_reader" started ...')
    print(counter_test.count_words_test())
    print(request_test.read_links_test())
    print(spelling_test.create_hs_test())
    print(spelling_test.base_form_test())
    print(xml_test.parse_links_test())
    print(xml_test.write_words_test())
    print('Tests for package: "file_reader" successfully passed')
