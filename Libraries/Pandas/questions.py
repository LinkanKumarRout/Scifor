#1. What is pandas and what are its main feature ?
'''
Pandas is an open-source data manipulation and analysis library for the Python programming language. It provides data structures and functions needed to efficiently manipulate large datasets. The library is built on top of NumPy and is widely used in data science, machine learning, and scientific computing.
- it has two data structure named Series and DataFrame
- it has lot of builtin methods to handle large datasets
'''
#2. Explain the difference between series and dataframe ?
'''
Series: A one-dimensional labeled array capable of holding any data type.

DataFrame: A two-dimensional labeled data structure with columns of potentially different types. It can be thought of as a dictionary of Series objects or a table of data similar to an SQL table or an Excel spreadsheet.
'''
#3. How do you create a DataFrame in pandas ?
'''
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)
'''