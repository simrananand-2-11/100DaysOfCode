# WAP to perform exception handling for Divide by zero Exception.
'''
try:  
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
except:  
    print("Can't divide with zero")

'''
#______________________________________________________________________________
# WAP to perform exception handling operation.

'''
# Program to handle multiple errors with one except statement 
try :  
    a = 3
    if a < 4 : 
  
        # throws ZeroDivisionError for a = 3  
        b = a/(a-3) 
      
    # throws NameError if a >= 4 
    print ("Value of b = ", b)
  
# note that braces () are necessary here for multiple exceptions 
except(ZeroDivisionError, NameError): 
    print ("\nError Occurred and Handled")
'''
#______________________________________________________________________________
# WAP to create user defined Exception.
'''
class YourException(Exception):
  def __init__(self, message, level):
    self.message = message
    self.level = level
 
try:
  raise YourException("Something is fishy", "Level 5")
 
except YourException as err:
  # perform any action on YourException instance
  print("Message:", err.message)
  print("Difficulty Level: ", err.level)
'''
#___________________________________________________________________________________
# WAP to show use of assert in exception.
def dividing(num1, num2):
   assert num2 > 0 , "Divisor cannot be zero"
   return num1/num2
# calling the divide function
a1 = dividing(12,3)
# print the quotient
print(a1)
# this will give the assertion error
a2 = dividing(12,0)
print(a2)
