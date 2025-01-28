def greet():
    """
    - Prints a basic greeting message.
    - Calls greet_morning to continue the chain.
    """
    print("Hello! Welcome to the greeting chain.")  # First greeting
    greet_morning()  # Call the next function

def greet_morning():
    """
    - Prints a 'Good morning' message.
    - Calls greet_evening to continue the chain.
    """
    print("Good morning! Have a great start to your day.")  # Morning greeting
    greet_evening()  # Call the next function

def greet_evening():
    """
    - Prints a 'Good evening' message.
    - Ends the chain here.
    """
    print("Good evening! Have a restful night.")  # Evening greeting

# ---------------------------------------------------------------
# Start the chain by calling greet.
# ---------------------------------------------------------------
greet()
print("End of script. All functions in the chain have been executed.")