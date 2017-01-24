# Michael Koger Darden (mkd788)
# EE 379K Lab 1

# Check for numpy and pyplot
try:
	import numpy as np
except ImportError:
	print("numpy is not installed")
try:
        import matplotlib.pyplot as plt
except ImportError:
        print("pyplot is not installed")

#_____ QUESTION ONE _____#
print("QUESTION ONE") 
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

#_____ QUESTION TWO _____#
print("QUESTION TWO") 
n1, n2, n3 = 10, 50, 250
z1, z2, z3 = [], [], []
for index in range(1000):
	x1 = np.random.binomial(1, .5, n1)	# Create Bernoulli Distribution (0 or 1)
	x2 = np.random.binomial(1, .5, n2)	# Create Bernoulli Distribution (0 or 1)
	x3 = np.random.binomial(1, .5, n3)	# Create Bernoulli Distribution (0 or 1)
	
	for i in range(len(x1)):
		x1[i] = x1[i]*2 - 1		# Convert to -1 and 1
	for i in range(len(x2)):
		x2[i] = x2[i]*2 - 1		# Convert to -1 and 1
	for i in range(len(x3)):
		x3[i] = x3[i]*2 - 1		# Convert to -1 and 1
	#temp1=1/n1*sum(n1)
	z1.append(1/n1*sum(x1))
	z2.append(1/n2*sum(x2))
	z3.append(1/n3*sum(x3))
plt.hist(z1, 30, label="{n} draws".format(n=n1))
plt.hist(z2, 30, label="{n} draws".format(n=n2))
plt.hist(z3, 30, label="{n} draws".format(n=n3))
plt.legend()
plt.show()

#_____ QUESTION THREE _____#
print("QUESTION THREE")
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

#_____ QUESTION FOUR _____#
print("QUESTION FOUR")
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
print(cov)


