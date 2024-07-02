#1. What is seaborn and how does it relate to matplotlib.
'''
Seaborn is a library for making statistical graphics in Python. It is built on top of matplotlib and provides a high-level interface for drawing attractive and informative statistical graphics.

Seaborn is essentially a wrapper around matplotlib, meaning it uses matplotlib to draw plots and extends its functionality.While matplotlib requires more code to create complex visualizations, Seaborn provides a more concise and intuitive interface for common statistical plots.Seaborn is often used in conjunction with matplotlib. Users can leverage the simplicity of Seaborn for initial exploratory data analysis and then use matplotlib for more detailed customization or specific plot types not directly supported by Seaborn.
'''
#2. How do you create a basic plot using seaborn.
'''
We can create a basic plot using seaborn like this:

import seaborn as sns
sns.set_theme(style="darkgrid")
tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
'''
#3. Explain the purpose of hue parameter in seaborn plots.
'''
The main purpose of hue parameter in seaborn plots is to create a plot with multiple subplots, each representing a different category of data. For example,
if we have a dataset with three different categories of data, we can use the hue parameter to create
a plot with three subplots, each representing a different category of data.
'''
#4. How do you create subplots in matplotlib and seaborn.
'''
To create subplot in matplotlib.
Example:
import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# Plot data on each subplot
axes[0].plot(x, y1, label='sin(x)')
axes[0].set_title('Sine Plot')
axes[0].legend()

axes[1].plot(x, y2, label='cos(x)', color='orange')
axes[1].set_title('Cosine Plot')
axes[1].legend()

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()


To create subplots using seaborn.
Example:
import seaborn as sns

# Load sample dataset
tips = sns.load_dataset('tips')

# Create a categorical plot (strip plot) with subplots based on 'day'
sns.catplot(x='day', y='total_bill', data=tips, kind='strip', height=4, aspect=2)
plt.title('Total Bill by Day')
plt.show()
'''
#5. What are some common techniques for customizing the appearance of plots in matplotlib and seaborn.
'''
Matplotlib: Offers detailed control over plot elements such as colors, markers, labels, and annotations.
Seaborn: Provides high-level functions with built-in styles and color palettes, simplifying customization for statistical plots and grids.
Common techniques for customizing the appearance of plots in matplotlib and seaborn include:
- Changing the color palette: matplotlib offers a wide range of color palettes, while seaborn provides
built-in color palettes for statistical plots.

- Adjusting the font size and style: matplotlib allows you to specify the font size and style for
text elements, while seaborn provides built-in font styles for statistical plots.

- Adding annotations and labels: matplotlib provides functions for adding annotations and labels to
plots, while seaborn provides functions for adding annotations and labels to statistical plots.

- Adjusting the plot layout: matplotlib provides functions for adjusting the plot layout, such as
adjusting the figure size and adding a title, while seaborn provides functions for adjusting the
layout of statistical plots, such as adding a title and adjusting the spacing between plots.

- Customizing the plot style: matplotlib provides functions for customizing the plot style, such as
changing the line style and marker style, while seaborn provides functions for customizing the style
of statistical plots, such as changing the line style and marker style.

Example:
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Matplotlib example
plt.figure(figsize=(8, 4))
plt.plot(x, y1, color='blue', linestyle='--', label='sin(x)')
plt.plot(x, y2, color='red', linestyle='-', linewidth=2, label='cos(x)')
plt.title('Customized Matplotlib Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True, linestyle=':', linewidth=0.5)
plt.show()

# Seaborn example
sns.set(style='whitegrid', palette='pastel')
plt.figure(figsize=(8, 4))
sns.lineplot(x=x, y=y1, color='blue', linestyle='--', label='sin(x)')
sns.lineplot(x=x, y=y2, color='red', linestyle='-', linewidth=2, label='cos(x)')
plt.title('Customized Seaborn Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()
'''
