# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:39:44 2018

@author: nitingera
"""

def greetingEnglish():
    print("Greeting and salutations")
    return

greetingEnglish()

def GreetMe(str):
    print("You are wonderful", str)
    return

GreetMe("Nitin")

def GreetTwoPeople(person1 = "Nitin", person2 = "Devesh"):
    print("Hello", person1)
    print("How are you", person2)
    return

GreetTwoPeople("Gera")

def Employee(name, *other):
    print("Employee info:")
    print("Name:", name)
    for x in other:
        print(x)
    return

Employee("Nitin", "Very Itelligent", "Going soon", "working in NCW")