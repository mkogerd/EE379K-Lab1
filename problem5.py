# Michael Koger Darden (mkd788)
# EE 379K Lab 1 - Problem #5

# Check for numpy and pyplot

try:
        import numpy as np
except ImportError:
        print("numpy is not installed")
try:
        import pandas as pd
except ImportError:
        print("pandas is not installed")

df = pd.read_csv('PatientData.csv', header=None, na_values=["?"])   # Read in PatientData

#(a) How many patients and how many features are there?
print("(a) There are {pat} patients and {feat} features.".format(pat = df.shape[0], feat = df.shape[1]))

#(b) What is the meaning of the first 4 features? See if you can understand what they mean.
print("(b) The first four features are Age (years), Gender (0/1-male/female), weight (pounds), and height (inches).")

#(c) Are there missing values? Replace them with the average of the corresponding feature column
print("(c) Yes, there are missing values.")
for col in df:
    df = df.replace(np.NaN, df[col].mean())
print("The missing values have been replaced.")
#ds = df.ix[:,12:14]
#print(ds)

# (d) How could you test which features strongly influence the patient condition and which do not?
print("(d) You could test which features strongly influence the patient condition and which do not by iterating through the columns and finding which columns have the highest and lowest correlations respectively with the patient condition column using numpy correlation functions.")

print("I think the three most important features are age, weight, and patient condition.")
