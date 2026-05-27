# # Apirori - Associate Rule Learning

# ## Importing the Dataset

import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "apyori"])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ## Importing the Dataset

dataset = pd.read_csv('Market_Basket_Optimisation.csv',header = None)
transactions = []
for i in range(0,7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

# ## Training the Apirori Model on dataset

from apyori import apriori
rules = apriori(transactions = transactions,min_support = 0.003, min_confidence = 0.2,min_lift = 3,max_length = 2,min_length = 2)

# ## Visualising The Results

# ### Displaying the test results coming directly from the output of apiriori function

results = list(rules)
print(results)

# ### Putting the results into a well organised pandas dataframe

def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

# ### Displaying the results in a sorted order

print(resultsinDataFrame.nlargest(n=10,columns = 'Lift'))
