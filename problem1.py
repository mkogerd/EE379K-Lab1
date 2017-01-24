# Michael Koger Darden (mkd788)
# EE 379K Lab 1 - Problem #1

# Check for numpy and pyplot
try:
        import numpy as np
except ImportError:
        print("numpy is not installed")
try:
        import matplotlib.pyplot as plt
except ImportError:
        print("pyplot is not installed")


# Create Gaussian distributions
mua, mub, sigma = -10, 10, 5 # means and standard deviation
a = np.random.normal(mua, sigma, 1000)
b = np.random.normal(mub, sigma, 1000)

# (a) sum and plot the 2 gaussians
c = [x + y for x, y in zip(a, b)]
#plt.hist(a, 30)
#plt.hist(b, 30)
plt.hist(c, 30)
plt.show()

# (b) Estimate the mean and variance of the sum
print("Mean of A is: {m} Variance of A is {v}".format(m=np.mean(a), v=np.var(a)))
print("Mean of B is: {m} Variance of B is {v}".format(m=np.mean(b), v=np.var(b)))
print("Mean of C is: {m} Variance of C is {v}".format(m=np.mean(c), v=np.var(c)))
