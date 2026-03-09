#A. Apply Clustering Algorithm (K-Means)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

documents = [
"Machine learning is the study of computer algorithms that improve through experience",
"Deep learning is a subset of machine learning",
"Natural language processing is a field of artificial intelligence",
"Computer vision is a field of study that enables computers to interpret the visual world",
"Reinforcement learning is a machine learning algorithm",
"Information retrieval is the process of obtaining information from a collection",
"Text mining is the process of deriving high quality information from text",
"Data clustering is the task of dividing a set of objects into groups",
"Hierarchical clustering builds a tree of clusters",
"K-means clustering is a method of vector quantization"
]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

k = 3

model = KMeans(n_clusters=k, random_state=42)
model.fit(X)

labels = model.labels_

for i, doc in enumerate(documents):
    print("Document", i+1, "Cluster:", labels[i])

#B. Evaluate Binary Classification Metrics

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import average_precision_score

y_true = [0,1,1,0,1]
y_scores = [0.1,0.8,0.6,0.3,0.9]

y_pred = [1 if score > 0.5 else 0 for score in y_scores]

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
avg_precision = average_precision_score(y_true, y_scores)

print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Average Precision:", avg_precision)
