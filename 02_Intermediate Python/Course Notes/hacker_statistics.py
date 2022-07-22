# Random Float

import numpy as np

np.random.seed(123)

# seed() sets the random seed, so that your results are reproducible.

print(np.random.rand())

# rand() returns a single random number, which is between 0 and 1.

print('\n-------------------\n')

# Roll the dice

print(np.random.randint(1, 7))

print(np.random.randint(1, 7))

print('\n-------------------\n')

# Determine your next Move

# Starting step
step = 50
# Roll the dice
dice = np.random.randint(1, 7)
# Finish the control construct
if dice <= 2:
    # if dice 1 or 2 one step down
    step = step - 1
elif dice <= 5:
    # if dice 3, 4, 5 one step up
    step = step + 1
else :
    # if dice 6, you throw the dice again and move the same amount as dice
    step = step + np.random.randint(1, 7)

print(dice, step)

print('\n-------------------\n')

## Random Walk

# Coin Toss
outcomes = []

for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append('H')
    else:
        outcomes.append('T')

print(outcomes)

# Random Walk

tails =[0]

for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)

print(tails)

print('\n-------------------\n')

random_walk = [0]

for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]
    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine next step
    if dice <= 2:
        # use max() to make sure step can't go below 0
        step = max(0, step - 1)
        # step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)
    
    # append next_step to random_walk
    random_walk.append(step)

print(random_walk)

print('\n-------------------\n')

# Visualize the Random Walk

import matplotlib.pyplot as plt

plt.plot(random_walk)
plt.show()
plt.clf()

print('\n-------------------\n')

## Distribution of Random Walks

final_tails = []

for x in range(1000):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])

plt.hist(final_tails, bins=10)
plt.show()
plt.clf()

print('\n-------------------\n')

all_walks = []

# Simulate random walk 10 times

for i in range(500):

    # Code from before
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        # implement clumsiniess
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)

# Visualize all_walks

# Convert all_walks to Numpy Array

np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw)

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Plot np_aw and show
plt.clf()
plt.plot(np_aw_t)
plt.show()

# Make a histogram of ends
plt.clf()
plt.hist(ends)
plt.show()


# Calculate the odds
odds = np.mean(ends >= 60)
print('Odds are ' + str(odds * 100) + '%')