maximum=[17,19,21,28,33,38,37,37,31,23,19,18]
minimum=[-62,-59,-56,-46,-32,-18,-9,-13,-25,-46,-52,-58]

months=["January","Feburary","March","April","May","June","July","August","September","October","November","December"]

# as nothing is given we need to plot bar chart here
import matplotlib.pyplot as plt 
plt.bar(months,maximum, color ='gray',width =0.5)
plt.bar(months,minimum, color ='red',width =0.5)
plt.xlabel('Months')
plt.ylabel("Maximum Temperature")
plt.xticks(rotation=90)
plt.axhline(0,color='black',linestyle="--")
plt.show()

# this is for seperate graph for maximum and minimum but plottiing the ssame graph above code
# for minimum temperature
#plt.bar(months,minimum, color ='red',width =0.5)
#plt.xlabel('Months')
#plt.ylabel("Manimum Temperature")
#plt.xticks(rotation=90)
#plt.show()
