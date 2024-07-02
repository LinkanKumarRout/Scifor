# Problem Statement
'''
In an e-commerce company, the management wants to predict wheather a customer will purchase a high value product based on their age, time spent on website, and wheather they have added items to the cart. The goal is to optimise marketing strategies by targeting potential customers more effectively, thereby increasing sales and revenue.
'''
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = np.array([[25, 30, 0], [30, 40, 1], [20, 35, 0], [35, 45, 1]])
y = np.array()
