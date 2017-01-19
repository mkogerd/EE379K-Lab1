# Check for numpy and matplot
try:
	import numpy as np
except ImportError:
	print("numpy is not installed")
try:
        import matplotlib.pyplot as plt
except ImportError:
        print("matplot is not installed")

# Create Gaussian distributions
mua, mub, sigma = -10, 10, 5 # means and standard deviation
a = np.random.normal(mua, sigma, 1000)
b = np.random.normal(mub, sigma, 1000)

# Use some untweeked code I found to show a histogram
count, bins, ignored = plt.hist(a, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mua)**2 / (2 * sigma**2) ), linewidth=2, color='r')
count, bins, ignored = plt.hist(b, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mub)**2 / (2 * sigma**2) ), linewidth=2, color='r')
print(len(a)) # print length of array (just checking for 1000)
plt.show()
