
#1
length=int(input("Enter the length: "))
width=int(input("Enter the width: "))
area=length*width
print("The area of the rectangle is: ",area)

#2
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))
BMI=weight/(height*height)
print("Your BMI is ",BMI)

#3
Student={}
n=int(input("Enter the no of students:"))
for i in range(n):
  name=input("Enter your name: ")
  score=int(input("Enter your score: "))
  Student[name]=score
print(Student)

#4
age=int(input("Enter your age:"))
if age<18:
  print("You are a minor")
elif age>=18 and age<60:
  print("You are an adult")
else:
  print("You are a senior")

#5
for i in range(1,51):
  if i%2==0:
    print(i,end=" ")
    i+=1
  else:
    i+=1

#6
correct_password="ABCD@1234"
user_password=input("Enter your password:")
if user_password==correct_password:
  print("You have entered the correct password")
else:
    while user_password!=correct_password:
      print("Please enter the correct password")
      user_password=input("Enter your password:")

#7
def average(aList):
  avg=0
  sum=0
  for i in aList:
    sum+=i
  avg=sum/len(aList)
  return avg

l=[1,2,3,4,5]
avg_of_list=average(l)
print("The average of the given list is: ",avg_of_list)

#8
def vowel_count(word):
  count=0
  for i in range(0,len(word)):
    if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o"or word[i]=="u"or word[i]=="A" or word[i]=="E" or word[i]=="I" or word[i]=="O" or word[i]=="U":
      count+=1
  return count

input_word=input("Enter a word: ")
a=vowel_count(input_word)
print("The number of vowels are: ",a)

#9
import datetime
from datetime import date
from datetime import datetime
Today_date=date.today()
print("Today's date is ",Today_date)
Time=datetime.now()
print("Time is ",Time)

#10
def addition(a,b):
  sums=0
  sums=a+b
  return sums

try:
  num1=int(input("Enter a number: "))
except Exception:
  print("Enter an integer value ")
try:
  num2=int(input("Enter a number: "))
except:
  print("enter an integer value ")

if(type(num1)==int and type(num2)==int):
      print("sum is ",addition(num1,num2))
else:
  print("Enter proper values!!!")

#11
try:
  num1=int(input("Enter a number: "))
except ValueError:
  print("enter an integer value")
try:
  num2=int(input("Enter a number: "))
except ValueError:
  print("enter an integer value")

#12
def division(a,b):
  final=0
  try:
    final=a/b
  except Exception as e:
    print(e)
  return final

a=10
b=0
if(b!=0):
  division(a,b)
else:
  print("Error")

#13
f=open("a.txt",'w')
f.write("Hello,Python!")
f.close()

#14
f=open("a.txt",'r')
print(f.readlines())
f.close()

#15
f=open("a.txt",'w')
f.write("Hello Python!")
f.close()
f=open("a.txt",'a')
f.write("How are you")
f.close()
f=open("a.txt",'r')
print(f.readlines())

