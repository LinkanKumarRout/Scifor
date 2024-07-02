#1. What is matplotlib and what are it's main features.
'''
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is widely used for its ability to produce high-quality plots and charts with minimal code.

Main Features:

Wide Range of Plots: Supports various types of plots like line, bar, scatter, histogram, pie, and more.

Customization: Highly customizable plots, allowing control over colors, labels, sizes, and more.

Integration: Integrates well with Pandas, NumPy, and other scientific computing libraries.

Interactivity: Supports interactive plots that can be embedded in applications using GUI toolkits.

Publication Quality: Capable of producing plots suitable for publication with precise control over every aspect.

Subplots: Ability to create complex layouts with multiple subplots.

Animations: Supports the creation of animated plots.

Extensive Documentation: Comprehensive documentation and a large community for support.
Example:
import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Creating a line plot
plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Line Plot')
plt.show()
'''
#2. How do you create a basic plt using matplotlib.
'''
import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Creating a line plot
plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Line Plot')
plt.show()
'''
#3. Explain the difference between plt.plot() and plt.scatter() in matplotlib.
'''
In Matplotlib, plt.plot() and plt.scatter() are both used to create visualizations.

However, there are some key differences between the two functions:
1. plt.plot() is used to create a line plot, which connects the points in the data.
2. plt.scatter() is used to create a scatter plot, which displays the points as individual markers.
'''
#4. What are the different types of plot available in matplotlib.
'''
Different types of plot available in matplotlib are:
1. Line plot: This type of plot connects the points in the data using a line.
2. Scatter plot: This type of plot displays the points as individual markers.
3. Bar plot: This type of plot displays the data as bars.
4. Histogram: This type of plot displays the data as a histogram.
5. Pie chart: This type of plot displays the data as a pie chart.
'''
#5. How do you add labels, titles, and legends to a matplotlib plot.
'''
We can add labels, titles and legends to a matplotlib plot like this:
1. To add labels, we can use the plt.xlabel() and plt.ylabel() functions to add labels to the x and y axes respectively.
2. To add a title, we can use the plt.title() function.
3. To add a legend, we can use the plt.legend() function.
'''
