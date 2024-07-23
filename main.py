import math
import random

iron = 0
stone = 0
gold = 0
gems = 0
food = 0
wood = 0
seeds = 0
plantedSeeds = 0
fields = 5
firstRun = True
month = 0

monsterdifficulty = 0
monsterattackchance = 50

while True:
    month += 1
    print(f"It is month **{month}**!")

    if firstRun == False:
        if plantedSeeds > 0:
            print(f"Your {plantedSeeds} planted seeds grew! You got {plantedSeeds * 3} food")
            food += plantedSeeds * 3 
            plantedSeeds = 0
        else:
            pass
    else:
        firstRun = False

    playerOption = input("Would you want to MINE, FARM, CHOP trees, LOOK for seeds or HUNT?")
    playerOption = playerOption.upper()
    print(playerOption)
    if playerOption == "MINE":
        gemgot = False
        stone += 5
        iron += 2
        gold += 1
        gemCheck = random.randint(0, 100)
        if gemCheck <= 20:
            gems += 1
            gemgot = True
            print("You got **5** stone, **2** iron, **1** gold and **1** gem!")
        else:
            print("You got **5** stone, **2** iron and **1** gold")

    elif playerOption == "FARM":
        if seeds > fields:
            plantedSeeds = fields
            seeds -= fields
            print(f"You planted **{fields}** seeds!")
        else:
            plantedSeeds = seeds
            print(f"You planted **{seeds}** seeds!")
            seeds = 0
    
    elif playerOption == "CHOP":
        wood += 5
        print(f"You got 5 wood!")
    elif playerOption == "LOOK":
        seeds += 5
        print(f"You found 5 seeds!")
    elif playerOption == "HUNT":
        food += 5
        print(f"You got 5 food!")

    VanityChoice = input ("Would you want to BUILD something or RESEARCH new things?")
    VanityChoice = VanityChoice.upper()
    print(VanityChoice)
    if VanityChoice == "BUILD":
        #Should come up with a few possible buildings here, preferrably in a dictionary in a separate file!
        pass
    if VanityChoice == "RESEARCH":
        #Should come up with research here, possibly tech tree!
        pass

    monsterAttackRoll = random.randint(0, 100)
    if monsterAttackRoll < monsterattackchance:
        print(f"Monsters attacked! Stolen: {stone/2} stone, {wood/2} wood, {food/2} food")
        stone = stone/2
        wood = wood/2
        food = food/2

    food -= 2
    if food <= 0:
        print ("You starved! :(")
        break
    else:
        print(f"{wood} wood, {plantedSeeds} planted seeds, {food} food, {stone} stone, {fields} fields, {seeds} seeds")
        print("============================== NEW MONTH =====================================")
