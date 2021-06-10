ram = 0
jar = "vanilla"
print("Hello! This program is supposed to calculate how much RAM would suit your needs.")
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
        print("How many player you would expect?")
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
            print("Are you going to use mostly heavy weight plugins? (yes/no)")
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
    ram += 3
else:
    ram += 2

if version in ["1.8", '1.9', '1.10', '1.11', '1.12']:
    ram = ram
else:
    ram += 2

if 10 < players < 30:
    ram += 1
elif 30 <= players < 50:
    ram += 3
elif 50 <= players < 80:
    ram += 5
elif 80 <= players < 110:
    ram += 6
elif 110 <= players < 160:
    ram += 8
elif 160 <= players <= 200:
    ram += 10
elif players > 200:
    ram += 14

if jar != "vanilla":
    if 20 < plugins < 30:
        ram += 1
    elif 30 <= plugins < 50:
        ram += 2
    elif 50 <= plugins < 80:
        ram += 3
    elif 80 <= plugins < 110:
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
print("Calculated ram is " + str(ram) + " (There is more that you should consider, dont rely on this only)")
print("---------------------------------------------------------------------------------------------------")
print("           THIS IS MADE FOR EXPERIMENTAL PURPOSES AND MAY OR MAY NOT BE ACCURATE")
print("---------------------------------------------------------------------------------------------------")
print("Made By aly#1992")

feedback = input("please dm aly#1992 if you have any feedback")