import matplotlib.pyplot as plt
import numpy as np 

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

fig = plt.figure()
fig.suptitle("Plot titles")

plt.subplot(2,2,1)
plt.plot(x,y , color = 'grey')
plt.xlabel('X2')
plt.ylabel('Y2')

plt.subplot(2,2,2)
plt.plot(x,y , color = 'blue')
plt.xlabel('X2')
plt.ylabel('Y2')

plt.subplot(2,2,3)
plt.plot(x,y , color = 'purple')
plt.xlabel('X2')
plt.ylabel('Y2')

plt.subplot(2,2,4)
plt.plot(x,y , color = 'green')
plt.xlabel('X2')
plt.ylabel('Y2')

plt.show()