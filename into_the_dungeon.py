import re
import time

#Defining sleep function
def sleep(sec):
    time.sleep(sec)

#Defining player name
name = input("Welcome Adventurer, to The Dungeon!\nFirst off, may I ask your name?\n")




sleep(1)

#Asking the player his name

while True:
    match name:
         case "no":
             name = input("Please don't be difficult, I'm this is me working right now. Name, please\n")
         case other:
             break

sleep(2)

print(name + ", Wonderful! What a grand name, not stupid at all.\n")

sleep(3)

print('''Now, before we get started, a couple ground rules to clarify. Please be aware:\n''')

sleep(3)

print('''1. This logic here is not perfect. Please input your answers as clearly as possible.\n''')

sleep(4)

print('''2. It's really hard to account for all possibilities and the DM is very lazy, so,
please try your best to stay on the paths laid out for you.\n''')

sleep(4)

print('''3. And finally, most importantly, there are many opportunities here for instant death.
Be careful what choices you make.\n''')

sleep(4)

print('''Make the right decisions, and survive to the end... and of course, have fun Godammit!!\n''')


sleep(3)


role = input("Ok! NOW, let's begin. First, choose a class: fighter, wizard, or crackhead?\n")

role = role.casefold()

sleep(1)

#Asking the player his role
while True:
    match role:
        case "wizard":
            print("Ah, so the spell slinging wizard, wise choice, or so, we shall see.\n")
            break
        case "fighter":
            print("Sturdy and deadly. Rational features to carry.\n")
            break
        case "crackhead":
            print("Addiction is just the beginning of your woes.\n")
            break
        case other:
            role = input("I think you mistyped something, or you're jesting. Please try again.\n")

sleep(2)


#Asking the player his race
race = input("Now, please select your race... are you a lizard, an elf, or a motherfucking LIVING CHAINSAW?!\n")

race = race.casefold()

if "chainsaw" in race:
    race = "chainsaw"

sleep(1)

while True:
    match race:
        case "lizard":
            print("Slithery, brutal, and dumb as shit, this lizard dominates nature, and certain"
                  "parts of the civilized world.\n")
            break
        case "elf":
            print("Nature good. Constructed world bad. Make the world better by killing"
                  "racist humans. Your forest shall encroach all.\n")
            break
        case "chainsaw":
            print("You are chaos. You live for destruction. Viewer discretion is advised.\n")
            break
        case other:
            backstory = input("I think you mistyped something, or you're jesting. Please try again.\n")



sleep(3)

#Asking the player for their backstory
backstory = input("And finally... what is your backstory? Are you rich, poor, or military?\n")

backstory = backstory.casefold()

sleep(1)


#make this a loop
while True:
    match backstory:
        case "rich":
            print("Good choice. Probably the best choice, honestly. Money solves, like, every problem.\n")
            break
        case "poor":
            print("Understood. You have selected HARD MODE. Good luck.\n")
            break
        case "military":
            print("Military, of course. Who needs wealth or social status when you're capable of killing the people around you.\n")
            break
        case other:
            backstory = input("I think you mistyped something, or you're jesting. Please try again.\n")

sleep(3)

character = (name, role, race, backstory)

