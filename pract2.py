# Write a program to select and print the largest of the three numbers using Nested if else statement

# print("Enter 3 numbers: ")
# num1 = input()
# num2 = input()
# num3 = input()

# if(num1 > num2 and num1 > num3):
#    print(num1," is the maximum")
#elif(num2 > num1 and num2 > num3):
#    print(num2," is maximum")
#else:
#    print(num3," is maximum")

#__________________________________________________________________________

# Grade of student using elif
print("Enter marks of student: ")
marks = int(input())

if(marks<=100 and marks >=81):
    print("Student gets AA grade. Looks like you are really interested in this subject. So, you are following Depth first search approach. Hopefully, you will like rest of subjects too. ;-)")
elif(marks<=80 and marks >=61):
    print("Student gets AB grade. Not bad. Seems like you are following Breadth first search approach. That is nice, one should dive in all subject slightly then take a deep dive later on. :-)")
else:
    print('You got AC. ')
    print("Hmm, looks like you didn't took much interest in subject.")
