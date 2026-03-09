#1A. Apply the PageRank Algorithm and Analyze Results
pages = ["A","B","C","D","E"]

links = {
"A":["B","C","D"],
"B":["C","E"],
"C":["A","D"],
"D":[],
"E":[]
}

d = 0.85
N = len(pages)

pagerank = {page:1/N for page in pages}

for i in range(10):
    new_rank = {}
    
    for page in pages:
        rank_sum = 0
        
        for p in pages:
            if page in links[p]:
                rank_sum += pagerank[p] / len(links[p])
        
        new_rank[page] = (1-d)/N + d * rank_sum
    
    pagerank = new_rank

for page,rank in pagerank.items():
    print(page,":",round(rank,3))

#1B Text Summarization

text = """
Information retrieval is the process of obtaining relevant information from large collections of data.
Search engines use information retrieval techniques to find documents.
These systems help users find useful information quickly.
Information retrieval is used in web search and digital libraries.
"""

sentences = text.split(".")

word_freq = {}

for sentence in sentences:
    for word in sentence.lower().split():
        word_freq[word] = word_freq.get(word,0) + 1

sentence_score = {}

for sentence in sentences:
    for word in sentence.lower().split():
        if word in word_freq:
            sentence_score[sentence] = sentence_score.get(sentence,0) + word_freq[word]

summary = sorted(sentence_score,key=sentence_score.get,reverse=True)[:2]

print("Summary:\n")

for s in summary:
    print(s.strip())
