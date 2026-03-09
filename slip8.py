#A. Implement the Vector Space Model with TF-IDF Weighting
import math
from collections import Counter

documents = [
"Document about python programming language and data analysis",
"Document discussing machine learning algorithms and programming techniques",
"Overview of natural language processing and its applications"
]

query = "python programming"

def preprocess(text):
    return text.lower().split()

docs_tokens = [preprocess(doc) for doc in documents]
query_tokens = preprocess(query)

vocab = set()
for doc in docs_tokens:
    vocab.update(doc)
vocab = list(vocab)

def compute_tf(tokens):
    tf = {}
    count = Counter(tokens)
    for word in vocab:
        tf[word] = count[word] / len(tokens)
    return tf

tf_docs = [compute_tf(doc) for doc in docs_tokens]

def compute_idf():
    idf = {}
    N = len(docs_tokens)
    for word in vocab:
        df = sum(1 for doc in docs_tokens if word in doc)
        idf[word] = math.log(N / (df + 1))
    return idf

idf = compute_idf()

tfidf_docs = []
for tf in tf_docs:
    tfidf = {}
    for word in vocab:
        tfidf[word] = tf[word] * idf[word]
    tfidf_docs.append(tfidf)

query_tf = compute_tf(query_tokens)

query_tfidf = {}
for word in vocab:
    query_tfidf[word] = query_tf[word] * idf[word]

#B. Calculate Cosine Similarity
def cosine_similarity(vec1, vec2):
    dot = sum(vec1[word] * vec2[word] for word in vocab)

    mag1 = math.sqrt(sum(vec1[word]**2 for word in vocab))
    mag2 = math.sqrt(sum(vec2[word]**2 for word in vocab))

    if mag1 == 0 or mag2 == 0:
        return 0

    return dot / (mag1 * mag2)

for i, doc in enumerate(tfidf_docs):
    score = cosine_similarity(query_tfidf, doc)
    print("Similarity between Query and Document", i+1, "=", score)
