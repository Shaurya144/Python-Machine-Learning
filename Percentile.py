# Percentiles are used in statistics to give you a number that describes
# the value that a given percent of the values are lower than.

import numpy

dataSet = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(dataSet, 75)

print(x) # 43
# This means that 75% of items in dataSet are below 43
