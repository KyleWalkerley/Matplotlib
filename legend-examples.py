import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]
y2 = [1, 1, 2, 3, 5]

plt.plot(x1, y1, 'r-o', label='students')
plt.plot(x1, y2, 'b-^', label='teatcher')

plt.subplots_adjust(right=0.7, bottom = 0.3)
plt.legend(bbox_to_anchor=(1.05, 0), loc='lower left')

plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('vertical title')
plt.grid(True)
plt.show()