# # Eclat Model

import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "apyori"])

# ## Importing the Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ## Importing the Dataset

dataset = pd.read_csv('Market_Basket_Optimisation.csv',header = None)
transactions =[]
for i in range(0,7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

# ## Training the Eclat Model

from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003,min_confidence = 0.2,min_lift = 3 ,min_length = 2,max_length=2)

# ## Visualising the Results

results= list(rules)
print(results)

# ## Putting the results into a organised Dataframe

def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    return list(zip(lhs, rhs, supports))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support'])

# ## Displaying the results by sorting in descending order

print(resultsinDataFrame.nlargest(n = 10, columns = 'Support'))
