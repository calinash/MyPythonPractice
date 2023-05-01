# name = "Cali"
# age = 21
# attractive = True
#
# print(name)
# print(age)
# print(attractive)
#
# name, age, attractive = "Cali", 21, True
# print(name)
#
# # Cali = 21
# # Sam= 21
# # Sidney= 21
#
# Cali = Sam = Sidney = 21
#
# print(Sidney)
# print(Sam)
# print(Cali)
#
# # String Methods
# # length
# name = "Cali"
# print(len(name))
# # Find a character
# print(name.find("C"))
# # Capitalize/lowercase
# print(name.capitalize())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
# print(name.replace("a", "o"))
# print(name * 3)


# String Spacing
# #1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
# #Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
#
# #Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are

# \n - new line
# \t - tab
# \t\t - double tab
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a "
#       "diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
# import datetime
# now = datetime.datetime.now()
# print("The current date and time is " + now.strftime("%Y-%m-%d %H:%M:%S "))

# Write a Python program that calculates the area of a circle based on the radius entered by the user. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# area = pi(rsqrd)

# from math import pi
# r = float(input("What is the radius of a circle?: "))
# area = float(pi * (pow(r, 2)))
# print("The area of the circle is " + str(area))

# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# first_name = str(input("What is your first name?: "))
# last_name = str(input("What is your last name?: "))
# name = str(last_name) + str(" ") + str(first_name)
# print(name)
# # reversed_name = name[::-1]
# # print(reversed_name)


# Type Casting
import json


# x = 1
# y = 2.0
# z = "3"
# print(y)
# print(int(y))
# y = int(y)
# print(y)
# # String is needed to display:
# print("Y is " + str(y))

# #User input and input function
# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))
# age = age + 1
# print("Hello " +name)
# print("You are "+str(age)+" years old")
# print("You are " +str(height)+ " inches tall")

# import math
# #
# pi = 3.14
# # x = 1
# # y = 2
# # z = 3
# print(round(pi))
# print(math.ceil(pi))
# print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(pi))
# print(max(x, y, z))
# print(min(x, y, z))

# String Slicing = creating substring by extracting elements from another string indexing[] or slice()
# [start;stop;step]
# name = "Cali Bruns"
# first_name = name[0:4]
# # first_name = name[:4]
# last_name = name[5:10]
# # last_name = name[:10]
# funky_name = name[::2]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website = "https://www.google.com"
# website_2 = "https://www.microsoft.com"
# slice = slice(12, -4)
# print(website[slice])
# print(website_2[slice])

# if statements
# Order matters here- executes in order
# age = int(input("How old are you?: "))
# if age == 100:
#     print("You are a century old!")
# elif age>= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")

# name = "Sam"
#
# if name == "Cali":
#     print("That is my name!")
# elif name == "Sam":
#     print("That is my husband!")
# else:
#     print("That is my mom")

# logical operators (and, or, not) used to check if two or more conditional statements
# temp = int(input("What is the weather like outside?: "))
# if temp >= 0 and temp <= 30:
#     print("The temperature is good today; go outside")
# elif temp < 0 or temp > 30:
#     print("The temperature is bad; stay inside!")
# if not temp >=0 and temp<= 30:
# print("The temperature is bad; stay inside:)
# elif not temp <0 or temp >30:
# print("The temperature is good; go outside:)

# while loops a statement that will execute it's block of code as long as its condition remains true
# while 1==1:
#     print("help im stuck in a loop!")
# name = ""
# while len(name) ==0:
#     name = input("Enter your name: ")
# print("Hello "+name)
# #Another Example same thing
# name = None
# while not name:
#     name = input("Enter you name: ")
# print("Hello "+name)

# Write a Python program to display the first and last colors from the following list.
# SAM DID THIS
# colorList2 = '{"name":"sam", "last": "bruns"}'
# colorList = json.loads(colorList2)
# color_list = ["Red", "Green", "White", "Black"]
# color_list_1 = color_list[0] + " " + color_list[len(color_list) - 1]
# print(colorList["name"])
#
#
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)

