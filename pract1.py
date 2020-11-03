# Basics of python
# write a program to calculate area of circle, triangle, rectangle

#print("Whose area would you like to find: \n1.Triangle \n2.Circle \n3.Rectangle")
#inp = int(input("\nEnter your choice: "))
#if(inp == 1):
 #  baseLength = float(input("Enter base length: "))
 #   areaTriangle = (height*baseLength)/2
 #   print("The area of Triangle is: ",areaTriangle)
#elif(inp == 2):
 #   pi = 22/7
 #   radius = float(input("Enter the radius of the circle: "))
 #   areaCircle = pi*radius*radius
 #   print("The radius of circle is ",areaCircle," units")
#elif(inp == 3):
 #   baseRectangle = float(input("Enter the base value of rectangle: "))
 #   heightRectangle = float(input("Enter the height value of the rectangle: "))
 #   areaRectangle = heightRectangle * baseRectangle
 #   print("Area of Rectangle is: ",areaRectangle," units")
#else:
 #   print("Invalid input!!! Please choose carefully!")


 #_______________________________________________________________________________


# Write a program to do addition of two numbers. Take input from user.

# number1 = int(input("Enter first number to be added: "))
# number2 = int(input("Enter second number to be added: "))
# sumOfTwo = number1 + number2
# print("Sum of given numbers is ",sumOfTwo)

#_____________________________________________________________

# Write a program to compute prime factors of and integer.

# number = int(input("Enter an integer: "))
# print("Factors are: ")
# i=1
# while(i<=number):
#    k=0
#    if(number%i==0):
#        j=1
#        while(j<=i):
#            if(i%j==0):
#                k = k + 1
#            j = j + 1
#        if(k==2):
#            print(i)
#    i = i + 1

#________________________________________________________________________

# WAP to show use of eval function

# print("What is your name?")
# name = input(">")
# print("\nWhen were you born? ")
# birthyear = eval(input(">"))
# print("\nHi %s! You are %d years old"%(name, 2020-birthyear))

#_______________________________________________________________________

# Write a program to convert month into days and days into month

# numOfDaysIn = int(input("Enter number of days: "))
# months = numOfDaysIn / 30
# days = numOfDaysIn % 30
# print("Months= %d, Days= %d"%(months, days))

#_____________________________________________________________

# Write a program to check whether a number is prime or not.
number = int(input("Enter a number: "))
if number > 1:
    for num in range(2,number):
        if(number % num)==0:
            print(number," is not a prime number")
            print(num," times ",number//num," is ",number)
            break
        else:
            print(number," is a prime number.")
else:
    print(number," is not a prime number. ")
    
