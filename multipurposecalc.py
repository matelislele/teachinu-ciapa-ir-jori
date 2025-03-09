#padare as

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print("Multi purpose calculator")
print("1. Paprasti skaiciavimai\n2. Kvadrato skaiciavimai\n3. Staciakampio skaiciavimai\n4. Trikampio skaiciavimai\n5. Apskritimo skaiciavimai\n6. Trapecijos skaiciavimai\n7. Exit")
choice = int(input("Pasirinkite skaiciavimo tipa: "))
cls()

if choice == 1:
    num1 = float(input("Iveskite pirma skaiciu: "))
    num2 = float(input("Iveskite antra skaiciu: "))
    print("1. Sudetis\n2. Atimtis\n3. Daugyba\n4. Dalyba")
    choice = int(input("Pasirinkite veiksma: "))
    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        print(num1 / num2)
    else:
        print("Neteisingas pasirinkimas")

elif choice == 2:
    print("Pasirinkite kvadrato skaiciavimo tipa:")
    print("1. Perimetras\n2. Plotas")
    choice = int(input("Pasirinkite veiksma: "))
    if choice == 1:
        num = float(input("Iveskite krastine: "))
        print(num * 4)
    elif choice == 2:
        num = float(input("Iveskite krastine: "))
        print(num ** 2)
    else:
        print("Neteisingas pasirinkimas")

elif choice == 3:
    print("Pasirinkite staciakampio skaiciavimo tipa:")
    print("1. Perimetras\n2. Plotas")
    choice = int(input("Pasirinkite veiksma: "))
    if choice == 1:
        num1 = float(input("Iveskite pirma krastine: "))
        num2 = float(input("Iveskite antra krastine: "))
        print((num1 + num2) * 2)
    elif choice == 2:
        num1 = float(input("Iveskite pirma krastine: "))
        num2 = float(input("Iveskite antra krastine: "))
        print(num1 * num2)
    else:
        print("Neteisingas pasirinkimas")

elif choice == 4:
    print("Pasirinkite trikampio tipą: ")
    print("1. Lygiakraštis\n2. Lygiasonis\n3. Statusis")
    trikampis = int(input("Pasirinkite trikampį: "))

    print("Pasirinkite skaičiavimo tipą:")
    print("1. Perimetras\n2. Plotas")
    skaiciavimas = int(input("Pasirinkite veiksmą: "))

    if trikampis == 1:  # Lygiakraštis
        num = float(input("Įveskite kraštinę: "))
        if skaiciavimas == 1:
            print("Perimetras:", num * 3)
        elif skaiciavimas == 2:
            print("Plotas:", (num ** 2) * 0.433)
        else:
            print("Neteisingas pasirinkimas")

    elif trikampis == 2:  # Lygiasonis
        num1 = float(input("Įveskite vienodąsias kraštines: "))
        num2 = float(input("Įveskite pagrindo kraštinę: "))
        if skaiciavimas == 1:
            print("Perimetras:", num1 * 2 + num2)
        elif skaiciavimas == 2:
            aukstine = (num1**2 - (num2/2)**2) ** 0.5
            print("Plotas:", (num2 * aukstine) / 2)
        else:
            print("Neteisingas pasirinkimas")

    elif trikampis == 3:  # Statusis
        num1 = float(input("Įveskite pirmąją statinę: "))
        num2 = float(input("Įveskite antrąją statinę: "))
        if skaiciavimas == 1:
            hipotenuza = (num1**2 + num2**2) ** 0.5
            print("Perimetras:", num1 + num2 + hipotenuza)
        elif skaiciavimas == 2:
            print("Plotas:", (num1 * num2) / 2)
        else:
            print("Neteisingas pasirinkimas")
    else:
        print("Neteisingas trikampio tipas")
elif choice == 5:
    num = float(input("Iveskite spinduli (pi = 3.14): "))
    print("1. Ilgis\n2. Plotas")
    choice = int(input("Pasirinkite veiksma: "))
    if choice == 1:
        print(2 * 3.14 * num)
    elif choice == 2:
        print(3.14 * num ** 2)
    else:
        print("Neteisingas pasirinkimas")

elif choice == 6:
    print("Pasirinkite trapecijos skaiciavimo tipa:")
    print("1. Perimetras\n2. Plotas")
    choice = int(input("Pasirinkite veiksma: "))
    if choice == 1:
        num1 = float(input("Iveskite pirma krastine: "))
        num2 = float(input("Iveskite antra krastine: "))
        num3 = float(input("Iveskite trecia krastine: "))
        num4 = float(input("Iveskite ketvirta krastine: "))
        print(num1 + num2 + num3 + num4)
    elif choice == 2:
        num1 = float(input("Iveskite pirma krastine: "))
        num2 = float(input("Iveskite antra krastine: "))
        num3 = float(input("Iveskite aukstine: "))
        print((num1 + num2) * num3 / 2)
    else:
        print("Neteisingas pasirinkimas")

elif choice == 7:
    print("Iki pasimatymo!")
    exit()
else:
    print("Neteisingas pasirinkimas")
