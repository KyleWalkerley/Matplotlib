import matplotlib.pyplot as plt 

values = [16, 18, 4, 8]
pielabels = ['Python', 'Ruby', 'Java', 'Perl']
piecolors = ['red','orange','yellow','black']
pieexplode = [0.3,0.1,0.1,0.5]

plt.pie(values, labels = pielabels, explode= pieexplode, colors= piecolors, startangle=90)
plt.title("pie chart")
plt.xlabel("Horizontal title")
plt.ylabel("verical title")
plt.legend(loc='best')
plt.show() 