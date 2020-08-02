# Practice problems provided to us by Sir from college and solutions by me
# Very easy problems

# 1. Define a function max() that takes two numbers as arguments and returns the largest of them.
# Use the if-then-else construct available in Python.
#(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)


def maxi(num1,num2):
    if(num1 > num2):
       return num1
    else:
       return num2
print("Enter two numbers")
a = eval(input())
b = eval(input())
maximum = maxi(a,b)
print("Maximum is %d"%maximum)

#____________________________________________________________________________________________________________________________________________________________________

# 2. Define a function max_of_three() that takes three numbers as arguments and returns the largest of them

def max_of_three(num1,num2,num3):
    if ((num1>num2) and (num1>num3)):
        return num1
    elif ((num2>num1) and (num2>num3)):
        return num2
    else:
        return num3

print("Enter three numbers: ")
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
maxi = max_of_three(num1,num2,num3)
print("Maximum is %d"%maxi)

#________________________________________________________________________________________________________________________________________________________________________

# 3. Define a function that computes the length of a given list or string.
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)

count = 0
stri = eval(input("Enter a string: "))
for i in stri:
    count = count + 1
print("Size is %d"%count)


#________________________________________________________________________________________________________________________________________________________________________

# 4.Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise

def check_vowel_true(a):
    if(a=='a' or a=='A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U'):
        return True
    else:
        return False
a = str(input("Enter a character: "))
b = check_vowel_true(a)
print("Value is ", b)

#__________________________________________________________________________________________________________________________________________________________________________
