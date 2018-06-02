from flask_app.app.messages_processor.clusters import get_clusters
from flask_app.app.messages_processor.tokenizer import create_stemmer, create_stop_words, process_messages
from flask_app.app.messages_processor.vectorizer import create_vectorizer, vectorize


def get_cloud(users):
    stemmer = create_stemmer()
    stop_words = create_stop_words()
    vectorizer = create_vectorizer()

    processed_messages = []

    for user in users:
        messages = user['messages']
        processed_messages.extend(process_messages(messages, stemmer, stop_words))

    vectors = vectorize(processed_messages, vectorizer)

    clusters = get_clusters(vectors, vectorizer)
    return clusters
