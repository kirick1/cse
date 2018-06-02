from sklearn.cluster import KMeans


def get_clusters(vectors, vectorizer):
    print('Getting clusters ...')
    clusters = 7
    model = KMeans(n_clusters=clusters)
    model.fit(vectors)
    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(clusters):
        print("Cluster %d:\n" % i)
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind])
        print('\n')