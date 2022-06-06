"""
Atividade Semana 04 - Sistemas Embarcados
Lucas Russignoli 11721EAU004
"""

import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3,5,7,3])
a2 = np.zeros(10)
# a3 = npones(10)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0, 10, 100)
a7 = np.arange(0, 10, 0.02)

2*a1

1/a1

1/a1 + a1 +2

x = np.linspace(0, 1, 100)
x**2

# plt.plot(x, y)

plt.hist(a4)

def f(x):
	return x**2 * np.sin(x) / np.exp(-x)

x = np.linspace(0, 10, 100)
y = f(x)

plt.plot(x,y)