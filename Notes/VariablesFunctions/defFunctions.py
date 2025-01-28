# main.py - A script to demonstrate the concept of
# functions: reusable blocks of code. Functions 
# help us organize our code and avoid repetition.
 
# ------------------------------------------------
# 1) A Simple Function.
#   - This function doesn't take any parameters.
#   - It simply prints "Hello, World!" to console.
 
def greet():
    print("Hello, World!") 
 
# Let's call it:
greet()
 
# ------------------------------------------------
# 2) A Function with Parameters.
#   - This function takes strings as parameter.
#   - It prints a personalized greeting message.
 
def greet_person(name):
    print("Hello, " + name + "!")
 
# Let's call it:
greet_person("Alice")