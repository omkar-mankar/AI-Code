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
print("F-Measure =", f_measure)
