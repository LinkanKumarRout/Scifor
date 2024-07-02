#1. What is scikit-learn and what is its main purpose.
'''
Scikit-learn is a free software machine learning library for the Python programming language. It features various
classification, regression and clustering algorithms including support vector machines, random forests, gradient
boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical
and scientific libraries NumPy and SciPy.
'''
#2. How do you install scikitlearn.
'''
To install scikitlearn we can use pip and the command is:
pip install scikit-learn
'''
#3. What are some common machine learning task that can be performed using scikitlearn.
'''
Some common machine learning task that can be performed using scikitlearn are:
1. Classification
2. Regression
3. Clustering
4. Dimensionality Reduction
5. Model Selection
6. Preprocessing
7. Feature Extraction
8. Feature Selection
9. Model Evaluation
10. Model Optimization
'''
#4. How do you create a machine learning model in scikit-learn.
'''
To create a machine learning model in scikit-learn, we first need to import the necessary libraries
and modules. Once we have imported the required libraries, we can create a machine learning model
by using the scikit-learn API. The API provides a set of functions and classes that can
be used to create, train, and evaluate machine learning models.

Example:
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

# Load the diabetes dataset
diabetes = load_diabetes()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes
.target, test_size=0.2, random_state=42)

# Create a linear regression model
regressor = LinearRegression()

# Train the model on the training data
regressor.fit(X_train, y_train)

# Evaluate the model on the testing data
y_pred = regressor.predict(X_test)
print("Mean squared error:", np.mean((y_pred - y_test)**2))
'''
#5. What is the purpose of the fit, predict and score methods in scikit-learn.
'''
The fit method is used to train the model on the training data. The predict method is used to
make predictions on new data. The score method is used to evaluate the performance of the
model on the testing data.
'''
