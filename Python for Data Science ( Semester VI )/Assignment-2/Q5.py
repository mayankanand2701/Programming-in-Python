
import random
import matplotlib.pyplot as plt

# Generate a list of 100 random integers between 1 and 100
random_integers = [random.randint(1, 100) for _ in range(100)]

# Plot the histogram
plt.hist(random_integers, bins=100, color='skyblue', edgecolor='black')
plt.title('Histogram of 100 Random Integers')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Get the maximum value in the random integers list
max_value = max(random_integers)

plt.show()
