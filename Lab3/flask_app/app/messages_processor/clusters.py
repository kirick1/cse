from sklearn.cluster import KMeans


def get_clusters(vectors, vectorizer, clusters_number, cluster_size):
    print('Getting clusters ...')
    model = KMeans(n_clusters=clusters_number)
    model.fit(vectors)
    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    clusters = []
    for i in range(clusters_number):
        print("Cluster %d:\n" % i)
        cluster = {'number': i, 'values': []}
        for ind in order_centroids[i, :cluster_size]:
            term = terms[ind]
            cluster['values'].append(term)
            print(' %s' % term)
        clusters.append(cluster)
        print('\n')
    return clusters