print("This is a test")
print(character[0])
print(character[1])
print(character[2-3])

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
"Hey! You! {name}! You're under arrest for {crime}, come quietly and face your judgement!"\n''')

sleep(8)

guard = input("""Enter your response.
 
Fight, run, talk, or yield?\n""")

guard = guard.casefold()

sleep(2)

#Guard encounter

while True:
    match guard:
        case "fight":
                match role:
                    case "wizard":
                        guard = "win"
                        print('''You use your wizardly powers and ignite the foolish lawkeeper into a blazing inferno.\n''')
                        break
                    case "fighter":
                        guard = "win"
                        print('''You kick the guards shin so hard it goes into his ass and he explodes\n''')
                        break
                    case "crackhead":
                        guard = "caught"
                        print('''you launch your wobbling body through the air toward the guard who kicks the shit
                              out of you and knocks you unconscious.\n''')
                        break
        case "run":
                match role:
                    case "wizard":
                        guard = "caught"
                        print('''your frail nerd legs can't outrun a trained guard. Your hilarious attempt to run
                              ends with the guard dragging you away by your collar, flailing.\n''')
                        break
                    case "fighter":
                        guard = "escaped"
                        print('''after a dramatically long, dangerous and parkour fueled chase scene, you narrowly
                              avoid the guard by hopping on a cart.\n''')
                        break
                    case "crackhead":
                        guard = "escaped"
                        print('''you take off the other direction and haul ass through the city and mind boggling speeds.
                              Even after losing the guard, you just kept running for some time.\n''')
                        break
        case "talk":
                match role:
                    case "wizard":
                        guard = "convinced"
                        print('''A twisting of words with a small dash of spells and you've convinced the guard you
                              are know danger to the city, he lets you free.\n''')
                        break
                    case "fighter":
                        guard = "caught"
                        print('''You make an attempt at talking that comes out to be a bit more on the angry grunt side.
                              During your aggressive babbling, a second guard bonks you out cold.\n''')
                        break
                    case "crackhead":
                        guard = "caught"
                        print('''You start babbling incoherently something about goblins living in your attic 
                              and then you try to convince the guard to give you some money. Eventually, 
                              he just arrests you.\n''')
                        break
        case "yield":
                guard = "caught"
                print("Your hands are tied with rope and you are escorted through the city streets\n")
                break
        case other:
                guard = input("I think you mistyped something, or you're jesting. Please try again.\n")

sleep(4)

#After guard encounter and build up to the mission
#This decide a few things, like whether you get a companion and what weapon you get.


#potentials:
#escaped
#win
#convinced
#caught

match guard:
    #Escaped to the edge of town
    case "escaped":
        print("You've arrived on the outskirts of town, along the docks.\n")
        sleep(2)
        print('''You come across a group of citizens gathered around a 'Help wanted' poster. It's offering 1000 Gold
              and dinner with The Mayor for whomever can slay the dragon that has taken residence in a nearby,
              abandoned, sub-terranean prison, and has been terrorizing the surrounding lands.\n''')
        sleep(4)
        action = input("do you head to the dungeon, or do you simply head back home?\n")
        action = action.casefold()
        sleep(2)
        if "home" in action:
            print('''you gather your groceries and return to your home, where you live comfortably for several
                weeks. Until one day; you, your belongings, and all your loved ones
                are burned to death in a dragon attack.
    
                *The End*\n''')
            sleep(10)
            exit()
        elif "dungeon" in action:
            print('''You snatch the poster off the wall and start heading in the direction of the dungeon, ready to get paid''')
            sleep(2)
            civilian = input('''\"Hey man, we were reading that!\" one of the civilians yells at you.
            
            Do you run, fight, or return the poster?''')
            civilian.casefold()
            sleep(2)
            if "fight" in civilian:
                print('''You karate chop their fucking heads off and the mob of dumb-fuck peasants run away crying and flailing.\n''')
                tofflin = False
            elif "run" in civilian:
                print('''you run away laughing, the poster flapping in the wind.\n''')
                tofflin = False
            elif "return" or "poster" in civilian:
                tofflin = input('''How very civil of you. So civil in fact, one of them decides to support your quest!
                His name is Tofflin, and he wish's to be you squire. Do you accept? Yes or no.\n''')
                tofflin.casefold()
                if "yes" in tofflin:
                    print('''"Yippie!" Tofflin announces as he jumps joyously. \"This quest is going to be the gayest ever... Onward!\"\n''')
                    tofflin = True
                else:
                    print("You crush the young boys dreams and stride away proudly as he cries from rejection.\n")
                    tofflin = False
        print('''On your way out of town to head to the Dungeon, you meet a weapons trader, He is a former pirate named DickBeard.
              He offers to sell you a weapon, but you can only afford one.\n''')

        sleep(3)

        trader = input('''\"WHAT'LL BE YA DICKLESS FUCKIN COWARD!?\" he asks you.
        In front of him there is a mace, a cutlass, and a twenty inch iron dildo.
        
        Which do you choose?\n''')

        trader = trader.casefold()

        match trader:
            case "mace":
                weapon = "mace"
            case "cutlass":
                weapon = "cutlass"

        if "iron" or "dildo" in trader:
            weapon = "iron dildo"

        sleep(2)

        match race:
            case "chainsaw":
                print('''As you lean forward to pay the man, your chainsaw appendages 'accidentally' sever his beard of
                wiggling willies. He cries bleeds and dies, then you run off as the villagers begin to form a mob.\n''')
                sleep(4)
                print(f'''but at least you got the {weapon} for free.\n''')
            case other:
                print('''\"Aye, a good choice there laddie!\" says Dickbeard, his locks jiggling majestically.
                \"Now, ye be careful with that thar quest yer goin' on. They don't offer 1000 Gold for now normal mission.
                No boy, that amount only gets offered to people they intend to use as cannon fodder. Keep an eye out,
                OR THEY'LL TAKE YOUR BALLS! HAAHAHAHAHAA!\"\n
                ''')

                sleep(6)

                print('''You ignore the smell of crusty cheese wafting upon his breath and disembark from the occupied docks\n''')

                sleep(2)

        print('''You have now reached the edge of the city, and upon a dusty dirt road you march off into the wilderness\n''')

        sleep(3)

        if tofflin == True:
            print('''...and Tofflin skipped behind merily...\n''')
            sleep(3)
            print('''...his optimism would not be misplaced, surely...\n\n''')
            sleep(4)
            print(''':)\n\n''')

        sleep(2)

