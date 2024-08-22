# In Machine Learning we create models to predict the outcome of certain events
# To measure if the model is good enough, we can use a method called Train/Test

# Train the model means create the model.
# Test the model means test the accuracy of the model.

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# It is called Train/Test because you split the data set into two sets: a training set and a testing set.
# 80% for training, and 20% for testing
# This is 80% of the data set 
train_x = x[:80]
train_y = y[:80]


# This is 20% of the data set
test_x = x[80:]
test_y = y[80:]

plt.scatter(train_x, train_y)
plt.show()

plt.scatter(test_x, test_y)
plt.show()