#A. Program to Calculate Precision, Recall and F-Measure
tp = 60
fp = 30
fn = 20

precision = tp / (tp + fp)

recall = tp / (tp + fn)

f_measure = 2 * (precision * recall) / (precision + recall)

print("True Positive:", tp)
print("False Positive:", fp)
print("False Negative:", fn)

print("Precision =", precision)
print("Recall =", recall)
print("F-Measure =", f_measure)

#B. Use an Evaluation Toolkit to Measure Average Precision and Other Metrics
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import average_precision_score

y_true = [1, 1, 1, 1, 0, 0, 0, 0]

y_pred = [1, 1, 0, 1, 0, 1, 0, 0]

precision = precision_score(y_true, y_pred)

recall = recall_score(y_true, y_pred)

f1 = f1_score(y_true, y_pred)

avg_precision = average_precision_score(y_true, y_pred)

print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Average Precision:", avg_precision)
