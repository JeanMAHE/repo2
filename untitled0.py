# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 05:09:52 2023

@author: Jean
"""



import matplotlib.pyplot as plt

'''
oo = ['u', 'r']
circle = plt.Circle((1,1), radius = 0.1, color = 'green')
circle2 = plt.Circle((10,4), radius = 0.1, color = 'green')
oo[0] = plt.Line2D((1,10), (1,4), linewidth=0.7, color='green')
ax = plt.gca()
ax.add_patch(circle)
ax.add_patch(circle2)
ax.add_line(oo[0])
'''


list = [[3, 5], [6, 9], [7, 3]]

list2 = [[6, 9], [7, 3], [3, 5]]
y = list2[0]
z = list2[1]

list3 = []

print(len(list)-1)


for i in range(len(list)-1):
    list3.append(str(i))
    y = list2[i]
    z = list2[i+1]
    list3[i] = plt.Line2D((y[0], z[0]), (y[1], z[1]), linewidth=0.7, color='green')

ax = plt.gca()
ax.add_line(list3[1])
ax.add_line(list3[0])


plt.axis('scaled')
plt.show()