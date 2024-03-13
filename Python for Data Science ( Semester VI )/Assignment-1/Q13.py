mentions=[500,505]
years=[2017,2018]

import matplotlib.pyplot as plt
plt.bar(years,mentions, color ='maroon')
plt.xlim([2015,2020])
plt.xlabel("Number of Mentions")
plt.ylabel("Year")
plt.show()
