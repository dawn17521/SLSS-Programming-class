# Tip Calc
# Author:Harry
#  Feb. 28. 2024

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    # Note: This is one way to round a number to two decimal places
    print(f"Leave ${round(tip, 2)}")


def dollars_to_float(d) -> float:
    return float(d)


def percent_to_float(p) -> float:
    return float(p) / 100


main()