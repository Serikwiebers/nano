import random

# Functie om woorden uit een tekstbestand te importeren
def importeer_woorden(bestandsnaam):
    try:
        with open(bestandsnaam, 'r') as bestand:
            woorden = [regel.strip() for regel in bestand if regel.strip()]
            return woorden
    except FileNotFoundError:
        print(f"Fout: Het bestand '{bestandsnaam}' kon niet worden gevonden.")
        return []
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")
        return []

# Functie om de Hangman tekening te maken
def teken_hangman(pogingen):
    if pogingen == 6:
        print(" +---+")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("=========")
    elif pogingen == 5:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("     |")
        print("     |")
        print("     |")
        print("=========")
    elif pogingen == 4:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("     |")
        print("=========")
    elif pogingen == 3:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("     |")
        print("=========")
    elif pogingen == 2:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\\  |")
        print("     |")
        print("     |")
        print("=========")
    elif pogingen == 1:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\\  |")
        print("/    |")
        print("     |")
        print("=========")
    elif pogingen == 0:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\\  |")
        print("/ \\  |")
        print("     |")
        print("=========")

# Functie voor het Hangman spel
def hangman():
    print("Welkom bij Galgje!")
    print("Raad het woord door één letter per keer te raden. Je hebt 6 pogingen.")

    woorden = importeer_woorden("woorden.txt")  # Woorden importeren uit het bestand
    if not woorden:
        print("Er zijn geen woorden beschikbaar om te spelen.")
        return

    gekozen_woord = random.choice(woorden)  # Kies een willekeurig woord
    geraden_letters = []  # Lijst om de geraden letters op te slaan
    pogingen = 6  # Aantal pogingen dat de speler heeft
    gewonnen = False  # Variabele om bij te houden of het spel gewonnen is

    while pogingen > 0 and not gewonnen:
        teken_hangman(pogingen)  # Toon de huidige staat van de galg
        huidige_status = ''.join(letter if letter in geraden_letters else '_' for letter in gekozen_woord)
        print(f"Huidige status: {huidige_status}")

        if '_' not in huidige_status:  # Controleer of het woord volledig geraden is
            gewonnen = True
            break

        gok = input("Raad een letter: ").lower()  # Vraag de speler om een letter te raden

        if len(gok) != 1 or not gok.isalpha():
            print("Voer alstublieft één letter in.")
            continue

        if gok in geraden_letters:
            print("Je hebt deze letter al geraden.")
            continue
        elif gok not in gekozen_woord:  # Letter zit niet in het woord
            pogingen -= 1
            geraden_letters.append(gok)
            print(f"Oeps! De letter '{gok}' zit niet in het woord. Je hebt nog {pogingen} pogingen over.")
        else:  # Letter zit in het woord
            geraden_letters.append(gok)
            print(f"Goed gedaan! De letter '{gok}' zit in het woord.")

    # Eindresultaat
    if gewonnen:
        print(f"Gefeliciteerd! Je hebt het woord '{gekozen_woord}' geraden!")
    else:
        teken_hangman(pogingen)
        print(f"Jammer, je hebt verloren. Het juiste woord was '{gekozen_woord}'.")

# Start het spel wanneer het script wordt uitgevoerd
if __name__ == "__main__":
    hangman()
