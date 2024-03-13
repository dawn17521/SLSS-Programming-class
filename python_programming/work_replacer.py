def translate(text: str) -> str:
    text = text.replace("100", "💯")
    text = text.replace("noodles", "🍜")
    return text
#test case
print(translate("i like noodles "))
print(translate("i like 100"))
def main():
    user_input = input("do you like noodles or 100 ")
    print(translate(user_input.strip().lower()))
main()



