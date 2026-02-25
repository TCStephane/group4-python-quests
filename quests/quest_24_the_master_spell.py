#!/usr/bin/python3

"""
Concept: Calling a function from within another function
"""


def ask_for_age():
    return int(input("How old are you?"))
    


def can_they_vote(age): 
    if age >= 18:
        print("Register as a voter and vote NOW!!")
    else:
        print("Too young to vote. Try again next year.")

age = ask_for_age()
can_they_vote(age)
