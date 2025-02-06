# --------------------------------------------------------------------------------
# Simulating a conversation between two persons using functions with arguments.
# --------------------------------------------------------------------------------

def start_conversation(person1, person2):
    """
    - Prints a greeting from person1 to person2 and "ask_question" to continue.
    """
    print(f"{person1}: Hi {person2}! How are you doing today?")
    ask_question(person2, person1)  # Pass the names in reverse order to simulate a reply

def ask_question(person1, person2):
    """
    - person1 asks person2 a question and "give_answer" to continue the.
    """
    print(f"{person1}: I'm good, {person2}! What are your plans for the weekend?")
    give_answer(person2, person1)  # Pass the names in reverse order to simulate a response

def give_answer(person1, person2):
    """
    - person1 gives an answer to person2's question.
    """
    print(f"{person1}: I’m planning to go hiking, {person2}. What about you?")

start_conversation("Alice", "Bob")
print("End of conversation. The simulation is complete.")
