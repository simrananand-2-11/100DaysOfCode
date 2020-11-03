# WAP to find out email address of a file
# and count total number of email address using regular expression,
# also find out name starts with S and with A
# Find out Mobile number starts with 99 and 98 and count it.

import re  
f=open("regex2.txt","r")
str1=f.read()
f.seek(0)
print("Content in the File: \n")
print(str1)
strs=str1.split("\n")
desfile=open("correct.txt",'w')
i=0
print("\nCorrect Emails and Mobile Numbers: \n")
while(i!=len(strs)):
    if(re.search('\w+@\w+', strs[i]) or re.search('\d{10}', strs[i])):
        print(strs[i])
        desfile.write(strs[i]+"\n")
    i=i+1
f.close()
desfile.close()
