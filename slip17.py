#A. Apply PageRank Algorithm and Analyze Results
pages = ["A","B","C","D","E"]

links = {
"A":["B","C","D"],
"B":["C","E"],
"C":["A","D"],
"D":[],
"E":[]
}

N = len(pages)
d = 0.85

pagerank = {page:1/N for page in pages}

for i in range(10):

    new_rank = {}

    for page in pages:

        rank_sum = 0

        for p in pages:

            if page in links[p] and len(links[p])>0:
                rank_sum += pagerank[p] / len(links[p])

        new_rank[page] = (1-d)/N + d*rank_sum

    pagerank = new_rank

print("PageRank Values")

#B. Implement Boolean Retrieval Model
documents = {
"doc1":"The university exam is scheduled next week",
"doc2":"The university of mumbai has declared the result"
}

inverted_index = {}

for doc_id,text in documents.items():

    words = text.lower().split()

    for word in words:

        if word not in inverted_index:
            inverted_index[word] = set()

        inverted_index[word].add(doc_id)

query_terms = ["university","mumbai"]

result = inverted_index[query_terms[0]]

for term in query_terms[1:]:
    result = result.intersection(inverted_index.get(term,set()))

print("Documents satisfying query:", result)

for page in pagerank:
    print(page,"=",pagerank[page])
