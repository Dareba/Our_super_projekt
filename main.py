"""
Vitejte v programu Jednoducha kalkulacka.
Uzivatel ma na vyber z peti matematickych operaci.
Program provede matematickou operaci na zaklace volby uzivatele a provede ji s cisly zadanymi uzivatelem.
"""
import math


def add(x, y):
    """
    Tato funkce definuje scitani dvou cisel zadanych uzivatelem.
    @param x: Prvni cislo, ktere uzivatel do programu zada.
    @param y: Druhe cislo, ktere uzivatel do programu zada.
    @return: Provede se soucet zadanych cisel.
    """
    return x + y


def subtract(x, y):
    """
    Tato funkce definuje odcitani dvou cisel zadanych uzivatelem.
    @param x: Prvni cislo, ktere uzivatel do programu zada.
    @param y: Druhe cislo, ktere uzivatel do programu zada.
    @return: Provede se rozdil zadanych cisel.
    """
    return x - y


def multiply(x, y):
    """
    Tato funkce definuje nasobeni dvou cisel zadanych uzivatelem.
    @param x: Prvni cislo, ktere uzivatel do programu zada.
    @param y: Druhe cislo, ktere uzivatel do programu zada.
    @return: Provede se nasobeni zadanych cisel.
    """
    return x * y


def divide(x, y):
    """
    Tato funkce definuje deleni dvou cisel zadanych uzivatelem.
    @param x: Prvni cislo, ktere uzivatel do programu zada.
    @param y: Druhe cislo, ktere uzivatel do programu zada.
    @return: Provede se podil zadanych cisel.
    """

    if y != 0:
        return x / y
    else:
        raise Exception("Nemuzes delit nulou.")


def factorial(x):
    """
    Tato funkce definuje vypocet faktorialu z cisla zadaneho uzivatelem.
    @param x: Cislo, ktere uzivatel co programu zada.
    @return: Provede se vypocet faktorialu zadaneho cisla.
    """
    return math.factorial(x)
if __name__ == '__main__':

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
