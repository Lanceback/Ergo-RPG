from random import randint, uniform, choice
import time

xy_co = []
Player_x = 7
Player_y = 7

weapons = {
	"None":{"damage":.01, "type":"close"},
	"Rock":{"damage":.05, "type":"range"},
	"Sword":{"damage":1, "type":"close"}, 
	"Dagger":{"damage":.4, "type":"close"}, 
	"Bow":{"damage":.2, "type":"range"}
	}

# define player template
class Player:
	def __init__(self, name , level, rep_med, rep_norse, inventory):
		self.name = name
		self.level = level
		self.xp = 0
		self.hp = int(level)*2
		self.Reputation_Medieval = rep_med
		self.Reputation_Norse = rep_norse
		self.Reputation_Orient = 0
		self.Reputation_Animals = 0
		self.inventory = []
		
	def __repr__(self):
		return f"{self.name} is level {self.level}."
	#Check reputation
	def check_rep(self):
		if self.Reputation_Medieval in range(0, 5):
			print("They seem to tolerate you.")
		else:
			print("null")

	#Get stats
	def stats(self):
		print("----------")
		print(f"Name: {self.name}")
		print(f"Level: {self.level}")
		print(f"Health: {self.hp}")
		print(f"Reputation: {self.rep}")
		self.check_rep()
		#Old check for weapon code
		# if self.inventory["weapon"] == "":
		# 	print("No Weapon equiped.")
		# else:
		# 	print(f"Weapon: {self.inventory['weapon']}")
		print(f"Weapon: {self.inventory['weapon']}")
		input("")
		print("")
	#Level up acording to number provided
	def lvl_up(self, lvls):
		while lvls > 0:
			print("----------")
			self.level += 1
			print("Level up!")
			print(f"Level: {self.level}")
			self.hp = self.level*2
			time.sleep(1)
			lvls -= 1
		self.xp = 0
		print("")
	#Level down acording to number provided
	def lvl_dwn(self, lvls):
		while lvls > 0:
			print("----------")
			if self.level > 0:
				self.level -= 1
				print("you have regressed one level.")
				print(f"Level: {self.level}")
				self.hp = self.level*2
			else:
				self.rep -= 0.5
			time.sleep(1)
			lvls -= 1
		print("")

class npc:
	def __init__(self, level):
		self.name = "Dov"
		self.level = level
		self.hp = 10

class Medieval(npc):
	def __init__(self, level):
		super().__init__(level)
		towns =["Arc", "Lancelot", "Bridgecliff", "Brookton", "Thornton", "Wilmore", "Eastmoor", "Falconworth", "Winchester", "York", "Easton"]
		knight_names = ["Lancer", "Jon", "Don", "Mathew", "John", "Peter", "Edward", "Jacob", "Simon", "Luke", "Noah", "Levi", "Seth", "Malachi", "Elijah", "Jesse", "Steven", "David", "Mark", "Micah", "Joel", "Isiah", "Saul", "Roberts", "Robin", "Joseph", "Joe", "Brian"]
		knight_names_last = ["Lanceback", "Fairfolk", "Goodchild", "Fairchild", "Brash", "Baldhead", "Easton", "Lancelot", "Du Lac", "Dragon", "Gaheris", "Bumble", "Dagonet", "Knight", f"{choice(knight_names)}son", "of Arc", f"of Castle {choice(towns)}", f"of {choice(towns)}"]
		self.armr = randint(0, 2)
		self.atk = round(uniform(.4, .6)*level, 2)
		self.spd = randint(4, 8)
		self.hp = round(int(level)*2)
		self.name = choice(knight_names)
		self.name_last = choice(knight_names_last)
		self.fullname = self.name + " " + self.name_last

class Knight(Medieval):
	def __init__(self, level):
		super().__init__(level)
		self.title = "Sir"
		if self.level > 10:
			self.title = "Lord"
		# elif self.level < 2:
		# 	self.title = None
		self.fullname = self.title +  " " + self.name + " " + self.name_last
		self.armr = randint(4, 8)
		self.spd = randint(8, 12)

	def __repr__(self):
		if self.title != None:
			self.fullname = self.title +  " " + self.name + " " + self.name_last
			return f"{self.fullname} is a level {self.level} knight."
		else:
			return f"{self.name} {self.name_last} is level {self.level}."
			self.fullname = self.name + " " + self.name_last

