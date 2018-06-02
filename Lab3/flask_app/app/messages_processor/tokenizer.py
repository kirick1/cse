import nltk
from nltk import word_tokenize, SnowballStemmer
from nltk.corpus import stopwords

nltk.download('stopwords')

LANGUAGE = 'russian'


def create_stemmer():
    return SnowballStemmer(LANGUAGE)


def create_stop_words():
    return stopwords.words(LANGUAGE)


def process_messages(messages, stemmer, stop_words):
    print('Processing messages ...')
    processed_messages = []
    for message in messages:
        tokens = word_tokenize(message.lower())
        processed_message = [word for word in tokens if word.isalpha() and word not in stop_words]
        processed_message = [stemmer.stem(word) for word in processed_message]
        processed_messages.append(processed_message)
    return processed_messages
