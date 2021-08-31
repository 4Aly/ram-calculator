print("Minecraft Server RAM Calculator - https://github.com/alyamr2006/ram-calculator")
def main():
    ram = 0
    jar = "vanilla"
    while True:
        try:
            print("Please enter the Minecraft Version you wish to run on your server e.g. 1.8.8, 1.17.1: ")
            version = int(str(input("Answer: ")).split(".")[1])
            if version in list(range(8,18)):
                break
            else:
                print("--------------------------------------")
                print("Please enter a valid Minecraft version")
                print("--------------------------------------")
        except ValueError:
            print("--------------------------------------")
            print("Please enter a valid Minecraft version")
            print("--------------------------------------")
    if version in list(range(8,13)):
        while True:
            try:
                print("Enter the JAR type you prefer: vanilla, spigot, paper")
                jar = str(input("Answer: ").lower())
                if jar in ['vanilla', 'spigot', 'paper']:
                    break
                else:
                    print("--------------------------------------")
                    print("  Please enter a valid JAR type")
                    print("--------------------------------------")
            except ValueError:
                print("--------------------------------------")
                print("  Please enter a valid JAR type")
                print("--------------------------------------")

    else:
        while True:
            try:
                print("Enter the JAR type you prefer: vanilla, spigot, paper, purpur")
                jar = str(input("Answer: ").lower())
                if jar in ['vanilla', 'spigot', 'paper', 'purpur']:
                    break
                else:
                    print("--------------------------------------")
                    print("  Please enter a valid JAR type")
                    print("--------------------------------------")
            except ValueError:
                print("--------------------------------------")
                print("  Please enter a valid JAR type")
                print("--------------------------------------")

    while True:
        try:
            print("How many players at most would be on the server at once?")
            players = int(input("Answer: "))
            if players > 0:
                break
            else:
                print("--------------------------------------")
                print("   Please enter an integer")
                print("--------------------------------------")
        except ValueError:
            print("--------------------------------------")
            print("      Please enter an integer")
            print("--------------------------------------")

    if jar != "vanilla":

        while True:
            try:
                print("How many plugins you would need?")
                plugins = int(input("Answer: "))
                if plugins > 0:
                    break
                else:
                    print("--------------------------------------")
                    print("   Please enter an integer")
                    print("--------------------------------------")
            except ValueError:
                print("--------------------------------------")
                print("      Please enter an integer")
                print("--------------------------------------")

    if jar != "vanilla":

        while True:
            try:
                print("Are you going to use mostly heavy weight plugins? (yes/no). These could be plugins like fully custom items or world gen, as some examples.")
                weight = str(input("Answer: ").lower())
                if weight in ['yes', 'no']:
                    break
                else:
                    print("--------------------------------------")
                    print("      Please enter yes or no")
                    print("--------------------------------------")
            except ValueError:
                print("--------------------------------------")
                print("      Please enter yes or no")
                print("--------------------------------------")

    if jar in ['vanilla', 'bukkit', 'spigot']:
        if players >= 20:
            ram += 3
        elif players >= 10:
            ram += 1
        else:
            ram += 0.5
    else:
        ram += 2

    if not version in list(range(8,13)):
        ram += 2

    if 20 < players < 40:
        ram += 1
    elif 40 <= players < 70:
        ram += 3
    elif 70 <= players < 100:
        ram += 5
    elif 100 <= players < 140:
        ram += 6
    elif 140 <= players < 180:
        ram += 8
    elif 180 <= players <= 220:
        ram += 10
    elif players > 220:
        ram += 14

    if jar != "vanilla":
        if 30 < plugins < 50:
            ram += 1
        elif 50 <= plugins < 70:
            ram += 2
        elif 70 <= plugins < 90:
            ram += 3
        elif 90 <= plugins < 110:
            ram += 4
        elif 110 <= plugins < 160:
            ram += 5
        elif 160 <= plugins <= 200:
            ram += 6
        elif plugins > 200:
            ram += 8

    if jar != "vanilla":
        if weight == "yes":
            ram += 1

    print("\033c")
    print("---------------------------------------------------------------------------------------------------")
    print(f"Approximately, your server will need {ram}GB allocated. Please note this tool is not 100% accurate.")
    print("---------------------------------------------------------------------------------------------------")

    

while True:
    main()
    repeat = str(input("Restart? (yes/no)").lower())
    if repeat != 'yes':
        print("---------------------------------------------------------------------------------------------------")
        print("Thanks for using this tool, made by aly#1992\nYou can view the other generous contributors here:\nhttps://github.com/alyamr2006/ram-calculator")
        print("---------------------------------------------------------------------------------------------------")
        break
