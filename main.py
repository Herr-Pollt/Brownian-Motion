"""

Creates a graph that shows Brownian motion aka
shows how a person's coordinates will look if they
walk in a random direction n steps

"""

import matplotlib.pyplot as plt
import numpy as np
import random


n = 1000 #number of steps
x = np.zeros(100)
y = np.zeros(100)
temp = 0


plt.figure(0)

for i in range(n):
    temp = random.randint(1, 4)
    if temp == 1:
        if i == 0:
            y[i] = 1
        else:
            y[i] = y[i-1] + 1
            x[i] = x[i-1]
    elif temp == 2:
        if i == 0:
            x[i] = 1
        else:
            x[i] = x[i-1] + 1
            y[i] = y[i-1]
    elif temp == 3:
        if i == 0:
            y[i] = -1
        else:
            y[i] = y[i-1] - 1
            x[i] = x[i-1]
    elif temp == 4:
        if i == 0:
            x[i] = -1
        else:
            x[i] = x[i-1] - 1
            y[i] = y[i-1]

    plt.clf()
    plt.subplot()
    plt.plot(x[:i], "b")
    plt.subplot()
    plt.plot(y[:i], "r")
    plt.title("Blue is X, Red is Y")
    plt.pause(0.1)

plt.show()