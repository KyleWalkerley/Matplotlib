import matplotlib.pyplot as plt 
x1  = [1,2,3,4,5]
y1 = [1,2,4,8,16]

colors = ['black', 'grey', 'blue', 'yellow', 'pink']
plt.bar(x1,y1,edgecolor="black",color=colors, linewidth=3)
plt.title('Your title')
plt.xlabel('horizontal label')
plt.ylabel('vertical label')
plt.show()