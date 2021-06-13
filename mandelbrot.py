import pandas as pd
from numpy import arange
from itertools import product

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
coefficients = product(arange(-limit, limit, step), repeat=2)

frame = pd.DataFrame([complex(x[0], x[1]) for x in coefficients], columns=['Coordinates'])
# below does not work because you cannot pass list of tuples to map as arguments. You have to pass iterable of n lists
# where n = number of arguments; so list 1 contains all the first arguments, list 2 all the second arguments etc etc
# frame = pd.DataFrame(map(complex, coefficients), columns=['Coordinates'])
frame.loc[:, 'Iterations'] = frame.Coordinates.apply(mandelbrot, args=(limit*10, ))
pass
