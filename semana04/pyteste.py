import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

G1s = tf([1], [1,1])
print(G1s)

G2s = tf([25], [1,2,25])
print(G2s)

t = np.arange(0,10,1e-3)

y1, T1 = step(G1s, t)
y2, T2 = step(G2s, t)

plt.plot(t,y1)
plt.plot(t,y2)
plt.show()


