# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:59:17 2019

@author: AShete
"""

# implementation of switch case 


# Using Dictionary

def add_nums(a,b):
    return a+b

def sub_nums(a,b):
    return a-b

def mul_nums(a,b):
    return a*b

def div_nums(a,b):
    return a/b

def default():
    return "Invalid Input !"


switcher={
        1:add_nums(10,20),
        2:sub_nums(30,20),
        3:mul_nums(5,5),
        4:div_nums(25,5),
        5:default()
        }

def switch(key):
    return switcher.get(key,default)

print("Result : ",switch(6))

# Simple switch case

print("## Mathematical Operations ##")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice=input("Enter your choice (1|2|3|4):  ")

num1=int(input("Enter 1st Number : "))
num2=int(input("Enter 2nd Number : "))

if choice=="1":
    result=add_nums(num1,num2)
    print("Result : ",result)
elif choice=="2":
    result=sub_nums(num1,num2)
    print("Result : ",result)
elif choice=="3":
    result=mul_nums(num1,num2)
    print("Result : ",result)
elif choice=="4":
    result=div_nums(num1,num2)
    print("Result : ",result)
else:
    print("Invalid Input !")    

