import random
import time

xy_co = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 3, 0, 0, 1, 1, 1, 1, 0, 1], 
[1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1], 
[1, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 1, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

Player_x = 7
Player_y = 7




def move():
	#show map
	print(f"You are at {Player_x} X and {Player_y} Y. ")
	for x in xy_co:
   		print(x)
   		# time.sleep(0.05)

 
	print("Which direction would you like to move? ")
	Action = input("W A S D :")
	if Action == "W" or Action == "w":

		if xy_co[Player_x - 1][Player_y] == 0:
			xy_co[Player_x - 1][Player_y] = 2
			xy_co[Player_x][Player_y] = 0
			Player_x = Player_x - 1
			print("You have moved Forward.")
		elif xy_co[Player_x - 1][Player_y] == 1:
			print("That's a wall.")
		elif xy_co[Player_x - 1][Player_y] == 3:
			print("Enemy encountered!")
			xy_co[Player_x - 1][Player_y] = 2
			xy_co[Player_x][Player_y] = 0
			Player_x = Player_x - 1
			#start encounter function for this enemy type
		else:
			print("Mysterious data uncovered! What is it? It isn't programed in.")
		
	elif Action == "A" or Action == "a":

		if xy_co[Player_x][Player_y - 1] == 0:
			xy_co[Player_x][Player_y - 1] = 2
			xy_co[Player_x][Player_y] = 0
			Player_y = Player_y - 1
			print("You have moved Left.")
		elif xy_co[Player_x][Player_y - 1] == 1:
			print("That's a wall.")
		elif xy_co[Player_x][Player_y - 1] == 3:
			print("Enemy encountered!")
			xy_co[Player_x][Player_y - 1] = 2
			xy_co[Player_x][Player_y] = 0
			Player_y = Player_y - 1
			#start encounter function for this enemy type
		else:
			print("Mysterious data uncovered! What is it? It isn't programed in.")
		
	elif Action == "S" or Action == "s":

		if xy_co[Player_x + 1][Player_y] == 0:
			xy_co[Player_x + 1][Player_y] = 2
			xy_co[Player_x][Player_y] = 0
			Player_x = Player_x + 1
			print("You have moved Backwards.")
		elif xy_co[Player_x + 1][Player_y] == 1:
			print("That's a wall.")
		elif xy_co[Player_x + 1][Player_y] == 3:
			print("Enemy encountered!")
			xy_co[Player_x + 1][Player_y] = 2
			xy_co[Player_x][Player_y] = 0
			Player_x = Player_x + 1
			#start encounter function for this enemy type
		else:
			print("Mysterious data uncovered! What is it? It isn't programed in.")

	elif Action == "D" or Action == "d":

		if xy_co[Player_x][Player_y + 1] == 0:
			xy_co[Player_x][Player_y + 1] = 2
			xy_co[Player_x][Player_y] = 0
			Player_y = Player_y + 1
			print("You have moved Left.")
		elif xy_co[Player_x][Player_y + 1] == 1:
			print("That's a wall.")
		elif xy_co[Player_x][Player_y + 1] == 3:
			print("Enemy encountered!")
			xy_co[Player_x][Player_y + 1] = 2
			xy_co[Player_x][Player_y] = 0
			Player_y = Player_y + 1
			#start encounter function for this enemy type
		else:
			print("Mysterious data uncovered! What is it? It isn't programed in.")
		
	else:
		print("")
		print("Which direction would you like to move? ")