# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %% Plot in General
x = np.array([0, 1, 2, 3, 4])
y = 2*x

plt.figure(figsize=(4, 5), dpi=100)

plt.plot(x, y, color='red', linewidth=2, marker='.',
         markersize=4, linestyle='-', label='2*x')
plt.plot(x, x**2, color='blue', marker='.', label='x^2')

plt.title('Main Title')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.yticks(np.arange(0, 17, step=4))

plt.legend()

plt.savefig('mygraph.png', dpi=100)  # LQ
plt.savefig('mygraph.eps', format='eps', dpi=300)  # HQ
plt.show()
# %%
