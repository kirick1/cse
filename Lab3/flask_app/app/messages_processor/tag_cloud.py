from clusters import get_clusters
from tokenizer import create_stemmer, create_stop_words, process_messages
from vectorizer import create_vectorizer, vectorize


def get_cloud(users, clusters_number=7, cluster_size=10):
    stemmer = create_stemmer()
    stop_words = create_stop_words()
    vectorizer = create_vectorizer()
    processed_messages = []
    for user in users:
        processed_messages.extend(process_messages(user['messages'], stemmer, stop_words))
    vectors = vectorize(processed_messages, vectorizer)
    return get_clusters(vectors, vectorizer, clusters_number, cluster_size)
