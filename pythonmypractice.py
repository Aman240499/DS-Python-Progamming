# -*- coding: utf-8 -*-
"""pythonmypractice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zre_8dQnuU72bWHoGkTOsyMPqiYFbLnF

### ***Using Python as Calculator***
"""



2+2

50-5*6

8/5 #decimal values as output

8//5 #not decimal values

25%6 #reminder

25**2#power

25-6*8/4+(25*2)+5**2
#25*2  50 ,5**2-25 8/4
#25-6*2+50+25
#6*2 12
#25-12+50+25
#88  #bodmas rule follow

width=20
height=2*5
width*height #20*2*5

tax = 12.5 / 100
price = 100.50
price * tax
12.5625

"""## **string**"""



#to print three time "am" followed by  2 time "an"
3*"am" + 2*"an"

#write python by 2 string "py" and "thon"
"py"+"thon"

first_name ="aman"
last_name ="taori"
first_name +" " +last_name

#indexing slicing
#position start with 0
#if we don't know how many element if we want to last element -1

#+---+---+---+---+---+---+
 #| P | y | t | h | o | n |
 #+---+---+---+---+---+---+
 #0   1   2   3   4   5   6
-#6  -5  -4  -3  -2  -1

name = "python"
name[0] #p first element
name[-1] #n last element
name[::-1] #reverse string
name1="ppyytthhoonn"
#print python as output
name1[1::2]

name = "ython"
"p" + name[0:]

"""### **List**"""

squares = [1,4,9,16,25,36]
squares

squares[0]

squares[-1]

squares[::-1]#reverse list

squares[:]#copy of list

squares + [49,64,81,100,121]    #concating in list

cubes = [1,8,27,65,125]
#cube of 4 is 64 but we put 65 so we need to replace so
cubes[3] = 64
cubes

"""append method

"""

#append method to add element at last

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes

#list of string

letters = ["a","b","c","d","e","f","g"]
#replace letter
letters[2:5] #c d e
letters[2:5] = ["C","D","E"]
letters



#remove
letters[2:5] = []
letters



#clear the list by replacing all the elements with an empty list
letters[:] = []
letters

letters = ["a","b","c","d","e","f","g"]
#BUILD IN FUNCTION
#CALCULATE LENGTH OF LIST len()
len(letters)

"""## ***nested list(list inside list)***"""

a = ["a","b","c"]
n = [1,2,3]
listinsidelist = [a,n]
listinsidelist

#another way of creating list
anotherway = list(("aman","sarang","umang"))
print(anotherway)
print(type(anotherway))

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

"""# **ADD ITEMS IN LIST**"""

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"watermelon")
print(thislist)

#extend method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
tropical.extend(thislist)
print(tropical)



"""# *** REMOVE ITEM FROM LIST***"""

name = ["aman","sarang","umang","radika"]
#remove method
name.remove("aman")
print(name)
#remove last item
#use pop() method
name.pop()
print(name)
#del
#remove first element from list
del name[0]
print(name)

"""# **clear the list**"""

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

"""# ***loop list***"""

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

"""# MOST IMPORTANT LIST **COMPREHANSION** 

"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

numbers = [1,2,3,4,5,6,7,8,9,10]
even_number = [x for x in numbers if x%2==0]
print(even_number)

numbers1 = [1,2,3,4,5,6,7,8,9,10]
odd_number = [x for x in numbers1 if x%2 != 0]
print(odd_number)

newlist = [x for x in range(1,10) if x > 5]

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

newlist1 = [x.lower() for x in fruits]
print(newlist1)

newlist2 =[x.title() for x in fruits]
print(newlist2)

newlist3 = [len(x) for x in fruits]
print(newlist3)

"""# **SORT**"""

#ALPHABATICALLY
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort()
print(fruits)

#ARRANGE NUMBER IN ASCENDING ORDER
number = [25,21,45,78,12,16]
number.sort()
print(number)





"""### ***LIST METHOD***"""

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

"""# **TUPLE**"""

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(type(thistuple))