class Archer(Medieval):
	def __init__(self, level):
		super().__init__(level)
		self.title = None
		self.atk = round(uniform(.2, .5)*lvl, 2)
		self.spd = randint(2, 5)

	def __repr__(self):
		
		return f"{self.name} {self.name_last} is a level {self.level} archer."

class Soldier(Medieval):
	def __init__(self, level):
		super().__init__(level)
		self.title = None
		self.atk = round(uniform(.1, .3)*lvl, 2)
		self.spd = randint(4, 6)
		self.armr = randint(2, 6)

	def __repr__(self):
		return f"{self.name} {self.name_last} is a level {self.level} foot soldier."

class Guard(Medieval):
	def __init__(self, level):
		super().__init__(level)
		self.title = None
		self.atk = round(uniform(.2, .5)*lvl, 2)
		self.spd = randint(2, 5)
		self.armr = randint(4, 6)

	def __repr__(self):
		return f"Guard {self.name} {self.name_last} is level {self.level}."

class Norse(npc):
	def __init__(self, level):
		super().__init__(level)
		viking_names = ["Erik", "Leif", "Thor", "Orn", "Styr", "Ragnar", "Loki", "Dan", "Orrin", "Ivar", "Ham", "Bjorn", "Arne", "Aesir", "Ulf", "Rune", "Frode", "Gisli", "Erling", "Roar", "Selby", "Herleif", "Gunnar", "Vidar", "Magnus", "Aric", "Ivar", "Arkyn", "Freyre", "Tor", "Yrsa", "Arne", "Bo", "Knud", "Njal", "Sten", "Skarde", "Torsten"]
		viking_titles = ["The Red", "The Lucky", "The Thunder", "The Small", "The Flounder", "The Storm", "of The Sea", "The Pillager", "The Bald", "The Proud", "The Bold", "The Bluetooth", f"{choice(viking_names)}son"]
		self.name = choice(viking_names)
		self.title = choice(viking_titles)
		self.spd = (randint(6, 20))
		self.hp = round((int(level)*2) + (level/self.spd), 2)
		
class Warior(Norse):
	def __init__(self, level):
		super().__init__(level)
		self.armr = randint(1, 2)
		self.atk = round(uniform(.6, 1.2)*level, 2)
		self.fullname = self.name + " " + self.title

	def __repr__(self):
		return f"{self.name} {self.title} is level {self.level}."

class Radier(Norse):
	def __init__(self, level):
		super().__init__(level)
		self.armr = randint(1, 4)
		self.atk = round(uniform(.6, 1)*level, 2)
		self.fullname = self.name + " " + self.title

	def __repr__(self):
		return f"{self.name} {self.title} is level {self.level}."

class Hunter(Norse):
	def __init__(self, level):
		super().__init__(level)
		self.armr = randint(1, 4)
		self.atk = round(uniform(.6, 1)*level, 2)
		self.fullname = self.name + " " + self.title

	def __repr__(self):
		return f"{self.name} {self.title} is level {self.level}."

