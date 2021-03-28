import matplotlib.pyplot as plt

plt.style.use('ggplot')
print(plt.style.available)

x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]

plt.bar(x1, y1)
plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('vertical title')
plt.show()