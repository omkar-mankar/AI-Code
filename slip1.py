#A. Implement an Inverted Index Construction Algorithm
documents = {
"doc1": "The computer science students are appearing for practical examination",
"doc2": "computer science practical examination will start tomorrow"
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

query = ["computer", "science"]

result = inverted_index[query[0]]

for term in query[1:]:
    result = result.intersection(inverted_index.get(term, set()))

print("Documents containing 'computer science':", result)

#B. Build a Question Answering System (Information Extraction)
knowledge_base = [
"Tiger is the national animal of India",
"Peacock is the national bird of India",
"Mango is the national fruit of India"
]

query = "national bird of India"

query_words = query.lower().split()

best_answer = ""
best_score = 0

for sentence in knowledge_base:

    words = sentence.lower().split()
    score = 0

    for word in query_words:
        if word in words:
            score += 1

    if score > best_score:
        best_score = score
        best_answer = sentence

print("Answer:", best_answer)