"""## **INDEXING IN TUPLE**"""

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[0])

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[::-1])

"""# **CHANGE TUPLE TO LIST**"""

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
lista = list(thistuple) 
print(lista)

"""# **ADD ITEMS IN TUPLE**

"""

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
y = list(thistuple)
y.append("watermelon")
thistuple = tuple(y)
print(thistuple)

newtuple=(1,2,3,4,5,6,7,8,9)
y = list(newtuple)
y.append(10)
newtuple = tuple(y)
print(newtuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

"""# ***JOIN TUPLE***"""

tuple1 = (1,2,3,4,5,6,7,8,9)
tuple2 =("a","b","c","d","e","f","g","h","i")
tuple3 = tuple1 +tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

























































































































"""# *** Fibonacci series***"""

a, b = 0, 1
while a < 10:
  print(a)
  a , b = b, a+b

i = 256*256
print("the value ofr i is " , i)

"""## IF ***Statement***"""

num = 15
if(num<10):
  print("number is smaller than 10")
else:  
  print("number is greater than 10")

if("java" in ["java","python","c","c++"]):
  print(True)
else:
  print(False)

passing_score = int(input("enter passing_marks :"))
my_score = int(input("Enter my_score : "))
if(my_score >= passing_score):
  print("congraulations !!!")
  print("you have passed exam")
else:
  print("you failed exam")
  print("retest!!!")

"""# ***For Statement***"""

words = ["cat","elephant","dog"]
for i in words:
  print(i,"=",len(i))

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x," " ,len(x))

for x in "banana":
  print(x)

"""# **BREAK IN FOR LOOP**

"""

for x in fruits:
  print(x)
  if(x=="banana"):
    break

for x in fruits:
  if x =="banana":
    break
  print(x)

"""# **CONTINUE STATEMENT**

"""

for x in fruits:
  if x == "banana":
    continue
  print(x)

"""# ***RANGE FUNCTION IN FOR LOOP***

---




---


"""

sum(range(5))



for i in range(1,10): #it will print 1 to 9
  print(i)

for i in range(1,50,3): #in the difference of 3
  print(i)

for x in range(6):
  print(x)
else:
  print("finally finished")

for x in range(6):
  if x==3: break
  print(x)
else:
  print("finally finished")

"""# **ODD EVEN CODE**"""

for i in range(2,10):
  if(i %2 ==0):
    print(i,"is even number")
  else:
    print(i,"is odd number")







"""# **Nested for loop**"""

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x," ",y)

for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement

"""# **definng function**

"""

i = 7

def f(arg=i):
    print(arg)
i = 6    
f()

i="aman"

def f(arg=i):
  print(arg)
i ="pratik"

f()

i = True
def f(arg = i):
  print(arg)
i = False
f()

def f(a, L=[]):
  L.append(a)
  return L
print(f(1))
print(f(2))
print(f(3))

def f(a, L=[]):
  L.append(a)
  return L
print(f(1))
print(f(2))
print(f(3))



"""### ***lambda function***"""

def make_incrementor(n):
  return  lambda x:x+n
f= make_incrementor(42)
f(0)  #f(n)
f(1) #43

def make_decrementor(n):
  return lambda x : x-n
f = make_decrementor(42)
f(0)
f(1)

x = lambda a:a+10
print(x(5))

x = lambda a , b : a * b
print(x(5, 6))

x = lambda a,b,c : a+b+c
print(x(4,6,10))

def myfunc(n):
  return lambda a : a * n

def myfunc(n):
  return lambda a :a * n
func = myfunc(5)
print(func(11))

def myfunc(n):
  return lambda a : a + n
func = myfunc(5)
print(func(5))

def myfunc(n):
  return lambda a:a**n
power = myfunc(5)
print(power(2))

































































































































x = int(input("enter any digit :"))
if (x<0):
  print("negative digit   ",x)
elif(x == 0):
  print("number is : 0")
elif(x == 1):
  print("number is :1")
else:
  print("number is :",x)

















x = int(input())









































































































