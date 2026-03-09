#A. Classification using Naïve Bayes (20 Newsgroups Dataset)
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

categories = ['rec.autos', 'rec.sport.hockey']

data = fetch_20newsgroups(subset='all', categories=categories)

X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42
)

vectorizer = TfidfVectorizer(stop_words='english')

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = MultinomialNB()

model.fit(X_train_tfidf, y_train)

predictions = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, predictions)

print("Naive Bayes Classification Accuracy:", accuracy)

#B. Classification using SVM (Support Vector Machine)
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

categories = [
'alt.atheism',
'soc.religion.christian',
'comp.graphics',
'sci.med'
]

data = fetch_20newsgroups(subset='all', categories=categories)

X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42
)

vectorizer = TfidfVectorizer(stop_words='english')

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = SVC(kernel='linear')

model.fit(X_train_tfidf, y_train)

predictions = model.predict(X_test_tfidf)

print("Classification Report:\n")
print(classification_report(y_test, predictions))
