#PROJECT

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('F:/ML IN PYTHON/PROJECT/carbon.csv')
#pd.set_option('display.max_rows',100)
#pd.set_option('display.max_columns',200)

dataset=dataset.drop(["DATE_TIME", "COKE_RATE", "COAL_RATE" ], axis=1)


