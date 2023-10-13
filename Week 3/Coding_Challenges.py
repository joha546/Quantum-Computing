'''Problem 1:
Research the numpy module to find a function that allows you simulate rolling a weighted die that is twice as likely
to land on 6 than a typical die. Then, simulate this die being rolled six times.'''

#Code:

import numpy as np
outcomes = [1, 2, 3, 4, 5, 6]
probabilities = [1/7, 1/7, 1/7, 1/7, 1/7, 2/7]
rolls = np.random.choice(outcomes, size=6, p=probabilities)
print("Results of six rolls:", rolls)


'''Problem 2:
Research the matplotlib module to find a function that creates a line graph of the data provided below. For an extra
 challenge, label the x-axis "Year" and the y-axis "Number of Transistors per Microprocessor in Millions". 
 This is a visual representation of Moore's Law!
'''
#code:
import matplotlib.pyplot as plt

# Data
years = [1972, 1982, 1992, 2002, 2012]
num_transistors = [0.004, 0.14, 3.11, 220.67, 2600]
plt.plot(years, num_transistors, marker='o', linestyle='-', color='b')
plt.xlabel("Year")
plt.ylabel("Number of Transistors per Microprocessor in Millions")
plt.title("Moore's Law")
plt.grid(True)
plt.show()
