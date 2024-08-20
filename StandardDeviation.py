import numpy
# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)

# Variance is another number that indicates how spread out the values are.

asset = [32,111,138,28,59,77,97]

y = numpy.var(asset)

print(y)

# Standard Deviation is represented with the Sigma Symbol
# Variance is represented with the Sigma Symbol Squared