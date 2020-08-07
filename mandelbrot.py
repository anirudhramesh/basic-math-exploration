import pandas as pd
from numpy import arange as range

MAX_ITERATIONS = 1000


def mandelbrot(c, limit):
    z = 0
    count = 0
    while abs(z) <= limit and count < MAX_ITERATIONS:
        z = z**2 + c
        count += 1
    return count


limit = 5
step = 0.1
frame = pd.DataFrame([complex(x,y) for x in range(-limit, limit, step) for y in range(-limit, limit, step)], columns=['Coordinates'])
frame.loc[:, 'Iterations'] = frame.Coordinates.apply(mandelbrot, args=(limit, ))
