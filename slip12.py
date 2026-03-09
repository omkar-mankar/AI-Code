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

pagerank = {}

for page in pages:
    pagerank[page] = 1/N

for i in range(10):

    new_rank = {}

    for page in pages:

        rank_sum = 0

        for p in pages:

            if page in links[p] and len(links[p]) > 0:
                rank_sum += pagerank[p] / len(links[p])

        new_rank[page] = (1-d)/N + d * rank_sum

    pagerank = new_rank

print("PageRank Values")

for page in pagerank:
    print(page,"=",pagerank[page])

#B. Program to Calculate Precision, Recall and F-Measure
tp = 20
fp = 10
fn = 30

precision = tp / (tp + fp)

recall = tp / (tp + fn)

f_score = 2 * (precision * recall) / (precision + recall)

print("True Positive =", tp)
print("False Positive =", fp)
print("False Negative =", fn)

print("Precision =", precision)
print("Recall =", recall)
print("F-Measure =", f_score)
