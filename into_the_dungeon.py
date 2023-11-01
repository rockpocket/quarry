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

sleep(1)

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

sleep(1)

match race:
    case "lizard":
        print("Slithery, brutal, and dumb as shit, this lizard dominates nature, and certain segments of the natural world.\n")
    case "elf":
        print("Nature good. Constructed world bad. Make the world better by killing racist humans. Your forest shall encroach all.\n")

chainsaw = "chainsaw"

if "chainsaw" in race:
    print("You are chaos. You live for destruction. Viewer discretion is advised.\n")

sleep(3)

#Asking the player for their backstory
backstory = input("And finally... what is your backstory? Are you rich, poor, or military?\n")

backstory = backstory.casefold()

sleep(1)

match backstory:
    case "rich":
        print("Good choice. Probably the best choice, honestly. Money solves, like, every problem.\n")
    case "poor":
        print("Understood. You have selected HARD MODE. Good luck.\n")
    case "military":
        print("Military, of course. Who needs wealth or social status when you're capable of killing the people around you.\n")

sleep(3)

#Begin Journey
print("Now, our story begins in the old town of Barley Hump.\n")

sleep(3)

match role:
    case "wizard":
        crime = "setting a library on fire"
    case "fighter":
        crime = "punching the mayor"
    case "crackhead":
        crime = "sucking some guys dick behind a medieval auto-parts store"


print(f'''You are walking to the market to get some groceries, when a lone town guardsman approaches you and says
"Hey! You! {name}! You're under arrest for {crime}, come quietly and face your judgement!\n''')

sleep(8)

guard = input("""Enter your response.
 
Fight, run, talk, or yield?\n""")

guard = guard.casefold()

match guard:
    case "fight":
            match role:
                case "wizard":
                    guard = "win"
                    print("You use your wizardly powers and ignite the foolish lawkeeper into a blazing inferno.")
                case "fighter":
                    guard = "win"
                    print("You kick the guards shin so hard it goes into his ass and he explodes")
                case "crackhead":
                    guard = "caught"
                    print("you launch your wobbling body through the air toward the guard who kicks the shit out of you and knocks you unconscious.")
    case "run":
            match role:
                case "wizard":
                    guard = "caught"
                    print("your frail nerd legs can't outrun a trained guard. Your hilarious attempt to run ends with the guard dragging you away by your collar, flailing.")
                case "fighter":
                    guard = "escaped"
                    print("after a dramatically long, dangerous and parkour fueled chase scene, you narrowly avoid the guard by hopping on a cart.")
                case "crackhead":
                    guard = "escaped"
                    print("you take off the other direction and haul ass through the city and mind boggling speeds. Even after losing the guard, you just kept running for some time.")
    case "talk":
            match role:
                case "wizard":
                    guard = "win"
                    print("A twisting of words with a small dash of spells and you've convinced the guard you are know danger to the city, he lets you free.")
                case "fighter":
                    guard = "caught"
                    print("You make an attempt at talking that comes out to be a bit more on the angry grunt side. During your aggressive babbling, a second guard bonks you out cold.")
                case "crackhead":
                    guard = "caught"
                    print("You start babbling incoherently something about goblins living in your attic and then you try to convince the guard to give you some money. Eventually, he just arrests you.")
    case "yield":
            guard = "caught"
            print("Your hands are tied with rope and you are escorted through the city streets")
#       Saving this for later
#          match role:
#              case "wizard":
#                    guard = ""
#                    print("")
#                case "fighter":
#                    guard = ""
#                    print("")
#                case "crackhead":
#                    guard = ""
#                    print("")

sleep(4)

match guard:
    case "escaped":
        print("You've arrived on the outskirts of town, along the docks.")
        sleep(2)
        print("You come across a group of citizens gathered around a 'Help wanted' poster. It's offering 1000 Gold and dinner with The Mayor for whomever can slay the dragon that has taken residence in a nearby, abandoned, sub-terranean prison, and has been terrorizing the surrounding lands.")
        sleep(4)
        action = input("do you head to the dungeon, or do you simply head back home?")
        action = action.casefold()
        sleep(2)
        if "home" in action:
            print("you gather your groceries and return to your home, where you live comfortably for several weeks until one day you, your belongings, and all your loved ones are burned to death in a dragon attack. The End.")
            sleep(10)
            exit()
        elif "dungeon" in action:
            print("You snatch the poster off the wall and start heading in the direction of the dungeon, ready to get paid")
            sleep(2)
            civilian = input('''"Hey man, we were reading that!" one of the civilians yells at you. Do you run, fight, or return the poster?''')
            civilian.casefold()
            sleep(2)
            if "fight" in civilian:
                print("you karate chop their fucking heads off and the mob of dumb-fuck peasants run away crying and flailing.")
                tofflin = False
            elif "run" in civilian:
                print("you run away laughing, the poster flapping in the wind.")
                tofflin = False
            elif "return" or "poster" in civilian:
                tofflin = input("How very civil of you. So civil in fact, one of them decides to support your quest! His name is Tofflin, and he wish's to be you squire. Do you accept? Yes or no.")
                tofflin.casefold()
                if "yes" in tofflin:
                    print('''"Yippie!" Tofflin announces as he jumps joyously. "This quest is going to be the gayest ever... Onward!"''')
                    tofflin = True
                else:
                    print("You crush the young boys dreams and stride away proudly as he cries in rejection.")
                    tofflin = False
        print("On your way out of town to head to the Dungeon, you meet a weapons trader, He is a former pirate named DickBeard. He offers to sell you a weapon, but you can only afford one.")

        trader = input("")
        weapon =
    case "win":
        weapon =
    case "caught":
        weapon =

#THE DUNGEON
#Factors will include the decisions made up to this point