#A. Implement an Inverted Index Construction Algorithm
documents = {
"doc1": "our class meeting starts soon",
"doc2": "my class starts at 6"
}

inverted_index = {}

for doc_id, text in documents.items():

    words = text.lower().split()

    for word in words:

        if word not in inverted_index:
            inverted_index[word] = []

        inverted_index[word].append(doc_id)

print("Inverted Index\n")

for term in inverted_index:
    print(term, ":", inverted_index[term])

#B. Build a Simple Document Retrieval System
documents = {
"doc1": "our class meeting starts soon",
"doc2": "my class starts at 6"
}

inverted_index = {}

for doc_id, text in documents.items():

    words = text.lower().split()

    for word in words:

        if word not in inverted_index:
            inverted_index[word] = []

        inverted_index[word].append(doc_id)

query = "class meeting"

query_words = query.lower().split()

result = set()

for word in query_words:
    if word in inverted_index:
        result.update(inverted_index[word])

print("Documents containing query terms:")
print(result)
