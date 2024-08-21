import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

# We can see that the dots are concentrated around the value 5 on the x-axis, and 10 on the y-axis.
# We can also see that the spread is wider on the y-axis than on the x-axis.