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


def get_occurrences_key(item):
    return item['occurrences']


def calculate_word_occurrences(words_array):
    word_occurrences_array = []
    if len(words_array) != 0:
        word_occurrences_array.append({'word': words_array[0], 'occurrences': 0})
        for word in words_array:
            added = False
            for woc in word_occurrences_array:
                if word == woc['word']:
                    woc['occurrences'] += 1
                    added = True
                    break
            if not added:
                word_occurrences_array.append({'word': word, 'occurrences': 1})
        word_occurrences_array.sort(key=get_occurrences_key, reverse=True)
    return word_occurrences_array


def get_cloud(users, clusters_number=7, cluster_size=10):
    clusters = calculate_clusters(users, clusters_number, cluster_size)
    clusters_words_array = []
    for cluster in clusters:
        clusters_words_array.extend(cluster['values'])
    tag_cloud = calculate_word_occurrences(clusters_words_array)
    return tag_cloud