# website = "https://www.google.com"
# website_2 = "https://www.microsoft.com"
# slice = slice(12, -4)
# print(website[slice])
# print(website_2[slice])

# color_list = ["Red", "Green", "White" , "Black" ]
# # slice = slice(1,-1)
# # print(color_list[slice])
# print(color_list[0] + " " + color_list[-1])


# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. Go to the editor
# The second line splits the string of numbers into a list of individual numbers using the split() method and assigns it to the variable 'list'.
# This method takes a separator as input, in this case ',' (comma) and returns a list of substrings that were separated by the separator.
# Sample data : 3, 5, 7, 23
# Output :
# values = input("Choose four numbers separated by commas: ")
# list = values.split(",")
# # tuple = tuple(list)
# # print(tuple)
# print(list)
# print(min(tuple))
# print(max(list))

# answer = input("What is your name?: ")
# print("Hello " + answer)

# for loops= a statement that will execute its block of code in a limited amount of time
# while loop- unlimited; for loop- limited

# for i in range(10):
#     print(i)
# for i in range(50,100+1,2):
#     print(i)
# for i in "Cali Bruns":
#     print(i)
# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# nested loops = the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop'
# row = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(row):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# Loop Control Statements= change a loop execution from its normal sequence
# Break = terminates loop
# Continue = skips to the next iteration
# Pass = does nothing; place holder
# stops while loop
# while True:
#     name = input("What is your name?: ")
#     if name != "":
#         break
# phone number with a character
# phone_number = "317-496-6047"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")
# skipping 13
# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i, end="")
# list = used to store multiple items in a single variable
# food = ["pizza", "pasta", "fish", "beef"]
# food.append("ice cream")
# food.remove("pasta")
# # food.pop()  removes last value
# food.insert(0, "cake")
# # food.sort() sorts in alphabetical order
# food.clear (removes everything in a list)
# for x in food:
#     print(x)

# 2D lists = a list of lists
# drinks = ["coffee", "tea", "water"]
# dinner = ["mashed potatoes", "mac and cheese", "steak"]
# dessert = ["cake", "candy", "whipped cream"]
# food = [drinks, dinner, dessert]
# print(food)
# print(food[2])
# print(food[2][2]) this will return an error because there is no value at index 2 of 2

# tuple = collections that are ordered and unchangeable
# student = ("Cali", 27, "female")
# # print(student.count("Cali"))
# # print(student.index("Cali"))
# # for x in student:
# #     print(x)
# if "Cali" in student:
#     print("Cali is Here!")

# set = collection that is ordered and unidexed. No duplicate values FASTER THAN LIST
# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}
#
# # utensils.add("napkin")
# # utensils.remove("fork")
# # utensils.clear() clears entire set values
# # utensils.update(dishes) adds two sets together (update)
# # dinner_table = utensils.union(dishes) adds two sets together using new variable (union)
# # print(utensils.difference(dishes)) shows different values in sets
# # print(utensils.intersection(dishes)) shows same variables in set
# # for x in dinner_table:
# #     print(x)

# dictionary = a changeable, unordered collection of unique key: value pairs
# # fast due to hashing , allows quick access
# capitols = {'USA':'Washington DC',
#             'India':'New Dehli',
#             'China':'Beijing',
#             'Russia':'Moscow'}
# capitols.update({'Germany':'Berlin'})
# capitols.update({'USA':'Denver'})
# # capitols.pop('China') removes a key/value from your dict
# # capitols.clear() removes all values from your dict
# # print(capitols["Russia"]) bad way to access key values- use the get method
# # print(capitols.get("Germany")) will return bullion value (True/False)
# # print(capitols.keys())
# # print(capitols.values())
# # print(capitols.items()) prints your key and values in your dictionary
# for key,values in capitols.items():
#     print(key, values)
# another way to print your keys and values of a dict
# indexing [] = gives access to a sequences elements (str,lists,tuple) [start, end, step]*
# name = "cali Nash!"
# # if (name[0].islower()):
# #     name = name.capitalize()
# first_name = name[0:4].upper() will capitalize (.isupper returns bullion value)
# last_name = name[5:-1].lower()  makes lower case (.islower returns bullion value)
# last_character = name[-1]
# print(first_name)
# print(last_name)
# print(last_character)
# functions = a block of code executed only when called

