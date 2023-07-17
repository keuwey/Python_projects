# Creating a Python Chatbot

# Importing the necessary libraries
import re
import random


# Defining the greeting function
def greeting(sentence):
    # Creating a list of greetings
    greetings = ["hello", "hi", "hey", "hola", "greetings", "wassup"]

    # Creating a list of responses
    responses = ["hey there!", "hello!", "hi there!", "howdy!", "heyy!"]

    # Checking if the user input contains a greeting
    for word in sentence.split():
        if word.lower() in greetings:
            # Returning a random response
            return random.choice(responses)


# Defining the goodbye function
def goodbye(sentence):
    # Creating a list of goodbye statements
    goodbye_statements = ["goodbye", "bye", "see you later", "see ya"]

    # Creating a list of responses
    responses = ["See you later!", "Bye!", "Have a nice day!", "Take care!"]

    # Checking if the user input contains a goodbye statement
    for word in sentence.split():
        if word.lower() in goodbye_statements:
            # Returning a random response
            return random.choice(responses)


# Defining the response function
def response(user_input):
    # Creating a list of responses
    responses = [
        "I'm sorry, I don't understand.",
        "Can you please explain that in more detail?",
        "What do you mean?",
        "I'm not sure I understand.",
    ]

    # Returning a random response
    return random.choice(responses)


# Creating an infinite loop
while True:
    # Taking user input
    user_input = input("User: ")

    # Checking if the user input is a greeting
    if greeting(user_input) != None:
        print("Chatbot: " + greeting(user_input))
    # Checking if the user input is a goodbye
    elif goodbye(user_input) != None:
        print("Chatbot: " + goodbye(user_input))
    else:
        print("Chatbot: " + response(user_input))
