from clusters import get_clusters
from tokenizer import create_stemmer, create_stop_words, process_messages
from vectorizer import create_vectorizer, vectorize


def calculate_clusters(users, clusters_number, cluster_size):
    stemmer = create_stemmer()
    stop_words = create_stop_words()
    vectorizer = create_vectorizer()
    processed_messages = []
    for user in users:
        processed_messages.extend(process_messages(user['messages'], stemmer, stop_words))
    vectors = vectorize(processed_messages, vectorizer)
    return get_clusters(vectors, vectorizer, clusters_number, cluster_size)


def calculate_word_occurrences(words_array):
    word_occurrences_array = []
    if len(words_array) != 0:
        value = {
            'word': words_array[0],
            'occurrences': 0
        }
        word_occurrences_array.append(value)
        for word in words_array:
            for wok in word_occurrences_array:
                if word == wok['word']:
                    wok['occurrences'] += 1
                else:
                    value['word'] = word
                    value['occurrences'] = 1
                    word_occurrences_array.append(value)
                    word = ''
    return word_occurrences_array


def get_cloud(users, clusters_number=7, cluster_size=10):
    clusters = calculate_clusters(users, clusters_number, cluster_size)
    clusters_words_array = []
    for cluster in clusters:
        for word in cluster['values']:
            clusters_words_array.append(word)
    '''
    tag_cloud = []
    for word in clusters_words_array:
        if len(tag_cloud) != 0:
            for tag in tag_cloud:
                if tag['word'] == word:
                    tag['occurrences'] += 1
                else:
                    tag_cloud_value = {
                        'word': word,
                        'occurrences': 1
                    }
                    tag_cloud.append(tag_cloud_value)
        else:
            tag_cloud_value = {
                'word': word,
                'occurrences': 1
            }
            tag_cloud.append(tag_cloud_value)
    return tag_cloud
    '''
    return clusters_words_array
