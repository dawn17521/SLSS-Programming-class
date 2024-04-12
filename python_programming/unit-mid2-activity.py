# title: mid2-activity
# Author: Harry
# Date: Apr 8

def calculatearea(rad):
    pi = 3.14159
    area = pi * rad ** 2
    return area

def multiples(num):
    print(f"Multiples of {num}:")
    for i in range(1, 11):
        print(num * i)

def main(rad):
    ar = calculatearea(rad)
    print(f"Area of circle with radius {rad}: {ar}")

    multiples(3)

main(int(input("Enter the radius ")))