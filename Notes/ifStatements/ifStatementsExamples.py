# simple example

import random
 
# Define different weather conditions
w_conditions = ["rainy", "sunny", "cloudy"]
 
# Pick a random value from the above list
weather = random.choice(w_conditions)
 
# Print the random value
print("The weather is " + weather + ".")
 
if weather == "rainy":
    print("Don't forget your umbrella!")



# -------------------------------------------------------------------------------------------------------------------------------


# comparation operators examples

# Define the list of scores
grades = [20, 45, 56, 68, 75, 100]

# Pick a random value from the list
score = random.choice(grades)

# Print the random score
print("Score: " + str(score))

if score >= 60:
    print("Congratulations!")
    print("You passed the exam.")


# ------------------------------------------------------------------------------------------------------------------------------


# else statement example

# Define the range of possible scores
min_score = 20
max_score = 100

# Pick a random score
score = random.randint(min_score, 
                       max_score)

# Print the random score
print("Score: " + str(score))

# Check if score meets the condition
if score >= 60:
    message_1 = "Congratulations! "
    message_2 = "You passed the exam."

else:
    message_1 = "Sorry, you didn't pass."
    message_2 = " Try Again!"

print(message_1 + message_2)


# -------------------------------------------------------------------------------------------------------------------------------


# elif satement example

# Define the range of possible scores
min_score = 20
max_score = 100

# Pick a random score
score = random.randint(min_score, 
                       max_score)

# Print the random score and
# the corresponding Grade

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# ---------------------------------------------------------------------------------------------------------------------------------


# Logical operators examples

# Example No. 1

age = 17
is_student = True

if age < 18 and is_student:
    print("You get a student discount!")

# Example No. 2 ---------------------------------

number = 7

if number % 2 == 0:
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")


# ----------------------------------------------------------------------------------------------------------------------------------------


# nested if statements example

age = 20
citizenship = "US"

if age >= 18:
    if citizenship == "US":
        print("You are eligible to vote.")
    else:
        print("You must be a US citizen to vote.")
else:
    print("You must be at least 18 to vote.")