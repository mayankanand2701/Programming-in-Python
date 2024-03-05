marks=int(input("Enter the marks = "))
grade=""
if marks>=90 and marks<=100: grade="A"
elif marks>=70 and marks<=89: grade="B"
elif marks>=50 and marks<=69: grade="C"
elif marks>=40 and marks<=49: grade="D"
elif marks>=0 and marks<=39: grade="F"

print("Grade Obtained : ",grade)
