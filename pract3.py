# WAP to do print Fibonacci series of N numbers use concept of command line arguments.
# a=int(input("Enter the terms"))
# f=0                                         
# s=1                                     
# if a<=0:
#    print("The requested series is",f)
# else:
#    print(f,s,end=" ")
#    for x in range(2,a):
#        next=f+s                           
#        print(next,end=" ")
#        f=s
#        s=next


# WAP to print the patter ‘G’

# Python program to print pattern G 
# def Pattern(line): 
#	pat="" 
#	for i in range(0,line):	 
#		for j in range(0,line):	 
#			if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
#				i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2) 
#				and j > line-5 and j < line-1) or (j == line-2 and
#				i != 0 and i != line-1 and i >=((line-1)/2))): 
#				pat=pat+"*"
#			else:	 
#				pat=pat+" "
#		pat=pat+"\n"
#	return pat 
#
# Driver Code 
# line = 7
# print(Pattern(line)) 


# Write a program to print all prime numbers in an interval

# lower = int(input("Enter lower range: "))  
# upper = int(input("Enter upper range: "))  
  
# for num in range(lower,upper + 1):  
#   if num > 1:  
#       for i in range(2,num):  
#           if (num % i) == 0:  
#               break  
#       else:  
#           print(num)  

# WAP to do Sum of squares of first n natural numbers

# def sqsum(n) :
#   sm = 0
#   for i in range(1, n+1) :
#      sm = sm + pow(i,2)
#   return sm
# main
# n = int(input("Enter number upto which you want to see the sum of squares: "))
# print(sqsum(n))


# WAP to check whether given number is Fibonacci number or not?


# import math

# function to check perferct square
# def checkPerfectSquare(n):
#    sqrt = int(math.sqrt(n))
#    if pow(sqrt, 2) == n:
#        return True
#    else:
#        return False

# function to check  Fibonacci number
# def isFibonacciNumber(n):
 #   res1 = 5 * n * n + 4
 #   res2 = 5 * n * n - 4
 #   if checkPerfectSquare(res1) or checkPerfectSquare(res2):
 #       return True
 #   else:
 #       return False

# main code
# num = int(input("Enter an integer number: "))

# checking
# if isFibonacciNumber(num):
 #   print ("Yes,", num, "is a Fibonacci number")
# else:
  #  print ("No,", num, "is not a Fibonacci number")


# WAP to print pyramid of *.
# rows = 5
# k = 2 * rows - 2
# for i in range(0, rows):
#    for j in range(0, k):
#        print(end=" ")
#    k = k - 1
#    for j in range(0, i + 1):
#        print("* ", end="")
#    print("")
    
# k = rows - 2

# for i in range(rows, -1, -1):
#    for j in range(k, 0, -1):
#        print(end=" ")
#    k = k + 1
#    for j in range(0, i + 1):
#        print("* ", end="")
#    print("")

