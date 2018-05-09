import urllib.request as request


def read_links(links):
    return ' '.join(list(map(lambda link: request.urlopen(link).read().decode('utf-8'), links)))
