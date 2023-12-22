def collinear(x1, y1, x2, y2, x3, y3):
    area = 0.5 * ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))
    return area == 0
x1=int(input("Enter the x value of Point 1 : "))
y1=int(input("Enter the y value of Point 1 : "))
x2=int(input("Enter the x value of Point 2 : "))
y2=int(input("Enter the y value of Point 2 : "))
x3=int(input("Enter the x value of Point 3 : "))
y3=int(input("Enter the y value of Point 3 : "))
result = collinear(x1, y1, x2, y2, x3, y3)
print("Are points collinear : ", result)
    
