# Vítejte v programu: Lehka kalkulacka
import math


# Tady definujeme scitani
def add(x, y):
    return x + y


# Tady definujeme odcitani
def subtract(x, y):
    return x - y


# Tady definujeme nasobeni
def multiply(x, y):
    return x * y


# Tady definujeme deleni
def divide(x, y):
    return x / y




# Tady definujeme fuknci faktorial
def factorial(x):
    return math.factorial(x)


print("Vyber si operaci:")

print("1.Scitani")

print("2.Odcitani")

print("3.Nasobeni")

print("4.Deleni")

print("5.Faktorial")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Vloz prvni cislo: "))
        num2 = float(input("Vloz druhe cislo: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))


        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        if choice in ('4'):

            if num2 == 0:
                print("Nemuzes delit nulou, zkus to znovu! xd")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))

    if choice in ('5'):

        num3 = int(input("Vloz  cislo: "))
        if num3 < 0:
            print("Nedefinovano, musis zadat kladne cislo!")


        else:

            print(num3, '!', '=', factorial(num3))

        next_calculation = input("Chces pokracovat v kalkulaci?? (y/n): ")

        if next_calculation == "n":
            break


    else:
        print("Invalid Input")
