skaicius1 = float(input("iveskite skaiciu: "))
skaicius2 = float(input("iveskite skaiciu: "))

operation = str(input("iveskite parinkti (*,/,+,-)"))

if operation == "*":
    s = skaicius1 * skaicius2
    print(s)

elif operation == "/":
    s = skaicius1 / skaicius2
    print(s)

elif operation == "+":
    s = skaicius1 + skaicius2
    print(s)

elif operation == "-":
    s = skaicius1 - skaicius2
    print(s)

else:
    print("tokios parinkties nera")
