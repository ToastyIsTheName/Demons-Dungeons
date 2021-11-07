
import random, sys, time, csv

warlockhealth = 125
warriorhealth = 200
playerid = " "


def instructions():
    print(" *Welcome to The Demon's Dungeon* ")
    time.sleep(1)
    print("The aim of the game is to find the treasure hidden somewhere in the compound ")
    time.sleep(1)
    print("To find the treasure you must battle the demons that guard the different rooms ")
    time.sleep(1)
    print("To defeat a demon you must out roll them with your dice ")
    time.sleep(1)
    print("   ")
    print("Instructions: ")
    time.sleep(3)
    print(" Utiling your players ability, you must defeat each demon defending the rooms.")
    time.sleep(3)
    print(" The battles will commence and be dictated by the roll of two die. One from the player and one from the defending demon")
    time.sleep(3)
    print(" Some demons will have a better chance of winning than others and maybe you. You must be cautious at all times as every decision counts ")
    time.sleep(3)
    print(" Once one room cleared, you must move on forward to the next. The clearing technique and battle mechanism will stay the same throughout the game")
    time.sleep(3)
    print(" The final fight, as the rest, will be a tough one. If the final demon is defeated, you will unlock the final room. The treasure will be in this room. Once finding the treasure, vacate the premisis as fast as possible. Good Luck! ")
    print(" ")
    time.sleep(2)
    choice = input("Press any key to continue... ")
    menu()


def menu():
    print("  ")
    print("Choose your character: ")
    time.sleep(1)
    print(" ")
    print("The warlock has great wisdom but isnt the most defensive ")
    time.sleep(1)
    print(" ")
    print("The warrior has irreplacable strength but lacks situational knowledge ")
    time.sleep(1.5)
    choice = input("Press 1 for Warlock, 2 for Warrior or 3 to quit ")
    if choice == "1":
        print("Good luck Warlock! ")
        warlock()
    elif choice == "2":
        print("Good luck Warrior! ")
        warrior()
    elif choice == "3":
        sys.exit()
    else:
        menu()


def warlock():
    global playerid
    playerid = "Warlock"
    print("  ")
    print("Warlock has 125 Health Points at the start of the game ")
    time.sleep(1)
    print("Warlock has 7 sided dice ")
    time.sleep(1)
    print(" To pass through a room you must defeat the demon guarding it ")
    time.sleep(1)
    print("Defeat the demon by winning 2 dice rolls ")
    choice = input("Press any key to continue... ")
    room1()

def warrior():
    global playerid
    playerid = "Warrior"
    print("  ")
    print("Warrior has 200 Health Points at the start of the game ")
    time.sleep(1)
    print("Warrior has a 6 sided dice ")
    time.sleep(1)
    print("To pass through a room you must defeat the demon guarding it ")
    time.sleep(1)
    print("Defeat the demon by winning 2 dice rolls ")
    choice = input("Press any key to continue... ")
    room1()

def room1():
    print("  ")
    print(" ********************************************** ")
    print("  --------- Welcome To The beginning --------- ")
    print(" ********************************************** ")
    print("  ")
    time.sleep(0.5)
    choice = input("Press any key to continue... ")
    time.sleep(2)
    wincount = 0
    global warlockhealth
    global warriorhealth
    global playerid
    print("You shouldn't of came here! Brute wont let you come here. I am BRUTE! ")
    if playerid == "Warlock":
        while wincount != 2:
            print("  ")
            time.sleep(1)
            demonroll = random.randint(1,8)
            print("Brute scores %s" % demonroll)
            warlockroll = random.randint(1,7)
            print("Warlock scores %s" % warlockroll)
            if warlockroll>=demonroll:
                wincount = wincount+1
                print("You have injured Brute ")
            else:
                warlockhealth = warlockhealth - 25
                print("Brute got a heavy hit onto you! ")
                print("You now have %s Health Points" % warlockhealth)
                if warlockhealth < 0:
                    print("You have run out of HP! ")
                    print("Game Over, better luck next time ")
                    sys.exit()

        print("You picked up a rock and Brute caught it across the head ")
        print("You now have %s HP" % warlockhealth)
        print("Well done Warlock, Carry on forward to find the next room ")
        room2()

    if playerid == "Warrior ":
        while wincount != 2:
            print(" ")
            time.sleep(1)
            demonroll = random.randint(1,8)
            print("Brute scores %s " % demonroll)
            warriorroll = random.randint(1,6)
            print("Warrior scores %s" % warriorroll)
            if warriorroll>=demonroll:
                wincount = wincount+1
                print("You have injured Brute ")
            else:
                warriorhealth = warriorhealth - 25
                print("Brute got a heavy hit onto you! ")
                print("You now have %s Health Points" % warriorhealth)
                if warriorhealth <0:
                    print("You have run out of HP! ")
                    print("Game Over, better luck next time ")
                    sys.exit

        print("You have picked up a rock and Brute caught it across the head ")
        print("You now have %s HP" % warriorhealth)
        print("Well done Warrior, Carry on forward to find the next room ")
        room2()

