#1A. Implement Cosine Similarity Between Query and Document
import math

query = "gold silver truck"
document = "shipment of gold damaged in a gold fire"

q_words = query.split()
d_words = document.split()

vocab = list(set(q_words + d_words))

q_vector = []
d_vector = []

for word in vocab:
    q_vector.append(q_words.count(word))
    d_vector.append(d_words.count(word))

dot_product = sum(q_vector[i]*d_vector[i] for i in range(len(vocab)))

q_mag = math.sqrt(sum(x*x for x in q_vector))
d_mag = math.sqrt(sum(x*x for x in d_vector))

similarity = dot_product/(q_mag*d_mag)

print("Cosine Similarity:", similarity)

#1B. Build a Question Answering System Using Information Extraction

data = {
"what is information retrieval": "Information retrieval is the process of obtaining relevant information from large datasets.",
"what is data mining": "Data mining is the process of discovering patterns in large data.",
"what is machine learning": "Machine learning is a method where computers learn from data."
}

question = input("Ask a question: ").lower()

if question in data:
    print("Answer:", data[question])
else:
    print("Answer not found in knowledge base")
