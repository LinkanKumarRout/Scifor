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
#4. What are some common methods for data explorationin Pandas ?
'''
Data exploration in Pandas involves various methods and functions to understand and analyze the structure and content of your data. Here are some common methods for data exploration in Pandas:

1. Loading Data
pd.read_csv(), pd.read_excel(), pd.read_json(), etc.: Load data into a DataFrame from different file formats.

2. Basic Data Inspection
df.head(n): Display the first n rows of the DataFrame.
df.tail(n): Display the last n rows of the DataFrame.
df.info(): Get a concise summary of the DataFrame, including the index dtype, column dtypes, non-null values, and memory usage.
df.shape: Get the dimensions of the DataFrame (number of rows and columns).
df.columns: List all column names.
df.index: Display the index (row labels) of the DataFrame.
df.describe(): Generate descriptive statistics for numerical columns, including count, mean, std, min, 25%, 50%, 75%, and max.
df.dtypes: Get the data types of each column.

3. Data Selection and Filtering
df['column_name'] or df.column_name: Select a single column.
df[['col1', 'col2']]: Select multiple columns.
df.loc[]: Access a group of rows and columns by labels.
df.iloc[]: Access a group of rows and columns by integer positions.
df[df['column_name'] > value]: Filter rows based on column values.

4. Data Cleaning and Preparation
df.isnull(): Detect missing values.
df.dropna(): Remove missing values.
df.fillna(value): Fill missing values with a specified value.
df.duplicated(): Detect duplicate rows.
df.drop_duplicates(): Remove duplicate rows.
df.rename(columns={'old_name': 'new_name'}): Rename columns.
df.apply(func): Apply a function along an axis of the DataFrame.

5. Aggregation and Grouping
df.groupby('column'): Group the DataFrame using a column.
df.groupby('column').agg({'col1': 'sum', 'col2': 'mean'}): Aggregate using one or more operations on grouped data.
df.pivot_table(values, index, columns, aggfunc): Create a spreadsheet-style pivot table.

6. Visualization
df.plot(kind='line'), df.plot(kind='bar'), df.plot(kind='hist'), etc.: Basic plotting using Pandas' built-in plotting capabilities (which leverage Matplotlib).

7. Correlation and Relationships
df.corr(): Compute pairwise correlation of columns.
pd.plotting.scatter_matrix(df): Generate a matrix of scatter plots for numerical columns.

8. Advanced Inspection
df.memory_usage(): Memory usage of each column.
df.value_counts(): Count unique values in a column.
df.sample(n): Return a random sample of n rows.
df.nunique(): Count unique values for each column.
'''
#5. How do you handle missing values in a DataFrame in Pandas ?
'''
Handling missing values in a Pandas DataFrame is a common task in data preprocessing. There are several strategies we can use, depending on the nature of your data and the specific requirements of our analysis. Here are some common methods:

1. Identifying Missing Values
Before handling missing values, we need to identify them:

df.isnull(): Returns a DataFrame of the same shape as df, with True where values are missing and False where they are not.
df.isnull().sum(): Returns the number of missing values in each column.
df.isnull().sum().sum(): Returns the total number of missing values in the entire DataFrame.

2. Removing Missing Values
df.dropna(): Removes rows with any missing values.
df.dropna(how='all'): Removes rows where all elements are missing.
df.dropna(subset=['col1', 'col2']): Removes rows where any of the specified columns have missing values.
df.dropna(axis=1): Removes columns with any missing values.

3. Filling Missing Values
df.fillna(value): Replaces missing values with a specified value.
df['col'].fillna(value): Replaces missing values in a specific column with a specified value.
df.fillna(method='ffill'): Forward fill, replaces missing values with the previous non-missing value.
df.fillna(method='bfill'): Backward fill, replaces missing values with the next non-missing value.
df.fillna(df.mean()): Fills missing values with the mean of each column.

4. Interpolating Missing Values
df.interpolate(): Interpolates missing values using various methods (linear, polynomial, etc.).

5. Replacing Specific Values
df.replace(to_replace=np.nan, value=0): Replaces specific values (e.g., NaN) with another value.
'''
#6. What is the purpose of groupby() in Pandas.
'''
The groupby() function in Pandas is used to split data into groups based on some criteria, and then perform operations on each group independently.

import pandas as pd

# Sample DataFrame
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Values': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum of 'Values'
grouped = df.groupby('Category')['Values'].sum()

print(grouped)

Output:
Category
A     30
B     70
C    110
Name: Values, dtype: int64
'''
#7. How do you merge two Dataframe in Pandas.
'''
You can merge two DataFrames in Pandas using the merge() function. It combines DataFrames based on a key column or index.

import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 90, 88]})

# Merge DataFrames on 'ID' column
merged_df = df1.merge(df2, on='ID', how='inner')

print(merged_df)

The how parameter can be 'inner', 'outer', 'left', or 'right' to specify the type of join.
'''
#8. Explain the concept of reshaping data in Pandas using pivot_table and melt.
'''
Reshaping data in Pandas involves changing the layout of a DataFrame to make it more suitable for analysis or visualization. Two key functions for reshaping data are pivot_table and melt.

1. pivot_table
The pivot_table function is used to create a spreadsheet-style pivot table as a DataFrame. It aggregates data based on one or more keys and can perform various summary statistics.

Key Parameters:
values: Column to aggregate.
index: Column(s) to set as the index.
columns: Column(s) to create new columns.
aggfunc: Aggregation function (e.g., 'mean', 'sum').

Example:
import pandas as pd

# Sample DataFrame
data = {
    'Date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Values': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Pivot table
pivot_df = df.pivot_table(values='Values', index='Date', columns='Category', aggfunc='sum')

print(pivot_df)

2. melt
The melt function is used to transform or "melt" a DataFrame from a wide format to a long format. It unpivots DataFrame from wide format to long format, making it easier to work with for analysis and visualization.

Key Parameters:
id_vars: Column(s) to keep as identifier variables.
value_vars: Column(s) to unpivot (if not specified, all columns that are not id_vars will be used).
var_name: Name to use for the variable column.
value_name: Name to use for the value column.

Example:
# Sample DataFrame
pivot_df = pd.DataFrame({
    'Date': ['2021-01-01', '2021-01-02'],
    'A': [10, 30],
    'B': [20, 40]
})

# Melt DataFrame
melted_df = pivot_df.melt(id_vars='Date', value_vars=['A', 'B'], var_name='Category', value_name='Values')

print(melted_df)
'''
#9. How do you apply a function to each element in a DataFrame in Pandas.
'''
In Pandas, you can apply a function to each element in a DataFrame using the applymap() method. This method applies a function to every single element in the DataFrame.

Example:
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Function to apply to each element
def square(x):
    return x ** 2

# Apply the function to each element in the DataFrame
result = df.applymap(square)

print(result)
'''
#10. What is the purpose of apply and applymap function in Pandas.
'''
In Pandas, apply() and applymap() functions are used to apply functions to DataFrames. They serve different purposes based on the scope and granularity of the application.

1. apply()
The apply() function applies a function along a specific axis of the DataFrame, either across rows or columns.

Key Parameters:
func: The function to apply.
axis: Axis along which the function is applied (0 for index/rows, 1 for columns).
Purpose:
To perform row-wise or column-wise operations.
Suitable for functions that need to process entire rows or columns at a time.
Example:
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Function to apply
def sum_row(row):
    return row.sum()

# Apply the function to each row
result = df.apply(sum_row, axis=1)

print(result)

2. applymap()
The applymap() function applies a function to each element of the DataFrame.

Key Parameters:
func: The function to apply to each element.
Purpose:
To perform element-wise operations across the entire DataFrame.
Suitable for functions that process individual elements independently.

Example:
# Function to apply to each element
def square(x):
    return x ** 2

# Apply the function to each element in the DataFrame
result = df.applymap(square)

print(result)
'''
