# WAP to Append, Delete and Display Elements of a List Using Classes.
'''
class MyList:
    def __init__(self):
        self.n = []

    def add(self,a):
        return self.n.append(a)

    def remove(self,b):
        self.n.remove(b)

    def display(self):
        return (self.n)

obj = MyList()

choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    choice = int(input("Enter choice: "))
    if choice == 1:
        n = int(input("Enter number to append: "))
        obj.add(n)
        print("List: ", obj.display())

    elif choice == 2:
        n = int(input("Enter number to remove: "))
        obj.remove(n)
        print("List: ", obj.display())

    elif choice == 3:
        print("List: ", obj.display())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
'''

#_________________________________________________________________________________
# WAP to print average of 10 numbers using class and object.
# Python code to Calculate sum and average of a list of Numbers.
'''
from math import fsum
from statistics import mean


class Sum_avg_of_list(object):
    __b = []
    def __init__(self, a):
        self.a = a

        for i in self.a:
            Sum_avg_of_list.__b.append(float(i))

    def sum_of_list(self):
        return fsum(Sum_avg_of_list.__b)

    def avg_of_list(self):
        return mean(Sum_avg_of_list.__b)


entered_list = input("Enter list separated by space: ").split()

# Create an Object
Object_1 = Sum_avg_of_list(entered_list)

#Call the function using Object

print("Sum of list: ",Object_1.sum_of_list())
print("Average of list: ",Object_1.avg_of_list())
'''

#__________________________________________________________________________
# WAP multiply the positive numbers using single level inheritance.
'''
#Base class
class Parent_class(object):
# Constructor
    def __init__(self, value1,value2):
        self.value1 = value1
        self.value2 = value2

    def multiplication(self) :
        print(" multiplication value1 : " , self.value1)
        print(" multiplication value2 : " , self.value2)
        return self.value1 * self.value2

# derived class or the sub class
class Child_class(Parent_class):
    pass
# Driver code

Object2 = Child_class(20,30)  # parent class object
print(" Multiplied value :" , Object2.multiplication() )
print( " " )
'''
#____________________________________________________________________________________
# WAP to create ATM system to withdraw, debit and check balance using class.

# Python program to create Bankaccount class 
# with both a deposit() and a withdraw() function 
class Bank_Account: 
	def __init__(self): 
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 

	def debit(self): 
		amount=float(input("Enter amount to be Debit: ")) 
		self.balance += amount 
		print("\n Amount Debited:",amount) 

	def withdraw(self): 
		amount = float(input("Enter amount to be Withdrawn: ")) 
		if self.balance>=amount: 
			self.balance-=amount 
			print("\n You Withdrew:", amount) 
		else: 
			print("\n Insufficient balance ") 

	def display(self): 
		print("\n Net Available Balance=",self.balance) 

# Driver code 

# creating an object of class 
s = Bank_Account() 

# Calling functions with that class object 
s.debit() 
s.withdraw() 
s.display() 





