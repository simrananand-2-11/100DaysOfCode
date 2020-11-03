# List, Tuples, dictionaries
# WAP to find min and max value from list of tuples.
'''
test_list = [(2,3),(4,7),(8,11),(3,6)]
print("The original list is: "+ str(test_list))
res1 = min(test_list)[0],max(test_list)[0]
res2 = min(test_list)[1],max(test_list)[1]

print("The min and max of index 1: "+str(res1))
print("The min and max of index 2: "+str(res2))
'''
#__________________________________________________________________________________
#WAP to remove matching tuples
'''
test_listA = [('Man','is'),('Man','goes'),('to','garden')]
test_listB = [('Man','is'),('Man','goes'),('Fruit','Garden')]
print("The original list 1: "+str(test_listA))
print("The original list 2: "+str(test_listB))

res = [sub for sub in test_listA if sub not in test_listB]

print("The filtered list of tuple: "+str(res))
'''
#__________________________________________________________________________________
# WAP to count tuples occurrence in list of tuples.
'''
from collections import Counter
from itertools import chain
Input = [('a','b')],[('c','d')],[('w','r')],[('a','b')],[('w','r')]
Output = Counter(chain(*Input))
print(Output)
'''
#______________________________________________________________________________
# WAP to Swap the First and Last Value of a List.
'''
def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
newList = [23,23,-2,33,-345,12,-21]
print("List before swap:"+str(newList))
print("List after swap is: "+str(swapList(newList)))
'''
#______________________________________________________________________________________
# WAP to Find the Intersection of Two Lists.
'''
def intersection(list1,list2):
    list3 = [value for value in list1 if value in list2]
    return list3
list1=[1,6,8,90,23,-6.89,'a','b','f']
list2 = [1,6,7,33,-97,'a','f',-6.89]
print(list1)
print(list2)
print(intersection(list1,list2))
'''
#________________________________________________________________________________
# Write a program to Print Largest Even and Largest Odd Number in a List.
'''
n = int(input("Enter the number of elements in the list: "))
b=[]
for i in range(0,n):
    a=int(input("Enter elements: "))
    b.append(a)
c=[]
d=[]
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()

count1=0
count2=0

for k in c:
    count1 = count1 + 1
for j in d:
    count2 = count2 + 1
print("Largest even number is: ",c[count1-1])
print("Largest odd number is: ",d[count2-1])
'''
#_________________________________________________________________________
# Write a program to Remove the Duplicate Items from a List.
'''
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate =[2,4,10,20,5,2,20,56,932,987,343]
print(duplicate)
print(Remove(duplicate))
'''
#________________________________________________________________________________
# Write a program to Form a Dictionary from an Object of a Class.
'''
class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = "Green"
    def do_nothing(self):
        pass
test = dictObj()
print(test.__dict__)
'''
#_____________________________________________________________________________________
# Write a program to Multiply All the Items in a Dictionary.
'''
trial_dict = {'data1':100, 'data2':-54,'data3':247}
result=1;
for key in trial_dict:
    result = result*trial_dict[key]

print(result)
'''

#_______________________________________________________________________________
# WAP to Concatenate Two Dictionaries into One.
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
'''

#_____________________________________________________________________________
# WAP to Remove the Given Key from a Dictionary
my_dict = {'a':1,'b':2,'c':3,'d':4}
print("Before deletion: ",my_dict)
if 'a' in my_dict:
    del my_dict['a']
print("After deletion: ",my_dict)
