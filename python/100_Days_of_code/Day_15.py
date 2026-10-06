# Day 15 - 100 Days of Code Challenge


# create a python program capible of grating with you good morning, good afternoon, and good evning based on the time of the day. Your program should use time module to get the current time

from os import name
import time 
timestamp= int (time.strftime("%H"))
print("current time is " + str(timestamp) + " hours")
if timestamp < 12:
    print("good morning")
elif timestamp < 17:
    print("good afternoon")
else:    print("good evening")

# now i am create a function that will take a name as input and greet the user with good morning, good afternoon, or good evening based on the time of the day.
def greet(name):
    timestamp= int (time.strftime("%H"))
    print("current time is " + str(timestamp) + " hours")
    if timestamp < 12:
        print("good morning " + name)
    elif timestamp < 17:
        print("good afternoon " + name)
    else:    
        print("good evening " + name)
        
        
name = input("enter your name: ")
greet(name)