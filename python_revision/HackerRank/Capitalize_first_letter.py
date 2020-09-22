'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.

Sample Input

chris alan

Sample Output

Chris Alan
'''
def solve(s):
    ss = s.split(" ")
    new_string = ""
    for i in ss:
        new_string += i.capitalize() + " "
    return new_string


    
s = input()

result = solve(s)

print(result)

