import random
import matplotlib.pyplot as plt

# random.seed(123)

# First exercise: Toss one 1d6
one_die = random.randint(1, 6)
print(one_die)

# Second exercise: Generate 6 random die tosses
tosses = [random.randint(1, 6) for i in range(6)]

# Plot histogram
plt.hist(tosses, bins=range(1, 8), edgecolor='black', align='left')
plt.xlabel('Die Face')
plt.ylabel('Frequency')
plt.title('Histogram of 6 Random Die Tosses')
plt.xticks(range(1, 7))
plt.show()