def fight(enemy_type, enemy_lvl):
	#variables that control how the fight goes and tracks who wins
	HP = 10.0
	battle_state = None
	enemy_lvl = int(enemy_lvl)
	if enemy_type == "Knight":
		enemy = Knight(enemy_lvl)
	elif enemy_type == "Archer":
		enemy = Archer(enemy_lvl)
	elif enemy_type == "Soldier":
		enemy = Soldier(enemy_lvl)
	elif enemy_type == "Guard":
		enemy = Guard(enemy_lvl)
	elif enemy_type == "Warior":
		enemy = Warior(enemy_lvl)
	else:
		print("Error... Unrecognized enemy type.")
		exit()

	#begin!

	print("")
	print("")
	print(repr(enemy))
	#The battle loop
	while battle_state == None:
		time.sleep(2)
		#genearate random numbers for the questions
		number1 = randint(0, 10)
		number2 = randint(0, 10)

		#set the stopwatch...
		time_0 = time.time()

		#list stats
		print("")
		print(f"Your health is at {HP}.")
		print(f"{enemy.fullname}'s health' is at {enemy.hp}.")

		#ask question
		while True:
			try:
				answer = int(input(f"{number1} X {number2} = "))
				break
			except ValueError:
				print("Nope!")

		#get time it took to answer
		elapsed = round(time.time()-time_0, 2)

		#check answer
		if  answer == number1*number2:
			damage = round(randint(5, 10)/(elapsed * enemy.armr), 2)
			print("Correct!")
			print("------------")
			if damage > 0:
				if damage < 1:
					print(f"You scratched {enemy.fullname} for {damage} points of damage.")
					if randint(0,5):
						print(f"{enemy.fullname} is not impressed.")
				else:
					print(f"You did {damage} points of damage.")
				enemy.hp = round(enemy.hp - damage, 2)
			else:
				print(f"You were too slow, {enemy.fullname} blocked your attack!")
				if randint(0,1):
					print(f"{enemy.fullname} seems to move a little faster.")
					enemy.spd -= 0.25

			if elapsed >= enemy.spd:
				damage = round(enemy.atk/elapsed, 2)
				print(f"You took {damage} points of damage.")
				HP = round(HP - damage, 2)

		else:
			damage = round(enemy.atk*(elapsed/2), 2)
			print("Incorrect")
			print(f"The answer is {number1*number2}")
			time.sleep(0.5)
			print("------------")
			HP = HP - damage
			print(f"You took {damage} points of damage!")

		if randint(0,2) == 2:
			print(f"{enemy.fullname} is tiring.")
			enemy.spd += 0.5

		time.sleep(1)
		if enemy.hp <= 0.0:
			print("You Won!")
			battle_state = "w"
			time.sleep(2)
		elif HP <= 0.0:
			print("You Lost!")
			battle_state = "l"
			exit()
			

def new_map():
	for i in range(0, 15): 
    	# Append an empty sublist inside the list 
		xy_co.append([]) 
		for j in range(0, 15): 
			xy_co[i].append([])
		
	for i in range(0, 15):  
		for j in range(0, 15): 
			map_int = uniform(0, 10)
			print(map_int)
			# make wall
			if i == 0 or i == 14 or j == 0:
				xy_co[j][i] = 1
				xy_co[i][j] = 1
			#make player
			elif j == 7 and i == 7:
				xy_co[j][i] = 2
			# make chest
			elif map_int > 9.6:
				xy_co[j][i] = 4
				xy_co[i][j] = 4
			# make basic enemy
			elif map_int > 8.5:
				xy_co[j][i] = 3
				xy_co[i][j] = 3
			# make norse warrior
			elif map_int > 8.5:
				xy_co[j][i] = 5
				xy_co[i][j] = 5
			# empty space
			else:
				xy_co[j][i] = 0
				xy_co[i][j] = 0

