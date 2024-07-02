'''
Problem Statement:
Predict a student's final exam score based on the number of hours they study
'''
"""
We can say scikit-learn is a combination of numpy, pandas and scipy
"""
'''It has a number of built-in models. We can choose a model based on our data'''
'''
If there is growth in your data then you can choose linear regression
'''
# step-1 import statements
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# step-2 import data
data =  {
    'Hours_study':[2,3,4,5,6,7,8,9,10],
    'Exam_score':[50,60,70,75,80,85,90,92,95]
}

# step-3
df = pd.DataFrame(data)
# print(df)

# step-4 extract columns(feature extraction)

X = df[['Hours_study']]
y = df[['Exam_score']]

# step-5 train & test
'''
Generally we train 80% data and test 20% data, but you can change as your choice. but it will reduce accuracy beacause your train should be more than your test.
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
'''
With random_state=42: The split is deterministic, meaning you will always get the same training and testing sets every time you run the code. This is useful when you want to share your code with others and ensure they get the same results, or when you need to debug your code and want consistent splits.

Without specifying random_state: The split is random and will likely be different every time you run the code. This can be problematic if you are trying to reproduce results or compare the performance of different models under the same conditions.
'''
# print("Training data:", X_train, y_train)
# print("Testing data:", X_test, y_test)

# step no-6
model = LinearRegression()

# step no-7
'''
Here we create an instance of our model to call it
'''
model.fit(X_train,y_train)

# Let's work on user input data
user_input = float(input("Enter number of hours you study: "))

predicted_score = model.predict(np.array([[user_input]]))

# printing the output
print(f"Predicted exam score for {user_input} hour study is {predicted_score[0][0]:.2f}")
