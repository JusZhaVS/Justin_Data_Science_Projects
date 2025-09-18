import numpy as np

#normal distribution samples
samples = np.random.normal(loc = 0, scale=1, size=10) #loc is mean, scale is std, size is num of samples
print(samples)

outcomes = ['a', 'b', 'c']
probs = [0.2, 0.5, 0.3]

discrete_samples = np.random.choice(outcomes, size=5, p=probs) #outcomes is set of choices, size is num samples, p is prob distrib
print(discrete_samples)