# def Hello(name):
#     print("Hello " + name)
# Hello("Cali")
# my_name = "Cali" you can instantiate a value into a function if it is permanently named and called into the funct
# # name = "Cali"
# Hello(my_name)
# def Hello(first_name, last_name, age):
#     print("Hello " + first_name + " " + last_name)
#     print("You are " + str(age) + " years old.")
# Hello("Cali", "Nash", 27)
# return statements = functions send python values/obj back to their caller- function return values
# def multiply(number_1, number_2):
#     result = number_1 * number_2
#     return result
# print(multiply(6,8))
# # or
# x = multiply(6,8)
# print(x)
# or
# def multiply(number_1, number_2):
#     return number_1 * number_2
# x = multiply(6,8)
# print(x)
# keyword arguments = arguments predicted by an identifier when we pass them into a function; the order of
# arguments doesn't matter unlike positional arguments pythons knows these arguments received by the function
# def hello(first,middle,last):
#     print("Hello " + first+ " " + middle + " " + last)
# hello(last="Cali",first="Alexis",middle="Nash")

# nested function calls= function calls inside other function calls; innermost solved first;
# returned value is used as argument for the next outer function
# number = input("Enter a whole positive number: ")
# number = float(number)
# number = abs(number)
# number = round(number)
# print(number)
# print(round(abs(float(input("Enter a whole positive number: "))))) you can add as many functions as necessary solving innermost to outermost

# Write a Python function to find the maximum of three numbers.
# def maximum(number_1, number_2, number_3):
#     for x in range():
#         max(number_1,number_2, number_3)
# maximum(1,2,3) THIS DOES NOT WORK!!!
# Write a Python function to find the maximum of three numbers.
# def Max_Value(x,y,z) -> int:
#     if x>y>z:
#         return x
#     elif y>x>z:
#         return y
#     else:
#         return z
# print(Max_Value(-1,7,21))
# Write a program to create a function that takes two arguments, name and age, and print their value.
# def name_age(name, age):
#     print("Hello " + name + ".\n" + "You are " + str(age) + " years old.")
# name_age("Cali", 27)
# Write a program to create function func1() to accept a variable length of arguments and print their value.
# def func1(*args):
#     for n in args:
#         print(n)
# func1(20,40,60)
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
# def calculation(a,b):
#     return (a+b),(a-b)
# res = calculation(40,50)
# print(res)

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
# def show_employee(name, salary):
#     print("Employee's Name: " + name)
#     print("Salary: " + str(salary))
# def show_employee(name, salary=9000):
#     print("Employee's Name: " + name +"\nSalary: " + str(salary))
# show_employee("Cali", 120000)
# show_employee("Cali")

# def numb_in_range(n):
#     if n in range(0,10):
#         print(str(n) + " this number is in range.")
#     else:
#         print(str(n) + " this number is not in range.")
#
# numb_in_range(11)

# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself again and again.
# def recursive(samp_list:list) -> int:
#     result = 0
#     if samp_list:
#         result = sum(samp_list)
#         print(result)
#     else:
#         return 0
# recursive({0,1,2,3,4,5,6,7,8,9,10})
# def addition(num):
#     if num:
#         # call same function by reducing number by 1
#         return num + addition(num - 1)
#     else:
#         return 0
# res = addition(10)
# print(res)
# Below is the function display_student(name, age).
# Assign a new name show_student(name, age) to it and call it using the new name.
# def display_student(name,age):
#     print(name, str(age))
# display_student("Cali", 25)
# show_student = display_student
# show_student("Cali", 25)
# have to define new name first because there is no assigned variable to the new name yet