def move():
	global Player_x
	global Player_y
	#show map
	while True:
		print(f"You are at {Player_x} X and {Player_y} Y. ")
		for x in xy_co:
   			print(x)
   			time.sleep(0.02)

 
		print("Which direction would you like to move? ")
		Action = input("W A S D :")

		def movementValues(valueX, valueY):
			global Player_x
			global Player_y

			if xy_co[Player_x - valueX][Player_y - valueY] == 0:
				xy_co[Player_x][Player_y] = 0
				xy_co[Player_x - valueX][Player_y - valueY] = 2
				
				Player_x = Player_x - valueX
				Player_y = Player_y - valueY
				print("You have moved Forward.")
			elif xy_co[Player_x - valueX][Player_y - valueY] == 1:
				print("That's a wall.")
			elif xy_co[Player_x - valueX][Player_y - valueY] == 2:
				print("That's uhh... you?")
			elif xy_co[Player_x - valueX][Player_y - valueY] == 3:
				print("Knight encountered!")
				xy_co[Player_x - valueX][Player_y - valueY] = 2
				xy_co[Player_x][Player_y] = 0
				Player_x = Player_x - valueX
				#start encounter function for this enemy type
				fight("Knight", randint(1, 5))
			elif xy_co[Player_x - valueX][Player_y - valueY] == 4:
				print("Norse warrior encountered!")
				xy_co[Player_x - valueX][Player_y - valueY] = 2
				xy_co[Player_x][Player_y] = 0
				Player_x = Player_x - valueX
				#start encounter function for this enemy type
				fight("Warior", 2)
			else:
				print("Mysterious data uncovered! What is it? It isn't programed in.")



		if Action == "W" or Action == "w":


			movementValues(1, 0)
			# if xy_co[Player_x - 1][Player_y] == 0:
			# 	xy_co[Player_x - 1][Player_y] = 2
			# 	xy_co[Player_x][Player_y] = 0
			# 	Player_x = Player_x - 1
			# 	print("You have moved Forward.")
			# elif xy_co[Player_x - 1][Player_y] == 1:
			# 	print("That's a wall.")
			# elif xy_co[Player_x - 1][Player_y] == 3:
			# 	print("Enemy encountered!")
			# 	xy_co[Player_x - 1][Player_y] = 2
			# 	xy_co[Player_x][Player_y] = 0
			# 	Player_x = Player_x - 1
			# 	#start encounter function for this enemy type
			# 	fight("Knight", 2)
			# elif xy_co[Player_x - 1][Player_y] == 3:
			# 	print("Enemy encountered!")
			# 	xy_co[Player_x - 1][Player_y] = 2
			# 	xy_co[Player_x][Player_y] = 0
			# 	Player_x = Player_x - 1
			# 	#start encounter function for this enemy type
			# 	fight("Warior", 2)
			# else:
			# 	print("Mysterious data uncovered! What is it? It isn't programed in.")
		
		elif Action == "A" or Action == "a":
			movementValues(0, 1)
			# if xy_co[Player_x][Player_y - 1] == 0:
			# 	xy_co[Player_x][Player_y - 1] = 2
			# 	xy_co[Player_x][Player_y] = 0
			# 	Player_y = Player_y - 1
			# 	print("You have moved Left.")
			# elif xy_co[Player_x][Player_y - 1] == 1:	
			# 	print("That's a wall.")
			# elif xy_co[Player_x][Player_y - 1] == 3:
			# 	print("Enemy encountered!")
			# 	xy_co[Player_x][Player_y - 1] = 2
			# 	xy_co[Player_x][Player_y] = 0
			# 	Player_y = Player_y - 1
			# 	#start encounter function for this enemy type
			# 	fight("Knight", 2)
			# else:
			# 	print("Mysterious data uncovered! What is it? It isn't programed in.")
			
		elif Action == "S" or Action == "s":

			movementValues(-1, 0)
			# if xy_co[Player_x + 1][Player_y] == 0:
			# 	xy_co[Player_x + 1][Player_y] = 2
			# 	xy_co[Player_x][Player_y] = 0
			# 	Player_x = Player_x + 1
			# 	print("You have moved Backwards.")
			# elif xy_co[Player_x + 1][Player_y] == 1:
			# 	print("That's a wall.")
			# elif xy_co[Player_x + 1][Player_y] == 3:
			# 	print("Enemy encountered!")
			# 	xy_co[Player_x + 1][Player_y] = 2
			# 	xy_co[Player_x][Player_y] = 0
			# 	Player_x = Player_x + 1
			# 	#start encounter function for this enemy type
			# 	fight("Knight", 2)
				
			# else:
			# 	print("Mysterious data uncovered! What is it? It isn't programed in.")

		elif Action == "D" or Action == "d":

			movementValues(0, -1)

			# if xy_co[Player_x][Player_y + 1] == 0:
			# 	xy_co[Player_x][Player_y + 1] = 2
			# 	xy_co[Player_x][Player_y] = 0
			# 	Player_y = Player_y + 1
			# 	print("You have moved Left.")
			# elif xy_co[Player_x][Player_y + 1] == 1:
			# 	print("That's a wall.")
			# elif xy_co[Player_x][Player_y + 1] == 3:
			# 	print("Enemy encountered!")
			# 	xy_co[Player_x][Player_y + 1] = 2
			# 	xy_co[Player_x][Player_y] = 0
			# 	Player_y = Player_y + 1
			# 	#start encounter function for this enemy type
			# 	fight("Knight", 2)
			# else:
			# 	print("Mysterious data uncovered! What is it? It isn't programed in.")
		
		else:
			print("")
			print("Which direction would you like to move? ")

