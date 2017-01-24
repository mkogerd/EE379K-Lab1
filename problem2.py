# Michael Koger Darden (mkd788)
# EE 379K Lab 1 - Problem #2

# Check for numpy and pyplot
try:
        import numpy as np
except ImportError:
        print("numpy is not installed")
try:
        import matplotlib.pyplot as plt
except ImportError:
        print("pyplot is not installed")

n1, n2, n3 = 10, 50, 250
z1, z2, z3 = [], [], []
for index in range(1000):
        x1 = np.random.binomial(1, .5, n1)      # Create Bernoulli Distribution (0 or 1)
        x2 = np.random.binomial(1, .5, n2)      # Create Bernoulli Distribution (0 or 1)
        x3 = np.random.binomial(1, .5, n3)      # Create Bernoulli Distribution (0 or 1)

        for i in range(len(x1)):
                x1[i] = x1[i]*2 - 1             # Convert to -1 and 1
        for i in range(len(x2)):
                x2[i] = x2[i]*2 - 1             # Convert to -1 and 1
        for i in range(len(x3)):
                x3[i] = x3[i]*2 - 1             # Convert to -1 and 1
        #temp1=1/n1*sum(n1)
        z1.append(1/n1*sum(x1))
        z2.append(1/n2*sum(x2))
        z3.append(1/n3*sum(x3))
plt.hist(z1, 30, label="{n} draws".format(n=n1))
plt.hist(z2, 30, label="{n} draws".format(n=n2))
plt.hist(z3, 30, label="{n} draws".format(n=n3))
plt.legend()
plt.show()

