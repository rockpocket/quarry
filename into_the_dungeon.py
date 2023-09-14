player = input("Welcome Adventurer, to The Dungeon!\nFirst off, may I ask your name?\n")


if player == "no":
    print("Please don't be difficult, I'm this is me working right now. Name, please")
elif (player is None):
    print("Please don't be difficult, I'm this is me working right now. Name, please")
else:
    print(player + ", Wonderful! What a grand name, not stupid at all.")

role = input("Now, let's begin, first, choose a class: Fighter, Wizard, or Crackhead?\n")

role = role.casefold()

if role == "wizard":
    print("Ah, so the spell slinging wizard, wise choice, or so, we shall see.")

print("\n\nNow, our story begins in the Old Town of Barley Hump.")