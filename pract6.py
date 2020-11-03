# Write a program to show use of default arguments to calculate area of circle in function.
'''
radius = float(input("Enter radius: "))
def circleArea(radius,pi=3.14):
    area = pi*radius*radius
    return area
print("Area of circle is ",circleArea(radius))
'''
#________________________________________________________________

# Write a program to illustrate the concept of call by value and call by reference.

# Call by value
#string = 'Call her Sunny'
#def test(string):
#    string = 'Madan Mohan'
#    print("Inside function: ",string)
#test(string)
#print("Outside function: ",string)

# Call by reference
#def add_more(list):
#    list.append(50)
#    print("Inside function: ",list)
#myList=[29,32,753]
#add_more(myList)
#print("Outside function: ",myList)

#_________________________________________________________________

# WAP to reverse the digit using function return value from function,
# create module for reverse number
'''
sum1=0
def revDig(num):
    global sum1
    while(num!=0): 
        b=int(num%10)
        sum1=sum1*10+b
        num=int(num/10)
    return sum1
number1=int(input("Enter a number: "))
print(revDig(number1))
'''
#____________________________________________________________________________

# WAP to find out factorial of given number using recursion
# import module of factorial.
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Input a number to compute factorial: "))
print(factorial(n))
'''
#________________________________________________________________________________
# WAP to arrange given number in ascending orders import
# module of ascending order.
'''
def insertion_sort(InputList):
    for i in range(1,len(InputList)):
        j=i-1
        next_element = InputList[i]
# compare the current element with next one
        while(InputList[j]>next_element) and (j>=0):
            InputList[j+1] = InputList[j]
            j = j-1
        InputList[j+1] = next_element
    
x = list(map(int,input("Enter few numbers: ").split()))
insertion_sort(x)
print(x)

'''
#___________________________________________________________________________________
# 
