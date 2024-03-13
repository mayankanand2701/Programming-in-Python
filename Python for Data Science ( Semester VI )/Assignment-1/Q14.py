test_1_grades=[99,90,85,97,80]
test_2_grades=[100,85,60,90,70]

import matplotlib.pyplot as plt
plt.scatter(test_1_grades,test_2_grades, c ="purple")
#plt.axis("equal")
plt.xlabel(" Test 1 Grades ")
plt.ylabel(" Test 2 Grades ")
plt.show()
