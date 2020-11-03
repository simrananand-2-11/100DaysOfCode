# Write a program to create a file and store given text and calculate
# total number of words in text and display it on shell.
# file = open("data.txt", "r")
# data = file.read()
#words = data.split()
#print('Number of words in text file :', len(words))


#______________________________________________

# Write a program to store content of two file into one file and count
# total numbers of character in file and display it.
data = data2 = " "
with open('file1.txt') as fp:
    data = fp.read()
with open('file2.txt') as fu:
    data2 = fu.read()

data += "\n"
data += data2
with open('file3.txt','w') as fe:
    fe.write(data)
    
