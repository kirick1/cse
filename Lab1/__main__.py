import Lab1.parser.words as xml
import Lab1.parser.request as request
import Lab1.parser.counter as counter
import os

if __name__ == '__main__':
    links = xml.parse_links(os.path.join(os.getcwd(), 'Lab1', 'links.file_reader'))
    print('Parsed links: ' + str(links))
    text = request.read_links(links)
    print('Requested test: ' + text)
    words = counter.count_words(text)
    print('Counted words dictionary: ' + str(words))
    xml.write_words(words, os.path.join(os.getcwd(), 'Lab1', 'counted.file_reader'))
    print('printed to "counted.file_reader"')
