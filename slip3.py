#3A. Develop a Spelling Correction Module Using Edit Distance
def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i

    for j in range(n+1):
        dp[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i-1][j] + 1,
                dp[i][j-1] + 1,
                dp[i-1][j-1] + cost
            )

    return dp[m][n]

s1 = "nature"
s2 = "creature"

print("Edit Distance:", edit_distance(s1,s2))

#3B. Implement Boolean Retrieval Model
documents = {
    "D1": "the cat chased the dog around the garden",
    "D2": "she was sitting in the garden last night",
    "D3": "i read the book the night before"
}

index = {}

for doc_id, text in documents.items():
    words = text.split()
    for word in words:
        if word not in index:
            index[word] = set()
        index[word].add(doc_id)

garden_docs = index.get("garden", set())
night_docs = index.get("night", set())

result = garden_docs.union(night_docs)

print("Documents matching query:", result)
