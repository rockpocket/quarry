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
    print(name + ", Wonderful! What a grand name, not stupid at all.\n")

sleep(2)

role = input("Now, let's begin, first, choose a class: fighter, wizard, or crackhead?\n")

role = role.casefold()

#Asking the player his role
match role:
    case "wizard":
        print("Ah, so the spell slinging wizard, wise choice, or so, we shall see.\n")
    case "fighter":
        print("Sturdy and deadly. Rational features to carry.\n")
    case "crackhead":
        print("Addiction is just the beginning of your woes.\n")

sleep(2)


#Asking the player his race
race = input("Now, please select your race... are you a lizard, an elf, or a motherfucking LIVING CHAINSAW?!\n")

race = race.casefold()

match race:
    case "lizard":
        print("Slithery, brutal, and dumb as shit, this lizard dominates nature, and certain segments of the natural world.\n")
    case "elf":
        print("Nature good. Natural world bad. Make the world better by killing racist humans. Your forest shall encroach all.\n")

chainsaw = "chainsaw"

if "chainsaw" in race:
    print("You are chaos. You live for destruction. Viewer discretion is advised.\n")

sleep(2)

#Asking the player for their backstory
backstory = input("And finally... what is your backstory? Are you rich, poor, or military?\n")

backstory = backstory.casefold()

sleep(2)

match backstory:
    case "rich":
        print("Good choice. Probably the best choice, honestly. Money solves, like, every problem.\n")
    case "poor":
        print("Understood. You have selected HARD MODE. Good luck.\n")
    case "military":
        print("Military, of course. Who needs wealth or social status when you're capable of killing the people around you.\n")

sleep(2)

#Begin Journey
print("Now, our story begins in the Old Town of Barley Hump.\n")

sleep(2)

match role:
    case "wizard":
        crime = "setting a library on fire"
    case "fighter":
        crime = "punching the mayor"
    case "crackhead":
        crime = "sucking some guys dick behind a medieval auto-parts store"


print(f'''You are walking to the market to get some groceries, when a lone town guardsman approaches you and says
"Hey! You! {name}! You're under arrest for {crime}, come quietly and face your judgement!\n''')

guard = input("""Enter your response.
 
Fight, run, talk, or yeild?\n""")