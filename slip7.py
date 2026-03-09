#1A. Implement a Text Summarization Algorithm (Extractive)
text = """
Information retrieval is the process of obtaining relevant information from large collections of data.
Search engines use information retrieval techniques.
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

#1B. Implement Boolean Retrieval Model

docs = {
"D1":"bsc lectures start at 7",
"D2":"my lectures are over",
"D3":"today is a holiday"
}

query = "lectures"

result = []

for doc_id,text in docs.items():
    words = text.split()
    
    if query not in words:
        result.append(doc_id)

print("Documents matching query 'NOT lectures':")
print(result)