# # Generate a Python list of all the even numbers between 4 to 30
# def evens(samp_list:list):
#     x = 0
#     while x%2 ==0:
#             print({x})
#
#
#
# print(evens(4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30))

# def evens():
#     for x in range(3,31):
#         if x%2:
#             return x
#         else:
#             return 0
# print(evens()) THIS DOESN'T WORK!!!!
# print(list(range(4,30,2)))

# Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# print(max(x))

# Define a function that accepts roll number and returns whether the student is present or absent.
# Sample_Roll = [1,2,3,4]
# def attendance(Sample_Roll: int):
#     Sample_Roll = [1, 2, 3, 4]
#     if Sample_Roll:
#         return True
#     else:
#         return "Absent"
# print(attendance([1])) Doesn't work!!!!

# Define a function that performs max of two and max of three:
# def max_of_two(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# def max_of_three(x,y,z):
#     return max_of_two(x, max_of_two(y, z))
# print(max_of_three(15,25,13))

# def multiply(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total
# print(multiply((1,2,3,4,5,6)))

# def CaseCounter(s):
#     d = {"UPPERCASE": 0 , "LOWERCASE": 0}
#     for c in s:
#         if c.isupper():
#             d["UPPERCASE"] +=1
#         elif c.islower():
#             d["LOWERCASE"] +=1
#         else:
#             pass
#     print("The number of UpperCase values is " + str(d["UPPERCASE"]))
#     print("The number of LowerCase values is " + str(d["LOWERCASE"]))
# CaseCounter("CALI is AwEsOmE")

# def Duplicate_Eliminator(List: list) -> set:
# #     return set(List)
# # print(Duplicate_Eliminator([1,2,3,3,4]))


# for l in "John":
#     if l == "o":
#         pass
#     print(l, end=", ")

# x = 0
# while x<100:
#     x+=2
# print(x)
# This will execute x+=2 until the loop equals 100 and then stops.  This is why the answer is 100

# for num in range(-2,-5,-1):
#     print(num, end=", ")

# numbers= [10,20]
# items = ["Chairs", "Tables"]
# for x in numbers:
#     for y in items:
#         print(x,y)

# x=0
# for j in range(-1,-10,-1):
#     for i in range(10):
#         x += 1
#         print(x)

# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)

# a, b = 12, 5
# if a + b:
#     print('True')
# else:
#   print('False')

# x = 0
# a = 5
# b = 5
# if a > 0:
#     if b < 0:
#         x = x + 5
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

# for num in range(10, 14):
#    for i in range(2, num):
#        if num%i == 1:
#           print(num)
#           break
#
# salary = 8000
# def printSalary():
#     salary = 12000
#     print("Salary:", salary)
#
#
# printSalary()
# print("Salary:", salary)
# var= "James Bond"
# print(var[2::-1])
# p, q, r = 10, 20 ,30
# print(p, q, r)
# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)
# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]
#
# print(listOne == listTwo)
# print(listOne is listTwo)
# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)
#
# calculate(5, 6)
# x = 50


# def fun1():
#     x = 25
#     print(x)
# fun1()
# print(x)
# x = 75
# def myfunc():
#     global x
#     x = x + 1
#     print(x)
#
# myfunc()
# print(x)
# def func1():
#     x = 50
#     return x
# func1()
# print(x)
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615
# answer = input("Choose an integer (n): ")
# print(int(answer) + int((answer*2)) + int((answer*3)))
# THIS WAS THE SAMPLE SOLUTION (Both Work)
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)
# def romanToInt(self, s: str) -> int:
#     ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     res = 0
#     for i in range(len(s)):
#         if i + 1 < len(s) & ROMAN[s[i]] < ROMAN[s[i + 1]]:
#             res -=ROMAN[s[i]]
#         else:
#             res +=ROMAN[s[i]]
#     return res
#
# def testFunc(intList:list) -> int:
#     result = 0
#     for x in intList:
#         if (x % 2) != 0:
#             result += x
#     return(result)
# print(testFunc({1,2,3,4,5,6,7}))

