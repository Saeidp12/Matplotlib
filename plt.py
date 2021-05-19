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

# How many nations are there?
print(fifa['nationality'].value_counts())
# How to put all English players in one variable
England = fifa.loc[fifa['nationality'] == 'England']
print(len(England))

# Sections (countries) of the pie chart
nations = ['England', 'Spain','Germany', 'France']
counts = []

# Appending number of players in fifa21 for each country in nations
for i in range(len(nations)):
    counts.append(len(fifa.loc[fifa['nationality'] == nations[i]]))

# print(counts)
nations.append('others')
counts.append(len(fifa) - sum(counts))
for i in range(len(counts)):
    print(f'{nations[i]}: {counts[i]}')

# Pie Chart
explode = [0.1, 0, 0, 0, 0]
plt.pie(x=counts, explode=explode, labels=nations, autopct='%.1f')
plt.show()

# Players of 3 main leagues
EPL = fifa.loc[fifa['league_name'] == 'English Premier League']['overall']
ESP = fifa.loc[fifa['league_name'] == 'Spain Primera Division']['overall']
ITA = fifa.loc[fifa['league_name'] == 'Italian Serie A']['overall']

# Box Plot
plt.boxplot([EPL, ESP, ITA], labels=['EPL','ESP','ITA'])
plt.show()
