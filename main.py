"""print("------------------------------------------")

print("PROGRAMS IN FILE HANDLING")


print("------------------------------------------")

print("FIND LONGEST WORD IN A FLE")

print("------------------------------------------")

f1=open("Anshu.py","r")
word=f1.read().split()
print((max(word,key=len)))

print("------------------------------------------")

#to take file name as input from user
fn=input("Enter")
f2=open(fn,"r")
word1=f2.read().split()
print((max(word1,key=len)))

print("------------------------------------------")

print("Display the Frequency OF words From a File")

print("------------------------------------------")

from collections import Counter

fna=input("Enter = ")
f3=open(fna,"r")
data=Counter(f3.read().split())
print(data)

print("------------------------------------------")"""

print("Concatinate every line from first file to the coressponding line of Second File")

print("------------------------------------------")

#from file
f7=open("Anshu.py","r")
f8=open("Aryan.py","r")
for l1,l2 in zip(f7,f8):
    print(l1+l2)


print("------------------------------------------")

#user input
fnam=input("eNTER = ")
fname=input("Enter = ")
f7=open(fnam,"r")
f8=open(fname,"r")
for l1,l2 in zip(f7,f8):
    print(l1+l2)


print("------------------------------------------")

