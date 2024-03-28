student = [
    {"student id": 1, "Math": 50, "Computer Science": 60, "Science": 73},
    {"student id": 2, "Math": 40, "Computer Science": 50, "Science": 55},
    {"student id": 3, "Math": 90, "Computer Science": 70, "Science": 95},
    {"student id": 4, "Math": 80, "Computer Science": 62, "Science": 72},
    {"student id": 5, "Math": 80, "Computer Science": 90, "Science": 45},
    {"student id": 6, "Math": 84, "Computer Science": 90, "Science": 50},
    {"student id": 7, "Math": 90, "Computer Science": 95, "Science": 55},
    {"student id": 8, "Math": 89, "Computer Science": 93, "Science": 53},
    {"student id": 9, "Math": 88, "Computer Science": 92, "Science": 58},
    {"student id": 10, "Math": 90, "Computer Science": 95, "Science": 55},
    {"student id": 11, "Math": 70, "Computer Science": 65, "Science": 39},
    {"student id": 12, "Math": 65, "Computer Science": 60, "Science": 35},
    {"student id": 13, "Math": 60, "Computer Science": 55, "Science": 30},
    {"student id": 14, "Math": 55, "Computer Science": 57, "Science": 25},
    {"student id": 15, "Math": 49, "Computer Science": 54, "Science": 22},
    {"student id": 16, "Math": 10, "Computer Science": 30, "Science": 11},
    {"student id": 17, "Math": 50, "Computer Science": 40, "Science": 16},
    {"student id": 18, "Math": 90, "Computer Science": 45, "Science": 80},
    {"student id": 19, "Math": 70, "Computer Science": 50, "Science": 39},
    {"student id": 20, "Math": 70, "Computer Science": 80, "Science": 75}
]

# To create a seperate vector for Compute Science marks
cs=[]

for x in student:
    cs.append(x["Computer Science"])
    
# To calculate the mean
sum=0
for x in cs:
    sum=sum+x
print("Mean of Computer Science Marks is : ",(sum/20))
    
# To calculate the median
# Since the number of observations is even,then the median is given by the average of (n/2)th  and  [(n/2) +1]th observation.
cs.sort()
print("Median of Computer Science Marks is : ",(cs[9]+cs[10])/2)

# To calculate the mode
from collections import Counter
count=Counter(cs)
frequency = count.most_common(1)[0][1]   # Get the frequency of the mode value
modes = [num for num, freq in count.items() if freq==frequency]  # Get all values with the maximum frequency
print("Mode(s) of Computer Science Marks are :", modes," with fequency of ",frequency,".")
