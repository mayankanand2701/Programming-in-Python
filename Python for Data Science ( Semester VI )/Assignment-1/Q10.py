male=[53,51,71,31,33,39,52,27,54,30,64,26,21,54,52,20,59,32]
female=[53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42,32,48,23,23]

import matplotlib.pyplot as plt

# For male
plt.hist(male,bins=25,color='skyblue', edgecolor='black')
plt.xlabel('Male Age')
plt.title('Histogram of Age')
plt.show()

# For female
plt.hist(female,bins=25,color='lightgreen', edgecolor='black')
plt.xlabel('Female Age')
plt.title('Histogram of Age')
plt.show()
            
