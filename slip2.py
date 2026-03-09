#A. Implement an Inverted Index Construction Algorithm
documents = {
"doc1": "The quick brown fox jumped over the lazy dog",
"doc2": "The lazy dog slept in the sun"
}

inverted_index = {}

for doc_id, text in documents.items():

    words = text.lower().split()

    for word in words:

        if word not in inverted_index:
            inverted_index[word] = set()

        inverted_index[word].add(doc_id)

print("Inverted Index:\n")

for term, docs in inverted_index.items():
    print(term, ":", docs)

query = ["lazy","sun"]

result = inverted_index[query[0]]

for term in query[1:]:
    result = result.intersection(inverted_index.get(term,set()))

print("Documents containing 'lazy sun':", result)


#B. Program to Calculate Precision, Recall and F-Measure

tp = 60
fp = 30
fn = 20

precision = tp / (tp + fp)

recall = tp / (tp + fn)

f_measure = 2 * (precision * recall) / (precision + recall)

print("True Positive =", tp)
print("False Positive =", fp)
print("False Negative =", fn)

print("Precision =", precision)
print("Recall =", recall)
print("F-measure =", f_measure)
