#A. Build a Question Answering System
corpus = [
"India has the second-largest population in the world",
"It is surrounded by oceans from three sides which are Bay of Bengal in the east the Arabian Sea in the west and Indian oceans in the south",
"Tiger is the national animal of India",
"Peacock is the national bird of India",
"Mango is the national fruit of India"
]

query = "Which is the national bird of India"

query_words = query.lower().split()

best_sentence = ""
best_score = 0

for sentence in corpus:

    words = sentence.lower().split()
    score = 0

    for word in query_words:
        if word in words:
            score += 1

    if score > best_score:
        best_score = score
        best_sentence = sentence

print("Query:", query)
print("Answer:", best_sentence)

#B. Create a Text Summarization System
from collections import Counter

text = """Natural language processing NLP is a field of computer science artificial intelligence and computational linguistics concerned with interactions between computers and human languages. NLP is related to human computer interaction. Many challenges in NLP involve natural language understanding natural language generation and machine learning. Text summarization is the process of distilling important information from text."""

sentences = text.split(".")

words = text.lower().split()

freq = Counter(words)

sentence_scores = {}

for sentence in sentences:

    score = 0
    for word in sentence.lower().split():
        score += freq[word]

    sentence_scores[sentence] = score

summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

print("Summary:\n")

for s in summary:
    print(s.strip())
