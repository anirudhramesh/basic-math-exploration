import pandas as pd
import numpy as np
from itertools import product
from matplotlib import pyplot as plt

MAX_ITERATIONS = 5_000


def mandelbrot(c, limit_):
    c = complex(c['x'], c['y'])
    z = 0
    count = 0
    while abs(z) <= limit_ and count < MAX_ITERATIONS:
        z = z**2 + c
        count += 1
    return count


limit = 5
step = 0.05
coefficients = product(np.arange(-limit, limit, step), repeat=2)

frame = pd.DataFrame(coefficients, columns=['x', 'y'])
# below does not work because you cannot pass list of tuples to map as arguments. You have to pass iterable of n lists
# where n = number of arguments; so list 1 contains all the first arguments, list 2 all the second arguments etc etc
# frame = pd.DataFrame(map(complex, coefficients), columns=['Coordinates'])
frame.loc[:, 'Iterations'] = frame[['x', 'y']].apply(mandelbrot, axis=1, args=(limit*10, ))

fig, ax = plt.subplots(figsize=(10, 12))
ax.scatter(frame['x'], frame['y'], c=frame['Iterations'], cmap='Greens')
fig.savefig('mandelbrot_plot.png')