# BMI Calculator

# def BMIcalc(name, height, weight) --> int
#     bmi= weight / (height**2)
#     print("BMI: ")
#     print(BMI)
#     if bmi < 25:
#         return name +
#
#
#
#
#
# print(dict.values)


# class employee:
#     name = ""
#     number = 0
#
# employee1 = employee()
# employee1.name = "Sam"
#
# print(employee1.name)
# Write a Python function to find the maximum of three numbers.
# def Max_Value(x,y,z) -> int:
#     if x>y>z:
#         return x
#     elif y>x>z:
#         return y
#     else:
#         return z
# print(Max_Value(-1,7,21))
# Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# def sum_function(Sum_List: list) -> int:
#     res = 0
#     for x in Sum_List:
#         res += x
#     return res
#  print(sum_function({8,2,3,0,7}))
#  Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
# def mult_funt(samp_list: list) -> int:
#     res = 1
#     for x in samp_list:
#         res *= x
#     return res
# print(mult_funt({8,2,3,-1,7}))

# def greet():
#     print("Hello")
#     print("How Do you Do?")

# def add_numbers(n1, n2):
#     result = n1 + n2
#     print("The sum is", int(result))
# number1 = 5.4
# number2 = 6.7
# add_numbers(number1, number2)

# Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
# def reversed_name(name):
#     return name[::-1]
#
# print(reversed_name("1234abcd"))

# Write a Python function to check whether a number falls within a given range.
# given range 1-10

# def numb_in_range(n):
#     if n in range(0,10):
#         print(str(n) + " this number is in range.")
#     else:
#         print(str(n) + " this number is not in range.")
#
# numb_in_range(11)

# Write a Python function that accepts a string and counts the number of upper and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


# import re

#
# def string_to_count(string):
#     d={"Upper_Case": 0, "Lower_Case": 0}
#     for x in string:
#         if x.islower():
#             d["Upper_Case"]+=1
#         elif x.isupper():
#             d["Lower_Case"]+= 1
#         else:
#             pass
#
#     print(d["Upper_Case"], "letters are lowercase.")
#     print(d["Lower_Case"], "letters are uppercase.")
# string_to_count("The quick Brown Fox")

# scope = The region the variable is recognize
# a variable is only avaialble from inside the region it is created
# global and local variables

# def square_machine(Samp_List: list):
#     i = 0
#     while i < len(Samp_List):

# for i in range(10):
#     if i % 2 == 1:
#         print(i)
# while, for, if, elif, else loops
# i = 1
# while i < 5:
#     i += 1
# print("The End")

# # Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)
# x=1
# for x in range(1500,2701):
#     if x % 7 == 0:
#         if x % 5 == 0:
#             print(x)
# Write a Python program to convert temperatures to and from Celsius and Fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# # 45°F is 7 in Celsius

# def temperature(degrees):
#     result = 0
#     for c in degrees:
#         if
#         f = c * (9 / 5) + 32
#         print("The temperature in Fahrenheit is " + str(f))
#     for f in degrees:
#         c = (f - 32) * (5 / 9)
#         print("The temperature in Celsius is " + str(c))
# temperature(32)
#
# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]
#
# if i_convention.upper() == "C":
#   result = int(round((9 * degree) / 5 + 32))
#   o_convention = "Fahrenheit"
# elif i_convention.upper() == "F":
#   result = int(round((degree - 32) * 5 / 9))
#   o_convention = "Celsius"
# else:
#   print("Input proper convention.")
#   quit()
# print("The temperature in", o_convention, "is", result, "degrees.")

# Write a Python program to guess a number between 1 and 9. Go to the editor
# Note : User is prompted to enter a guess.
# If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

# import random
# random_number, guess_number = random.randint(0,10), 0
# while guess_number != random_number:
#         guess = int(input("Guess a number between 1-9: "))
# print("Well Guessed!")
# Write a Python program to construct the following pattern, using a nested for loop.
# nested loops = the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop'
# row = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(row):
#     for j in range(columns):
#         print(symbol, end="")
#     print()
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# i = 5
# for x in range(i):
#     print("*", end="")
#     for j in range(i):
#         print()
#
# i = 0
# while i<5:
#     print("*", end="")
#     i += 1
#     for i in range(5):
#         for j in range(i):
#             print("*", end="")