inventories = {
	"Dov":[
	{"Name":"Knife", "Type":"melee", "Damage":4, "Speed":6, "Effect": ["bleeding", "backstab"], "Equiped": True}, 
	{"Name":"Dov's Cloak", "Type":"clothing", "Protection":1, "Color":"Black", "Effect": ["shadow", "silent", "suspicion"], "Equiped": True}, 
	{"Name":"Dart", "Type":"ranged", "Damage":3, "Range":8, "Speed":10, "Effect": ["silent", "piercing"], "Equiped": False} 
	], 

	"Will":[
	{"Name":"Bow", "Type":"ranged", "Damage":4, "Range":9, "Speed":10, "Effect": [], "Equiped": True}, 
	{"Name":"will's Cloak", "Type":"clothing", "Protection":1, "Color":"Green", "Effect": ["swift"], "Equiped": True}, 
	{"Name":"Short Sword", "Type":"melee", "Damage":5, "Speed":4, "Effect": ["guard-break"], "Equiped": False}, 
	{"Name":"Arrow", "Type":"ammo", "Amount":12, "Effect": ["piercing"]}
	], 

	"Silverstr":[
	{"Name":"Sword", "Type":"melee", "Damage":6, "Speed":3, "Effect": ["guard-break", "stun"], "Equiped": True}, 
	{"Name":"Silverstr's Armor", "Type":"armor", "Protection":6, "Color":"Red", "Effect": ["slow", "resist"], "Equiped": True}, 
	{"Name":"Shield", "Type":"defense", "Damage":2, "Speed":3, "Effect": ["resist", "full-block"], "Equiped": True}
	]
	}

#saved characters (temporary solution)
profiles = [
	{"Name":"Dov", "Level":10, "Reputation_Medieval":2, "Reputation_Norse":6, "Inventory":inventories["Dov"]}, 
	{"Name":"Will", "Level":1, "Reputation_Medieval":5, "Reputation_Norse":4, "Inventory":inventories["Will"]},
	{"Name":"Silverstr", "Level":1, "Reputation_Medieval":7, "Reputation_Norse":1, "Inventory":inventories["Silverstr"]}
	]
# profiles = [["Dov", 10, 4, "Sword"], ["Will", 1, 0, "Bow"], ["Silverstr", 1, 0, "Sword"]]

# #Begin login
login = input("Who are you? ")
#If developer login
if login == "dev":
	disguise_name = input("Hello Developer! What would you like to go by? ")
	while True:
		try:
			disguise_lvl = int(input(f"Accepted name: {disguise_name}, what level would you like to be? "))
			if disguise_lvl in range(0, 10):
				break
			else:
				print("That's not a valid level.")
		except ValueError:
			print("That's not a valid level.")
	disguise_weapon = input(f"Accepted level: {disguise_lvl}, what weapon would you like? ")
	while True:
		if disguise_weapon not in weapons:
			print("Weapon not available.")
			disguise_weapon = input(f"Accepted level: {disguise_lvl}, what weapon would you like? ")
		else:
			break
	curent_player = Player(disguise_name, disguise_lvl, 0, 0, disguise_weapon)
	#new login
else:
	print("Signing you in...")
	curent_player = Player(login, 1, 0, 0, "None")
	for n in profiles:
		if login == n["Name"]:
			# print(f"Loading {login}...")
			# print(f"Name: {n["Name"]}")
			# print(f"Level: {n["Level"]}")
			# print(f"Reputation with Medieval folk: {n["Reputation_Medieval"]}")
			# print(f"Reputation with Norse people: {n["Reputation_Norse"]}")
			curent_player = Player(n["Name"], n["Level"], n["Reputation_Medieval"], n["Reputation_Norse"], n["Inventory"])


new_map()
move()
# fight("Soldier", 1)
# fight("Soldier", 2)
# fight("Soldier", 3)

# fight("Knight", 1)
# fight("Knight", 2)
# fight("Knight", 3)

# fight("Warior", 1)
# fight("Warior", 2)
# fight("Warior", 3)


# fight("Knight", 4)
# fight("Knight", 5)
# fight("Knight", 6)