def room2():
    print(" ")
    print(" ************************************************* ")
    print("  --------- Welcome To The Torture Room --------- ")
    print(" ************************************************* ")
    print(" " )
    choice = input("Press any key to continue... ")
    time.sleep(2)
    print("Congratulations you have reached Room Two ")
    print("That was a tough battle, well done to you! As a reward you have gained an extra 100 Health Points ")
    print(" ")
    wincount = 1
    global warlockhealth
    global warriorhealth
    global playerid
    print("Cruciatu is the chosen demon for this room. He specialises in torutre and pain so be careful! ")
    if playerid == "Warlock":
        while wincount != 2:
            print("  ")
            time.sleep(1)
            demonroll = random.randint(1,9)
            print("Cruciatu scores %s" % demonroll)
            warlockroll = random.randint(1,7)
            print("Warlock scores %s" % warlockroll)
            if warlockroll>=demonroll:
                wincount = wincount+1
                print("You have injured Cruciatu ")
            else:
                warlockhealth = warlockhealth - 25
                print("Cruciatu got a heavy hit onto you! ")
                print("You now have %s healthpoints" %warlockhealth)
                if warlockhealth < 0:
                    print("You have run out of HP! ")
                    print("Game Over, better luck next time ")
                    sys.exit()

        print("You picked up a log and Cruciatu caught it across the head ")
        print("You now have %s HP" % warlockhealth)
        print("Well done Warlock, Carry on forward to find the next room ")
        room3()

    if playerid == "Warrior ":
        while wincount != 2:
            print(" ")
            time.sleep(1)
            demonroll = random.randint(1,9)
            print("Cruciatu scores %s " % demonroll)
            warriorroll = random.randint(1,6)
            print("Warrior scores %s" % warriorroll)
            if warriorroll>=demonroll:
                wincount = wincount+1
                print("You have injured Cruciatu ")
            else:
                warriorhealth = warriorhealth - 25
                print("Brute got a heavy hit onto you! ")
                print("You now have %s Health Points" % warriorhealth)
                if warriorhealth <0:
                    print("You have run out of HP! ")
                    print("Game Over, better luck next time ")
                    sys.exit

        print("You have picked up a log and Cruciatu caught it across the head ")
        print("You now have %s HP" % warriorhealth)
        print("Well done Warrior, Carry on forward to find the next room ")
        room3()

