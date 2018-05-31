import lxml.etree as ET


def parse_links(path):
    links_node = ET.parse(path).getroot()
    return list(map(lambda link_node: link_node.text, links_node))


def write_words(words_dic, output_file):
    words_node = ET.Element('words')
    for word in words_dic:
        word_node = ET.SubElement(words_node, 'word')
        text_node = ET.SubElement(word_node, 'text')
        count_node = ET.SubElement(word_node, 'count')
        text_node.text = word
        count_node.text = str(words_dic[word])
    ET.ElementTree(words_node).write(output_file, 'utf-8')
