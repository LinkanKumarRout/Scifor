import seaborn as sns
import matplotlib.pyplot as plt

# set_style()
# 'darkgrid', 'whitegrid', 'dark', 'white' , 'ticks'

# Set the style to whitegrid
sns.set_style("whitegrid")

# Box plot
data = sns.load_dataset('iris')
sns.boxplot(x='species', y='petal_length', data=data)
plt.show()

# Set the color palette to pastel
sns.color_palette("pastel")

# Scatter plot
data = sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', hue='sex', data=data)
plt.show()

# distplot()
data = sns.load_dataset('tips')
sns.distplot(data['total_bill'])
plt.show()

# Scatter plot
data = sns.load_dataset('iris')
sns.scatterplot(x='sepal_length', y='sepal_width', data=data)
plt.show()

# Line plot
data = sns.load_dataset('iris')
sns.lineplot(x='sepal_length', y='sepal_width', data=data)
plt.show()

# HeatMap
dataset = sns.load_dataset('flights')
data = dataset.pivot(index='month', columns='year', values='passengers')
sns.heatmap(data, annot=True, fmt="d", cmap="YlGnBu")
plt.show()