# n=5;
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')
#
# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

# Write a Python program to count the number of even and odd numbers in a series of numbers Go to the editor
# # Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# # Expected Output :
# # Number of even numbers : 5
# # Number of odd numbers : 4

# list = [1,2,3,4,5,6,7,8,9]
# even_number = 0
# odd_number = 0
# for x in list:
#     if not x % 2:
#         even_number += 1
#     else:
#         odd_number += 1
# print("The number of odd numbers is " + str(odd_number))
# print("The number of even numbers is " + str(even_number))

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
# for x in range(0,6):
#     if x == 3 or x == 6:
#         continue
#     else:
#         print(x, end="")
# Write a Python program to get the Fibonacci series between 0 and 50. Go to the editor
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
# a,b = 0,1
# while b<50:
#     print(b)
#     a,b = b, a+b

# Write a Python program that accepts a string and calculates the number of digits and letters. Go to the editor
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
# word = input("Enter a string :")
# letters = 0
# numbers = 0
# for x in word:
#     if x.isalpha():
#         letters += 1
#     elif x.isdigit():
#         numbers += 1
#     else:
#         pass
# print("There are " + str(numbers) + " numbers and " + str(letters) + " letters.")

# Write a Python program to check the validity of passwords input by users. Go to the editor
# Validation :
#
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# password = input("Create a password: ")
# cap_letter = 0
# low_letter = 0
# number = 0
# character = 0
# min_length = 0
# max_length = 0
# for x in len(password):
#     if x.isalpha(a-z):
#         pass
#     if x.isdigit(0,9):
#         pass
#     if x.isalpha(A-Z):
#         pass
#     if x.length(6, 16):
#         pass
#     # if x == & or x== * or x== @:
#     #     pass
#     else:
#         print("This password is not applicable try again.. ")
# import re
# p= input("Input your password")
# x = True
# while x:
#     if (len(p)<6 or len(p)>12):
#         break
#     elif not re.search("[a-z]",p):
#         break
#     elif not re.search("[0-9]",p):
#         break
#     elif not re.search("[A-Z]",p):
#         break
#     elif not re.search("[$#@]",p):
#         break
#     elif re.search("\s",p):
#         break
#     else:
#         print("Valid Password")
#         x=False
#         break
#
# if x:
#     print("Not a Valid Password")
# Write a Python program to find numbers between 100 and 400(both included) where each digit of a number is an even number.The numbers obtained should
# be printed in a comma - separated sequence.

# for x in range(100, 401):
#     if x % 2 == 0:
#         print(x, end=", ")
# items = []
# for i in range(100, 401):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
#         items.append(s)
# print( ",".join(items))

# Write a Python program to calculate a dog's age in dog years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:
#
# Input a dog's age in human years: 15
# The dog's age in dog's years is 73

# def dogs_age(age):
#     for x in age:
#         age *= 4
#     print("The dog's age in dog's years is " + str(age))
# dogs_age(15)
# h_age = int(input("Enter a dog's age in human years: "))
# if h_age<=2:
#     d_age = h_age * 10.5
# elif h_age>2:
#     d_age = 21 + (h_age - 2)*4
# print("The dog is " + str(d_age) + " years old")

# Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
# Expected Output:
#
# Input a letter of the alphabet: k
# k is a consonant.

# vowel = ["a", "e", "i", "o", "u", "y"]
# consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", 'r', "s", "t", "v", "w", "x", "z"]
# word = str(input("Enter a letter of the alphabet: "))
# if word in ("a", "e", "i", "o", "u", "y"):
#     print("%s is a vowel." % word)
# else:
#     print("%s is a consonant." % word)


