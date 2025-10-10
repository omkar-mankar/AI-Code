from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

dataset = [['milk','bread','nuts'],
           ['milk', 'bread'],
           ['milk', 'eggs', 'nuts'],
           ['milk', 'bread', 'eggs'],
           ['bread', 'nuts']]

df = pd.DataFrame(dataset)

df_encoded = pd.get_dummies(df, prefix='', prefix_sep='')

frequent_itemsets = apriori(df_encoded, min_support=0.4, use_colnames=True)

print("Frequent Itemsets:\n", frequent_itemsets)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

print("\nAssociation Rules:\n", rules)
