# In the real world, you would use much larger sets of data
# To create big data sets for testing, we use the Python module NumPy,
# which comes with a number of methods to create random data sets, of any size
import numpy
import matplotlib.pyplot as plt # to visualise the data set

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

# Normal Distribution also known as a bell curve
# We use the array from the numpy.random.normal() method, with 100000 values,  to draw a histogram with 100 bars.
# We specify that the mean value is 5.0, and the standard deviation is 1.0.
# Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
# And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
x = numpy.random.normal(5.0, 1.0, 100000)


plt.hist(x, 100)
plt.show()