#Defeated the guard and gets pulled into a criminal organization
    case "win":
        print('''The guard collapses to the dirt road, no longer a threat. Civilians run in fear of your awesome power. 
        All but one person, a hooded man who watches you from the alley.\n''')
        sleep(3)
        print('''the man then notions for you to follow him, and slips away into the alley.\n''')
        sleep(2)
        if backstory == "poor":
            print('''Your experience in poverty helps you identify that he's trying to help you hide
            before more guards show up.\n''')
            sleep(3)
        thief = input('''Do you follow him?\n''')
        thief = thief.casefold()
        #following the thief
        if "yes" or "follow" in thief:
            print('''You move into the darkened alley, and see the hooded man slunk behind a corner.
            You follow on his heels, staying one step behind as he keep just narrowly keeping himself ahead and slightly hidden.\n''')
            sleep(3)
            print('''Finally, you turn a corner and see the man look at you as he raises a trap door hidden behind
            a barrel and slips below ground.\n''')
            sleep(2)
            follow = input('''Do you follow him down the hatch?\n''')
            follow = follow.casefold()
            if follow == "yes" or "follow":
                sleep(1)
                print("")
            else:
                sleep(1)
                print('''You hear a whisper from a voice uncomfortably close to your ear say
                \"You can't know our secret location and just walk away\"\n''')
                sleep(3)
                if role == "fighter":
                    print('''You feel these fuckers ATTEMPT to place a blade in you back, but you're a fighter.
                    You're trained specifically to not be about that shit.\n''')

                    sleep(3)

                    print('''You spin around to see two thieves who had emerged from the shadows, shattering ones
                    collar bone with a fucking karate chop as you do.\n''')

                    sleep(3)

                    print('''The other attempts to disengage, but you grab his arm and break it you three locations
                    before snapping his shin in half with a downward stomp. You then powerbomb him right the fuck
                    into the other thief, killing both.\n''')

                    sleep(4)

                    revenge = input('''With the assassins dead, do you now head down the thieves hatch to seek revenge,
                    or do you run?\n''')

                    if "fight" or "kill" or "revenge" or "hatch" in revenge:
                        print('''''')
                    else:
                        print('''''')

                else:
                    print('''You feel cold steel peirce your spine, and the world goes black. You are dead.''')

                    sleep(2)

                    print('''*The End*''')

                    sleep(2)

                    exit()
        #Trying to fight the law, instead of following the thief
        else:
            print('''You ignore the man and begin heading back on your quest for groceries.\n''')
            sleep(2)
            print('''However, your actions have seemed to piss off the town guard. Now, 5 guards approach you.
            \"On the ground, Criminal!\n''')
            match crime:
                case "setting a library on fire":
                    print('''Your days of igniting public buildings are over! Time to die!\"\n''')
                case "punching the mayor":
                    print('''Your days of punching elected officials are over! Time to die!\"\n''')
                case "sucking some guys dick behind a medieval auto-parts store":
                    print('''Your days of shotgunning cocks are over! Time to die!\"\n''')
            sleep(4)
            print('''It seems these guards are out for blood and aren't willing to negotiate.\n''')
            sleep(3)


        weapon = ""

#Caught by the guard and is taken to meet the mayor
    case "caught":
        weapon = ""

#THE DUNGEON
#Factors will include the decisions made up to this point