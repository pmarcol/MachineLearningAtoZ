# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)
results2 = []
for i in range(len(results)):
    row = {
            'items': list(results[i].items),
            'base': list(results[i].ordered_statistics[0].items_base),
            'add': list(results[i].ordered_statistics[0].items_add),
            'support': results[i].support,
            'confidence': results[i].ordered_statistics[0].confidence,
            'lift': results[i].ordered_statistics[0].lift
            }
    results2.append(row)