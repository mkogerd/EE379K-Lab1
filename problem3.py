# Michael Koger Darden (mkd788)
# EE 379K Lab 1 - Problem #3

# Check for numpy and pyplot
try:
        import numpy as np
except ImportError:
        print("numpy is not installed")
try:
        import matplotlib.pyplot as plt
except ImportError:
        print("pyplot is not installed")


# Generate 25,000 samples from a Gaussian distribution with mean 0 and standard deviation 5.
mu, sigma, n = 0, 5, 25000 # mean, standard deviation, and number of samples
dist = np.random.normal(mu, sigma, n)
plt.hist(dist, 30)
plt.show()

# Estimate the mean and standard deviation of this gaussian using elementary numpy commands
sum = 0 # Mean
for i in range(n):
        sum += dist[i]
mean = sum/n
sum = 0 # Standard Deviation
for i in range(n):
        sum += (dist[i]-mean)**2
dev = np.sqrt(sum/n)
print("Mean is {mean}, standard deviation is {dev}".format(mean = mean, dev = dev))
