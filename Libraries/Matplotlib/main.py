import matplotlib.pyplot as plt

# Line Plot(Graph)
# x, y can be a list, tuple, array or other iterable objects having numerical data
x = [1,2,3,4,5]
y = [2,3,4,7,11]
plt.plot(x,y) # line graph
plt.show() # to show the graph

plt.scatter(x, y) # scatter plot of points ( to view the data points )
plt.show()

# Bar plot
branches = ['Kdp', 'Bbsr', 'ctk', 'bal']
students = [20, 35, 50, 40]
plt.bar(branches, students)
plt.show()

# Histogram Plot
# this graph is used to represent frequency of distribution of a dataset
import pandas as pd
data = pd.read_csv('/content/sample_data/california_housing_test.csv')
rooms = data['total_rooms']
plt.hist(rooms)
plt.show()

populations = [22,55,62,45,21,22,34,42,57,86,65,54,74,32,12,23,56,42,70,65,55,111,115,80,75,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(populations, bins, histtype='bar', rwidth=0.8, color='blue')
plt.show()

plt.plot(x, y)
plt.xlabel('X - axis') # gives the name of x-axis
plt.ylabel('Y - axis') # gives the name of y-axis
plt.title("Line Plot") # gives the title of our graph
plt.show()

plt.hist(populations, bins, histtype='bar', rwidth=0.8, color='blue')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.title("Line Plot")
plt.legend('x', 'y')
plt.show()

# xlim() and ylim() these are used to set the limit for x-axis and y-axis
plt.plot(x,y)
plt.xlim(1,6)
plt.ylim(1,12)
plt.show()

players = ['Kohli', 'Rohit', 'Dhoni', 'Surya', 'Sachin']
runs = [183, 264, 183, 90, 200]
plt.pie(runs, labels= players) # creates a pie graph
plt.show()

# savefig() - this is used to save our plot as an image file
plt.plot(x,y)
plt.savefig('graph.png')

# Customize appearance of line plot

# format string containing color and style of line plot
plt.plot(x, y, 'g-.')
plt.show()

# linewidth or lw
plt.plot(x,y, linewidth=5)
plt.show()

# linestyle or ls
# its values are solid, dotted, dashdot, --, -., None, -
plt.plot(x, y, linestyle = 'dashdot')
plt.show()

# color
plt.plot(x,y, color='green')

# marker and markersize
plt.plot(x, y, marker='o', markersize=8)

plt.plot(x,y)
plt.grid()
plt.show()