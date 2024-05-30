import pandas as pd # importing pandas module

data = {
    'Linkan':[4,7,9,5],
    'Ram':[9,8,9,7]
}
# Series: A one-dimensional labeled array capable of holding any data type.
se = pd.Series(data) # creating a series from our data
print(se)

# DataFrame: A two-dimensional labeled data structure with columns of potentially different types.
df = pd.DataFrame(data)
print(df)

# also we can change the index as we want like this
index = ['a','b','c','d']
df = pd.DataFrame(data, index=index)
print(df)

# Reading and Writing Data

data = pd.read_csv('/content/netflix_titles.csv') # reading a csv file
print(data.info()) # getting information from a file

data.to_csv('new_netflix.csv', index=False) # writing data to a file

# Data Manipulation

# data.head(n) display top n rows
data.head(5)

# df.tail() display last n rows
data.tail(5)

data.describe() # give a brief description about data

# df.shape() gives current shape of your dataframe
print(data.shape) # gives shape (row & columns)
print(data.columns) # shows all columns in your dataframe
print(data.index) # gives index of your dataframe

# df.loc[], df.iloc[]: Access rows and columns by label or integer-based indexing.
data.loc[4000]
data.iloc[5000]

# df.rename(): Rename columns in a DataFrame.
data.rename(columns={'title':'name'}, inplace=True)
print(data.loc[1])

# df.groupby(): Group data in a DataFrame based on specified criteria.
data.groupby('country').count()

# Data Cleaning

# df.isnull() check for null value in your data
data = pd.read_csv('/content/new_netflix.csv')
data.isnull().sum()

# fill all null value with 0
data.fillna(0, inplace=True)
print(data)

data.dropna(inplace=True) # drop rows with missing values(null)
print(data)

# df.query() - separate data based on a query
data1 = data.query('release_year > 2019')
print(data1)

print(data['title']) # print only title from a dataframe

#------------------------------------------------------------
import pandas as pd

# Create a sample DataFrame with missing values
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# Fill missing values in column 'A' with the mean of column 'A'
mean_A = df['A'].mean()
df['A'].fillna(mean_A, inplace=True)

# Fill missing values in column 'B' with the median of column 'B'
median_B = df['B'].median()
df['B'].fillna(median_B, inplace=True)

print(df)

# Home Work to find out all the movies which are released in india
data = dict(data)
index = []
movies = dict(data['type'])
co = dict(data['country'])
for i in co:
  if co[i] == 'India':
    for j in movies:
      if j == i:
        index.append(i)
for i in index:
  print(data['title'][i])