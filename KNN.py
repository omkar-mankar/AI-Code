import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("Iris.csv")

x = df.drop(['ID', 'Target'], axis=1).values
y = df['Target'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

k = 3

clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

classification_accuracy = accuracy_score(y_test, y_pred)

print("Classification accuracy: ", classification_accuracy)
