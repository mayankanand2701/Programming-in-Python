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

# To create a seperate vector for each subjects marks
math=[]
cs=[]
sci=[]
for x in student:
    math.append(x["Math"])
    cs.append(x["Computer Science"])
    sci.append(x["Science"])

# To calculate the total sum
def sum(list):
    tsum=0
    for x in list: tsum=tsum+x
    return tsum
 
# To store the total sum of each subject
total_math=sum(math)
total_cs=sum(cs)
total_sci=sum(sci)

print("Total Marks Obtained by all 20 Student's in Maths  is : ",total_math)
print("Total Marks Obtained by all 20 Student's in Computer Science is : ",total_cs)
print("Total Marks Obtained by all 20 Student's in Science is : ",total_sci)
print()
print("The Average Marks obtained by all 20 Student's in Math is ",(total_math/20))
print("The Average Marks obtained by all 20 Student's in Computer Science is ",(total_cs/20))
print("The Average Marks obtained by all 20 Student's in Science is ",(total_sci/20))
