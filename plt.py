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

# Subplots
x = np.array([0,1,2,3,4])
y = 2*x

plt.subplot(2, 2, 1) #(nrow, ncol, index)
plt.plot(x, y, 'red')
plt.subplot(2, 2, 2)
plt.plot(x, y, 'blue')
plt.subplot(2, 2, 3)
plt.plot(x, y, 'green')
plt.subplot(2, 2, 4)
plt.plot(x, y, 'yellow')

plt.show()

# Fifa 21 Player Rankings
fifa = pd.read_csv('fifa21.csv')

print(fifa.shape)  # gives us both dimensions
print(len(fifa))  # number of rows only

# Count Values of a specified column
print(fifa['preferred_foot'].value_counts())

# Barplot
plt.bar(['right', 'left'], fifa['preferred_foot'].value_counts())

# Descriptive Statistics
print(fifa['overall'].describe())

# Bins required for histogram
bins = [40, 50, 60, 70, 80, 90, 100]

# Reset the Canvas Width and Height Ratio
plt.figure(figsize=(8, 5))

# Histogram of player overalls with specified color
plt.hist(fifa['overall'], bins=bins, color='skyblue', edgecolor='blue')

# Plot labels and title
plt.xlabel('Player Overalls')
plt.ylabel('Frequency')
plt.title('Histogram of player overalls')

plt.show()
