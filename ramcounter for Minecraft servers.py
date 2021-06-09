ram = 0
jar = "vanilla"
print("Hello! This program is supposed to calculate how much RAM would suit your needs.")
while True:
  try:
    print("Enter the minecraft version you prefer: 1.8 , 1.9 , 1.10 , 1.11 , 1.12 , 1.13 , 1.14 , 1.15 , 1.16 , 1.17")
    version = str(input("Answer:"))
    if version in ["1.8" , '1.9' , '1.10' , '1.11' , '1.12' , '1.13' , '1.14' , '1.15' , '1.16' , '1.17']:
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
elif version in ["1.8" , "1.9" , "1.10" , "1.11" , "1.12"]:
  while True:
    try:
      print("--------------------------------------")
      print("--------THIS IS CASE SENSITIVE--------")
      print("--------------------------------------")
      print("Enter the Server Jar you prefer: vanilla , spigot , paper")
      jar = str(input("Answer:"))
      if jar in ['vanilla' , 'spigot' , 'paper']:
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
      print("--------------------------------------")
      print("--------THIS IS CASE SENSITIVE--------")
      print("--------------------------------------")
      print("Enter the Server Jar you prefer: vanilla , spigot , paper , purpur")
      jar = str(input("Answer:"))
      if jar in ['vanilla' , 'spigot' , 'paper' , 'purpur']:
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
    players = int(input("Answer:"))
    if players>0:
        break
    else:
        print("--------------------------------------")
        print("   Please enter a positive number")
        print("--------------------------------------")
  except ValueError:
        print("--------------------------------------")
        print("      Please enter a number")
        print("--------------------------------------")

if jar!="vanilla":

  while True:
    try:
      print("How many plugins you would need?")
      plugins = int(input("Answer:"))
      if plugins>0:
          break
      else:
          print("--------------------------------------")
          print("   Please enter a positive number")
          print("--------------------------------------")
    except ValueError:
          print("--------------------------------------")
          print("      Please enter a number")
          print("--------------------------------------")

if jar!="vanilla":

  while True:
    try:
      print("Are you going to use mostly heavy weight plugins? (yes/no)")
      weight = str(input("Answer:"))
      if weight in ['yes' , 'no']:
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

if jar in ['vanilla' , 'bukkit' , 'spigot']:
    ram = ram+3
else:
    ram = ram+2

if version in ["1.8" , '1.9' , '1.10' , '1.11' , '1.12']:
    ram = ram
else:
    ram = ram+2

if players<=10:
    ram = ram
elif players>10 and players<30:
    ram = ram+1
elif players>=30 and players<50:
    ram = ram+3
elif players>=50 and players<80:
    ram = ram+5
elif players>=80 and players<110:
    ram = ram+6
elif players>=110 and players<160:
    ram = ram+8
elif players>=160 and players<=200:
    ram = ram+10
elif players>200:
    ram = ram+14

if jar !="vanilla":
  if plugins<=20:
    ram = ram
  elif plugins>20 and plugins<30:
    ram = ram+1
  elif plugins>=30 and plugins<50:
    ram = ram+2
  elif plugins>=50 and plugins<80:
    ram = ram+3
  elif plugins>=80 and plugins<110:
    ram = ram+4
  elif plugins>=110 and plugins<160:
    ram = ram+5
  elif plugins>=160 and plugins<=200:
    ram = ram+6
  elif plugins>200:
    ram = ram+8

if jar !="vanilla":
  if weight=="yes":
    ram = ram+1
  else:
    ram = ram

print("Ram has been calculated")
print("---------------------------------------------------------------------------------------------------")
print("Calculated ram is " + str(ram) + " (There is more that you should consider, dont rely on this only)")
print("---------------------------------------------------------------------------------------------------")
print("           THIS IS MADE FOR EXPERIMENTAL PURPOSES AND MAY OR MAY NOT BE ACCURATE")
print("---------------------------------------------------------------------------------------------------")
print("Made By aly#1992")

feedback = input("please dm aly#1992 if you have any feedback")
