#A. Implement Vector Space Model with TF-IDF Weighting
import math
from collections import Counter

documents = [
"The sun is the star at the center of the solar system",
"She wore a beautiful dress to the party last night",
"The book on the table caught my attention immediately"
]

query = "solar system"

docs = [doc.lower().split() for doc in documents]
query_words = query.lower().split()

vocab = set()

for doc in docs:
    vocab.update(doc)

vocab = list(vocab)

N = len(docs)

idf = {}

for word in vocab:
    df = sum(1 for doc in docs if word in doc)
    idf[word] = math.log(N/(df+1))

tfidf_docs = []

for doc in docs:

    tf = Counter(doc)

    tfidf = {}

    for word in vocab:
        tfidf[word] = (tf[word]/len(doc)) * idf[word]

    tfidf_docs.append(tfidf)

print("TF-IDF representation created for all documents.")

#B. Implement a Clustering Algorithm (K-Means) Objective
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

documents = [
"The sun is the star at the center of the solar system",
"She wore a beautiful dress to the party last night",
"The book on the table caught my attention immediately"
]

vectorizer = TfidfVectorizer(stop_words='english')

X = vectorizer.fit_transform(documents)

k = 2

model = KMeans(n_clusters=k, random_state=42)

model.fit(X)

labels = model.labels_

for i, doc in enumerate(documents):
    print("Document", i+1, "Cluster:", labels[i])
