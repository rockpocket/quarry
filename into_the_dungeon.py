import re
import time

player = input("Welcome Adventurer, to The Dungeon!\nFirst off, may I ask your name?\n")


if player == "no":
    print("Please don't be difficult, I'm this is me working right now. Name, please")
elif (player is None):
    print("Please don't be difficult, I'm this is me working right now. Name, please")
else:
    print(player + ", Wonderful! What a grand name, not stupid at all.")

role = input("Now, let's begin, first, choose a class: fighter, wizard, or crackhead?\n")

role = role.casefold()

match role:
    case "wizard":
        print("Ah, so the spell slinging wizard, wise choice, or so, we shall see.")
    case "fighter":
        print("Sturdy and deadly. Rational features to carry.")
    case "crackhead":
        print("Addiction is just the beginning of your woes.")

sleep(2)

race = input("Now, please select your race... are you a lizard, an elf, or a motherfucking LIVING CHANISAW?!")

match race:
    case "lizard"
        print("Slithery, brutal, and dumb as shit, this lizard dominates nature, and certain segments of the natural world.")


print("\n\nNow, our story begins in the Old Town of Barley Hump.")

