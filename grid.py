import matplotlib.pyplot as plt 

x1 = [1, 2, 3,  4, 5]
y1 = [1, 2, 4, 8, 16]

plt.plot(x1,y1, 'r^-', label= "students")
plt.legend(loc='best') 
plt.title("Your title")
plt.xlabel("horizontal title")
plt.ylabel("vertical title")
plt.grid(linestyle = '--', color = "grey", which='major')
plt.minorticks_on()
plt.show()