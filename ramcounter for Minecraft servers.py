print("Hello! This program is supposed to calculate how much RAM would suit your needs.")
def main():
    ram = 0
    jar = "vanilla"
    while True:
        try:
            print("Enter the minecraft version you prefer: 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17")
            version = str(input("Answer: "))
            if version in ["1.8", '1.9', '1.10', '1.11', '1.12', '1.13', '1.14', '1.15', '1.16', '1.17']:
                break
            else:
                print("--------------------------------------")
                print("Please enter a valid minecraft version")
                print("--------------------------------------")
        except ValueError:
            print("--------------------------------------")
            print("Please enter a valid minecraft version")
            print("--------------------------------------")
    if version in ["1.17"]:
        print("Only vanilla jar is available so let's move on to the next question")
    elif version in ["1.8", "1.9", "1.10", "1.11", "1.12"]:
        while True:
            try:
                print("Enter the Server Jar you prefer: vanilla, spigot, paper")
                jar = str(input("Answer: ").lower())
                if jar in ['vanilla', 'spigot', 'paper']:
                    break
                else:
                    print("--------------------------------------")
                    print("  Please enter a valid Server Jar")
                    print("--------------------------------------")
            except ValueError:
                print("--------------------------------------")
                print("  Please enter a valid Server Jar")
                print("--------------------------------------")

    else:
        while True:
            try:
                print("Enter the Server Jar you prefer: vanilla, spigot, paper, purpur")
                jar = str(input("Answer: ").lower())
                if jar in ['vanilla', 'spigot', 'paper', 'purpur']:
                    break
                else:
                    print("--------------------------------------")
                    print("  Please enter a valid Server Jar")
                    print("--------------------------------------")
            except ValueError:
                print("--------------------------------------")
                print("  Please enter a valid Server Jar")
                print("--------------------------------------")

    while True:
        try:
            print("How many players are you hoping to run with?")
            players = int(input("Answer: "))
            if players > 0:
                break
            else:
                print("--------------------------------------")
                print("   Please enter a positive number")
                print("--------------------------------------")
        except ValueError:
            print("--------------------------------------")
            print("      Please enter a number")
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
                    print("   Please enter a positive number")
                    print("--------------------------------------")
            except ValueError:
                print("--------------------------------------")
                print("      Please enter a number")
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

    print("Calculating...")

    if jar in ['vanilla', 'bukkit', 'spigot']:
        if players > 20:
            ram += 3
        else:
            ram += 0
    else:
        ram += 2

    if version in ["1.8", '1.9', '1.10', '1.11', '1.12']:
        ram = ram
    else:
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

    print("Ram has been calculated")
    print("---------------------------------------------------------------------------------------------------")
    print(f"Calculated ram is {ram}GB plus 1 GB of overflow if you are on pterodactyl panel (this is really important and needed)! (There is more that you should consider, dont rely on this only)")
    print("---------------------------------------------------------------------------------------------------")
    print("           THIS IS MADE FOR EXPERIMENTAL PURPOSES AND MAY OR MAY NOT BE ACCURATE")
    print("---------------------------------------------------------------------------------------------------")
    print("Made By aly#1992, view contributors on the github at https://github.com/alyamr2006/ram-calculator .")

    

while True:
    main()
    repeat = str(input("Restart? (yes/no)").lower())
    if repeat != 'yes':
        break
