# enkel räkne maskin med funktioner

def calculator():
    print("välkommen till räknemaskinen")
    print("välj en operation")
    print("1.addition")
    print("2.subtration")
    print("3.multiplikation")
    print("4.division")
    print("5.avsluta")

    while True:
        try:
            choice = int(input("ange val (1/2/3/4/5): "))

            if choice == 5:
                print("avslutar räknemaskinen")
                break

            if choice in [1,2,3,4]:
                num1 = float(input("ange första talet: "))
                num2 = float(input("ange det andra talet: "))

                if choice == 1:
                    print(f"resultat: {num1} + {num2} = {num1 + num2}")
                elif choice == 2:
                    print(f"resultat: {num1} - {num2} = {num1 - num2}")
                elif choice == 3:
                    print(f"resultat: {num1} * {num2} = {num1 * num2}")
                elif choice == 4:
                    if num2 != 0:
                        print(f"Resultat: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Fel: Division med noll är inte tillåten!")
            
            