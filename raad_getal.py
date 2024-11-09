import random


def raad_getal():
    print("Welkom bij het Getallen Raadspel!")
    getal = random.randint(1, 10)
    pogingen = 5

    while pogingen > 0:
        try:
            gok = int(input(f"Raad een getal tussen 1 en 10 (je hebt nog {pogingen} pogingen): "))

            if gok < getal:
                print("Hoger! Probeer het nog eens.")
            elif gok > getal:
                print("Lager! Probeer het nog eens.")
            else:
                print(f"Gefeliciteerd! Je hebt het getal {getal} geraden!")
                return

            pogingen -= 1
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")

    print(f"Oeps! Je pogingen zijn voorbij. Het juiste getal was {getal}.")

if __name__ == "__main__":
    raad_getal()