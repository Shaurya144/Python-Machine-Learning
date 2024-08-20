# Here we will learn how to make functions to get the answers we want
# and some python modules we can use
# There are three types of data
# Numerical, Catergorical and Ordinal
# Categorical data can not be measured up against each other
# Ordinal data is like categorical but it can be compared
# Numerical data can be split into two sections:
# Discrete data - limited to integers
# Continuous data - measured data that can be any number

import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]



# Mean - The average value
x = numpy.mean(speed) # add them together and divide by number of items
print(x)



# Median - The mid point value
x = numpy.median(speed) # item in the middle
print(x)


# Mode - The most common value
x = stats.mode(speed)
print(x)