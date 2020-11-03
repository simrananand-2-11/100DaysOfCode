# September 1, 2020

# WAP to swap commas and dots in a String.
'''
def ReplaceCommaDot(stringInput):
    maketrans = stringInput.maketrans
    finalResult = stringInput.translate(maketrans(',.','.,'))
    return finalResult
stringInput = "12,34.213,shfjf."
print(ReplaceCommaDot(stringInput))
'''

# WAP to remove ith character from a String.
'''
def remove(string,i):
    for pos in range(len(string)):
        if pos == i:
            string = string.replace(string[i],"",1)
    return string
if __name__ == '__main__':
    string = str(input("Enter a string: "))
    pos1 = int(input("Enter position you want to remove: "))
    actualpos = pos1 - 1
    print(remove(string,actualpos))
'''
# WAP to Find words which are greater than given length k.
'''
def  stringGreaterThanK(stringInput, k):
    outputString = []
    words = stringInput.split(" ")
    for size in words:
        if len(size) > k:
            outputString.append(size)
    return outputString
stringInput = str(input("Enter a string: "))
k = int(input("Enter your limit(greater than which you want to see words): "))
print(stringGreaterThanK(stringInput,k))            
'''
# WAP to remove all duplicates from a given String.
'''
def removeDuplicateFromString(StringInput):
    s = set(stringInput)
    s="".join(s)
    print("Without order: ",s)
    t=""
    for i in stringInput:
        if (i in t):
            pass
        else:
            t = t + i
        print("With order: ",t)
stringInput = str(input("Enter a string: "))
removeDuplicateFromString(stringInput)
'''
# WAP to print total of ASCII character of given string
def AsciiTotalString(stringInput,sumArray):
    length = len(stringInput)
    total = 0
    ActualTotal = 0
    for i in range(length):
        if(stringInput[i] == ' '):
            ActualTotal += total
            sumArray.append(total)
            total = 0
        else:
            total += ord(stringInput[i])
    sumArray.append(total)
    ActualTotal += total
    return ActualTotal
if __name__ == "__main__":
    stringInput = str(input("Enter a string: "))
    sumArray = []
    total = AsciiTotalString(stringInput,sumArray)

    print("Sum of ASCII values of words: ")
    for element in sumArray:
        print(element, end = ' ')
    print()
    print("Total sum: ",total)
