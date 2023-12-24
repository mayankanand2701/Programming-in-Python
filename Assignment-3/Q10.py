def glcm(x,y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
print("LCM of two number is = ",glcm(a,b))

