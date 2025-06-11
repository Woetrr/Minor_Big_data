# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:57:41 2025

@author: woute
"""

cal = 160.0 / 3 
fat = 7.0 / 3
sodium = 0.190 / 3
protein = 2.0 / 3
  
cookies = int(input("How many cookies have you eaten today? ")) #input how many coookies you eat

#multiply the nutritional values with the amount
cal = cal * cookies
fat = fat * cookies
sodium = sodium * cookies
protein = protein * cookies

#print the values
print("You have consumed the following nutritional values:")
print(f"Calories: {cal:.2f}")
print(f"Fat: {fat:.2f}")
print(f"Sodium: {sodium:.2f}")
print(f"Protiens: {protein:.2f}")

if cal > 400: # if the colorie intake is to high print the warning
    print("Warning! you should stop eating so many cookies!")