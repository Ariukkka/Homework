import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Line bar  
x = np.random.uniform(low=0.5, high=5.3, size=(100))
y = np.random.uniform(low=1, high=10.5, size=(100))
plt.plot(x, y, color = "black")
plt.show()

# Scatter
x = np.random.uniform(low=0.5, high=5.3, size=(100))
y = np.random.uniform(low=1, high=10.5, size=(100))
plt.scatter(x, y)
plt.show()

# Stacked bar
x = np.random.uniform(low=5, high=10, size=(100))
y = np.random.uniform(low=1, high=10.5, size=(100))
plt.plot(kind='bar', stacked=False)
plt.show()

# Unstacked bar
x = np.random.uniform(low=0.5, high=5.3, size=(100))
y = np.random.uniform(low=1, high=10.5, size=(100))
plt.bar(x, y, color = "red")
plt.show()

# Histogram
x = np.random.uniform(low=0.5, high=5.3, size=(100))
plt.hist(x)
plt.show()

# Area
x = np.random.uniform(low=5, high=10, size=(100))
y = np.random.uniform(low=1, high=10.5, size=(100))
df = pd.DataFrame("x", "y");
df.plot(kind='area', stacked=False)
plt.show()

# Pie
x = np.random.uniform(low=0.5, high=5.3, size=(100))
plt.pie(x)
plt.show()

# Violin plot
