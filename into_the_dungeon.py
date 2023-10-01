import re
import time


#Defining player name
name = input("Welcome Adventurer, to The Dungeon!\nFirst off, may I ask your name?\n")

#Defining sleep function
def sleep(sec):
    time.sleep(sec)

sleep(1)

#Asking the player his name
if name == "no":
    print("Please don't be difficult, I'm this is me working right now. Name, please")
elif (name is None):
    print("Please don't be difficult, I'm this is me working right now. Name, please")
else:
    print(name + ", Wonderful! What a grand name, not stupid at all.")

sleep(1)

role = input("Now, let's begin, first, choose a class: fighter, wizard, or crackhead?\n")

role = role.casefold()

#Asking the player his role
match role:
    case "wizard":
        print("Ah, so the spell slinging wizard, wise choice, or so, we shall see.")
    case "fighter":
        print("Sturdy and deadly. Rational features to carry.")
    case "crackhead":
        print("Addiction is just the beginning of your woes.")

sleep(1)


#Asking the player his race
race = input("Now, please select your race... are you a lizard, an elf, or a motherfucking LIVING CHANISAW?!\n")

race = race.casefold()

match race:
    case "lizard":
        print("Slithery, brutal, and dumb as shit, this lizard dominates nature, and certain segments of the natural world.")
    case "elf":
        print("Nature good. Natural world bad. Make the world better by killing racist humans. Your forest shall encroach all.")

chainsaw = "chainsaw"

if "chainsaw" in race:
    print("You are chaos. You live for destruction. Viewer discretion is advised.")

print("Now, our story begins in the Old Town of Barley Hump.")

