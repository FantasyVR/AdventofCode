import re
import numpy as np
from operator import itemgetter

e10 = [[int(z) for z in re.findall(r'-?\d+', x)] for x in get_input_by_lines(10)]

n10 = np.array(e10)

coords = n10[:, :2].copy()
vels = n10[:, 2:].copy()

def row_exists(coords):
    return len(set(np.array(sorted(coords, key=itemgetter(0)))[:6, 0])) == 1

for i in range(1, 20000):
    coords += vels
    if row_exists(coords):
        print(i)


import matplotlib.pyplot as plt

coords = n10[:, :2].copy()
vels = n10[:, 2:].copy()

coords += 10312*vels

canvas = np.zeros(coords.max(axis=0)+2)
canvas[coords[:, 0], coords[:, 1]] += 1


minx, miny = coords.min(axis=0)
plt.imshow(canvas[minx-1:, miny-1:].T)
plt.show()