#title:exercise
#Name:Harry Feng
#date: Feb 12

user_name = input("greeting my friend, what is your name?: ")
print(f"nice name {user_name}")
print()
user_answer_1 = input(f"{user_name}, do you like football? ")
if user_answer_1 == 'no':
    print("good")
elif user_answer_1 == 'No':
    print('Good')
elif user_answer_1 == "NO":
    print("good")
else:
    print("i love football")
user_answer_2 = input(f"{user_name}, do you like pizza? ")
if user_answer_2 == 'no':
    print("good")
elif user_answer_2 == 'No':
    print('Good')
elif user_answer_2 == "NO":
    print("good")
else:
    print("i love pizza")
user_answer_3 = input(f"{user_name}, do you like Genshin Impact? ")
if user_answer_3 == 'no':
    print("good")
elif user_answer_3 == 'No':
    print('Good')
elif user_answer_3 == "NO":
    print("good")
else:
    print("Genshin impact is a good game.")
print()
print(f"is nice to talk to you {user_name}, goodbye")

