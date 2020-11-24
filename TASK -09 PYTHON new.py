#!/usr/bin/env python
# coding: utf-8

# Task:9
# Ask 2 numbers from users and store it in num1 and num2
# Ask user to press 1 for addition,2 for subtraction,3 for multiplication and 4 for division
# based on number given by user do the math operation
# 
# 

# In[4]:


press=input('enter the press(1/2/3/4);')
num1=int(input('enter the value of num1;'))
num2=int(input('enter the value of num2;'))
if press=='1':
    print(num1 + num2)
elif press=='2':
    print(num1 - num2)
elif press=='3':
    print(num1 * num2)
elif press=='4':
    print(num1 / num2)
else:
    print('invalid syntex')

