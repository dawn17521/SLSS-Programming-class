#title : Programming Level 1 and 2
#Author: Harry F
#Data : march 3rd 2024

num = 123
strnum = '123'
print(f"{str(num) + strnum} is '123' + '123'")
print(f"{int(strnum)+ num} is 123 + 123")

user_input = int(input("enter a number that is larger or equal 5: "))

if user_input > 7:
    print(f"{user_input} is larger than 5. You are correct! ")
elif user_input == 7:
    print(f"{user_input} is equal to 5, you are correct! ")
elif user_input < 7:
    print(f"{user_input} is smaller than 5, you are wrong!!!! ")
else:
    print(f"Sorry, i don't know what is {user_input} ")

def main(number : int) -> int:
    user_answer_plus3 = user_input + 3
    print(f"{user_answer_plus3} is the number that has plused to 3")
    return user_answer_plus3
main(user_input)