#!/usr/bin/python3

"""
Concept: Function with parameters (arguments)
"""


def personalized_greeting(name, quest): {
    print(f"Welcome {name}. Lets begin Python Quest: {quest}!")
    }
                                         

name = input("Please enter your name:")
quest = input("Now please enter your Python Quest:")



personalized_greeting(name, quest)
