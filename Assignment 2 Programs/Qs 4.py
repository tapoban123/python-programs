### Write a program that takes a list Of numbers and generates a histogram displaying the frequency Of each number,

import matplotlib.pyplot as plot

numbers = list(map(int, input("Enter the numbers separated by a space: ").split()))

histogram = plot.hist(x=numbers)

plot.show()
