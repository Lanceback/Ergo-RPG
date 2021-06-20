import random
import time

Health = 10
Reputation = 0

Enemy_health = 10

def Check_rep():
	print(f"Your Reputation is {Reputation}.")
	if Reputation > 10:
		print("You are a Hero.")
	elif Reputation > 5:
		print("You are somewhat famous.")
	elif Reputation > 2:
		print("You are well liked.")
	elif Reputation > -1:
		print("You are fairly average.")
	elif Reputation > -5:
		print("You aren't well liked.")
	elif Reputation > -10:
		print("You generally disliked and looked down on.")
	elif Reputation <= -10:
		print("You are a villain.")

print("You have encountered an enemy knight!")

while Enemy_health >= 1:
	print(f"Enemy health is {Enemy_health}")
	print(f"Your health is {Health}")
	Action = input("Do you wish to F\u0332ight, or R\u0332un? ")

	if Action == "F" or Action == "f" or Action == "Fight" or Action == "fight":
		print("")
		time.sleep(1)
		print("You attack")
		Enemy_health = Enemy_health - round(random.uniform(0,1), 1)

		if round(random.randint(0,1)) == 1:
			print("The enemy attacked.")
			Health - round(random.uniform(0,1), 2)

	elif Action == "R" or Action == "r" or Action == "Run" or Action == "run":
		Randomizer = random.randint(1,3)

		if Randomizer == 1:
			print("")
			time.sleep(1)
			print("You run from the battle.")
			Reputation = Reputation - 1
			Check_rep()
			break

		print("")
		time.sleep(1)
		print("You couldn't get away fast enough.")
		eputation = Reputation - .1
		Health = Health - round(random.uniform(0,2), 2)
		print("")

	else:
		print("The knight attacked you!")
		Health = Health - round(random.uniform(0,1), 2)

print("Battle Over")