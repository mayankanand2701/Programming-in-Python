import matplotlib.pyplot as plt
import math

xlist=[]
ylist=[]
ylist1=[]
ylist2=[]
ylist3=[]
for x in range(-10,11):
    xlist.append(x)
    ylist.append((x**1)*math.sin(x))
    ylist1.append((x**2)*math.sin(x))
    ylist2.append((x**3)*math.sin(x))
    ylist3.append((x**4)*math.sin(x))
    
plt.plot(xlist, ylist, color='red')
plt.title("x sin(x)")
plt.show()

plt.plot(xlist, ylist1, color='red')
plt.title("x^2 sin(x)")
plt.show()

plt.plot(xlist, ylist2, color='red')
plt.title("x^3 sin(x)")
plt.show()

plt.plot(xlist, ylist3, color='red')
plt.title("x^4 sin(x)")
plt.show()
