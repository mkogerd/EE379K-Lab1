# Michael Koger Darden (mkd788)
# EE 379K Lab 1 - Problem #4

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
mean = [-5, 5]
cov = [[20, .8], [.8,30]]
n = 25000
x, y, = np.random.multivariate_normal(mean, cov, n).T
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()

# Estimate the mean and covariance matrix for this multi-dimensional data using elementary numpy commands
# Mean Matrix
xy = np.vstack((x,y))   # Form 2d array with X and Y samples for easier navigation
mean = [0, 0]           # [mean X, mean Y]
for r in range(2):
    sum = 0
    for i in range(n):
        sum += xy[r][i] # Mean summation
    mean[r] = sum/n

# Covariance Matrix
cov = [[0, 0], [0, 0]]  # [[variance X, covariance], [covariance, variance Y]]
for r in range(2):
    for c in range(2):
        sum = 0
        for i in range(n):
            sum += (xy[r][i]-mean[r])*(xy[c][i]-mean[c]) # Variance summation
        cov[r][c] = sum/n

print("Mean of X is {meanX}, mean of Y is {meanY}".format(meanX = mean[0], meanY = mean[1]))
print("Covariance Matrix:")
print(cov)