# def add_num(num1, num2):
#     sum = num1 + num2
#     return sum
# def add_num(*args):
#     sum = 0
#     args = list(args)
#     args[0] = 0
#     for i in args:
#         sum += i
#     return sum
# print(add_num(1,2,3,4,5,6))

# **kwargs = parameter that will pack all arguements into a dictionary
# useful so a function can accept a varying amount of keyword arguements
# def hello(first, last):
#     print("Hello " + first + " " + last)
#     print("Hello")
# def hello(**kwargs):
#     print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("hello", end=" ")
#     for key,value in kwargs.items():
#         print(value, end=" ")
# hello(title="Mrs.", first="Cali", second="Alexis", last="Nash")

# str.format = optional method that gives users more control when displaying output
# animal = "cow"
# item = "moon"
# print("The " + animal+" jumped over the " +item)
# print("The {0} jumped over the {1}".format(animal,item))
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))
# print(f"The {animal} jumped over the {item}")
# text = "The {} jumped over the {}"
# print(text.format(animal,item))
# name = "Cali"
# print("Hello, my name is {}".format(name))
# print("Hello my name is {:10}. Nice to meet you.".format(name))
# {:10} - denotes ten spaces in the display of the name
# {:<10}- space to the left
# {:>10}- space to the right
# {:^10}- centers the word with space on either side

# number = 3.14159
# print(f"The nuber pi is {number}")
# print("The number pi is {:.2f}".format(number)) - displays only the first two digits (floating point number)
# number = 1000
# print("The number is {:,}".format(number)) - inserts the comma at 1000
# print("The number is {:b}".format(number)) - displays the number in binary
# print("The number is {:o}".format(number)) - displays octal number
# print("The number is {:x}".format(number)) - hexadecimal (x lowercase or uppercase X)
# print("The number is {:E}".format(number)) - scientific notation

# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)


import math
# pi = 3.1415
# r = float(input("What is the radius of a circle:" ))
# A = (pow(r, 2)*pi)
# print(f"The area of a circle is {A}")

# answer = input("What is your first and last name: ")
# answer = answer[::-1]
# print(answer)
# Write a Python program that accepts a sequence of comma-separated numbers from the user and
# generates a list and a tuple of those numbers.
# list = ['3', '5', '6', '7']
# conversion = tuple(list)
# print(conversion)
# Take a list and return only the odd values as a sum

# for x in list:
#     list = ['3', '4', '5', '6', '7', '8', '9']
#     if x % 2 != 0:
#         result += x

# print(x)
# def odd_numb_sum(intlist:list):
#     result = 0
#     for x in intlist:
#         if (x % 2) != 0:
#             result += x
#     print(result)
#
# odd_numb_sum([3,4,5,6,7,8,9,10])
#
# def addOddNumbers(numbers):
#     print(sum(num for num in numbers if num %2 ==1))
#
# addOddNumbers([3,4,5,6,7,8,9,10])
# def odd_numbs(numbers):
#     result = 0
#     for x in numbers:
#         if (x % 2) != 0:
#             result += x
#     print(result)
# odd_numbs([1,2,3,4,5,6,7,8,9,10])

# Write a program to check whether a person is eligible for voting or not
# Voting requirements: 18 yos; american citizen; do you have your id

# ID = input("Do you have your voter ID? yes or no: " )
# Num = input("Are you 18 or older? yes or no: " )
# Citizenship = input("Are you a US Citizen or have your green card? yes or no: ")
# if ID is True:
#     Continue
# elif ID is False:
#     print("You cannot vote.")

# Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# def sum(numbs):
#     result = 0
#     for x in numbs:
#         result += x
#     print(result)
#
# sum((8,2,3,0,7))

























# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         result = "FizzBuzz"
#         for i in n:
#             if i%3 and i%5:
#                 return "FizzBuzz"
#             elif i%3:
#                 return "Fizz"
#             elif i%5:
#                 return "Buzz"
#             else:
#                 return str(i)


# # f strings
# youtuber = "Cali"
# print("Subscribe to " + (youtuber))
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")
#