def room3():
    print(" ")
    print(" ************************************************* ")
    print("  --------- Welcome To Toilet Chamber ----------- ")
    print(" ************************************************* ")
    print(" " )
    choice = input("Press any key to continue... ")
    time.sleep(2)
    print("Congratulations you have reached The Lavatory ")
    print("That was a tough battle, well done to you! As a reward you have gained an extra 100 Health Points and a toilet break, Unless you cannot defeat Feline ")
    print(" ")
    wincount = 2
    global warlockhealth
    global warriorhealth
    global playerid
    print("Cruciatu is the chosen demon for this room. He specialises in torutre and pain so be careful! ")
    if playerid == "Warlock":
        while wincount != 2:
            print("  ")
            time.sleep(1)
            demonroll = random.randint(1,9)
            print("Cruciatu scores %s" % demonroll)
            warlockroll = random.randint(1,7)
            print("Warlock scores %s" % warlockroll)
            if warlockroll>=demonroll:
                wincount = wincount+1
                print("You have injured Cruciatu ")
            else:
                warlockhealth = warlockhealth - 25
                print("Cruciatu got a heavy hit onto you! ")
                print("You now have %s healthpoints" %warlockhealth)
                if warlockhealth < 0:
                    print("You have run out of HP! ")
                    print("Game Over, better luck next time ")
                    sys.exit()

        print("You picked up a log and Cruciatu caught it across the head ")
        print("You now have %s HP" % warlockhealth)
        print("Well done Warlock, Carry on forward to find the next room ")
        final_room()

    if playerid == "Warrior ":
        while wincount != 2:
            print(" ")
            time.sleep(1)
            demonroll = random.randint(1,9)
            print("Cruciatu scores %s " % demonroll)
            warriorroll = random.randint(1,6)
            print("Warrior scores %s" % warriorroll)
            if warriorroll>=demonroll:
                wincount = wincount+1
                print("You have injured Cruciatu ")
            else:
                warriorhealth = warriorhealth - 25
                print("Brute got a heavy hit onto you! ")
                print("You now have %s Health Points" % warriorhealth)
                if warriorhealth <0:
                    print("You have run out of HP! ")
                    print("Game Over, better luck next time ")
                    sys.exit

        print("You have picked up a log and Cruciatu caught it across the head ")
        print("You now have %s HP" % warriorhealth)
        print("Well done Warrior, Carry on forward to find the next room ")
        final_room()


def final_room():
    print(" ")
    print(" ************************************************* ")
    print("  --------- Welcome To The Treasury ------------- ")
    print(" ************************************************* ")
    print(" ")
    print("This is The Final Room. Deafeating the defender of the treasury would mean you take everything inside. Losing this would result in losing everything you have worked for tonight! ")
    print(" ")
    choice = input("Press any key to continue ")
    time.sleep(2)
    print("Well done on making it this far. Sadly, its not over yet ")
    print("For getting this far the game master is rewarding you with 200 extra HP ")
    print(" You are going to need them as the defender of the Treasury is Diablo! ")
    print(" Diablo has extensive knowledge in defence, you must land 5 good attacks to take him down! ")
    print(" ")
    choice = input("Press any key to continue ")
    wincount = 3
    global warlockhealth
    global warriorhealth
    global playerid
    if playerid == "Warlock":
        while wincount != 2:
            print("  ")
            time.sleep(1)
            demonroll = random.randint(1,12)
            print("Diablo scores %s" % demonroll)
            warlockroll = random.randint(1,7)
            print("Warlock scores %s" % warlockroll)
            if warlockroll>=demonroll:
                wincount = wincount+1
                print("You have injured Diablo ")
            else:
                warlockhealth = warlockhealth - 25
                print("Cruciatu got a heavy hit onto you! ")
                print("You now have %s healthpoints" %warlockhealth)
                if warlockhealth < 0:
                    print("You have run out of HP! ")
                    print("Game Over, better luck next time ")
                    sys.exit()

        print("You picked up a log and Diablo caught it across the head ")
        print("You now have %s HP" % warlockhealth)
        print("Well done Warlock, you have reached and defeated the final demon. This means you have made your way to the treasure. Make sure to save me some ! ")
        menu()

    if playerid == "Warrior ":
        while wincount != 2:
            print(" ")
            time.sleep(1)
            demonroll = random.randint(1,9)
            print("Diablo scores %s " % demonroll)
            warriorroll = random.randint(1,6)
            print("Warrior scores %s" % warriorroll)
            if warriorroll>=demonroll:
                wincount = wincount+1
                print("You have injured Diablo ")
            else:
                warriorhealth = warriorhealth - 25
                print("Brute got a heavy hit onto you! ")
                print("You now have %s Health Points" % warriorhealth)
                if warriorhealth <0:
                    print("You have run out of HP! ")
                    print("Game Over, better luck next time ")
                    sys.exit

instructions()
    


