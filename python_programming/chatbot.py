# Chatbot
# Author: Harry
# Mrs. Ubial's Birthday

import random

# 1. Greets the user
print("Hello there!")

# 2. Asks them, "how are you?" or something like it
print("How are you doing?")
user_feeling = input().strip(",.?! ").lower()

# 3. Responds with a general statement
#       that is randomly chosen
#         - create a list of possible responses
#         - randomly choose a response
#         - print that response

good_possible_resp = [
    "I'm really happy for you.",
    "That's really good news!!",
    "That's awesome.",
]
bad_possible_resp = [
    "Im really sorry about that",
    "IDC"
]

if user_feeling == "good" or user_feeling == "great":
    chosen_response = random.choice(good_possible_resp)
    print(chosen_response)
elif user_feeling == "bad" or user_feeling == "not too good":
    chosen_bad_response = random.choice(bad_possible_resp)
    print(chosen_bad_response)
else:
    print("Thanks for sharing that with me.")

# 4. Says goodbye
print("Well thank you for your time! 😊")