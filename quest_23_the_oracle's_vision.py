#!/usr/bin/python3
"""
Concept: Function that returns a value

"""


def calculate_area(length, width): 
        area = length * width
        print(f"The Area is {area}")
        

length = float(input("Enter the length of your quadrant:"))
width = float(input("Enter the width of your quadrant:"))


calculate_area(length, width)
