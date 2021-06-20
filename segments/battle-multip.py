from random import randint, uniform, choice
import time

# rework classes so enemy and all generic npcs are a subclass of npc and all enemy types(viking, mediviel) are a subclass of enemy and all varients are a subcalss of that.
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
		self.armr = randint(2, 8)
		self.atk = round(uniform(.4, .6)*level, 2)
		self.spd = randint(4, 10)
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
		elif self.level < 2:
			self.title = None
		self.fullname = self.title +  " " + self.name + " " + self.name_last

	def __repr__(self):
		if self.title != None:
			return f"{self.title} {self.name} {self.name_last} is level {self.level}."
			self.fullname = self.title +  " " + self.name + " " + self.name_last
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

	def __repr__(self):
		return f"{self.name} {self.name_last} is a level {self.level} foot soldier."

class Guard(Medieval):
	def __init__(self, level):
		super().__init__(level)
		self.title = None
		self.atk = round(uniform(.2, .5)*lvl, 2)
		self.spd = randint(2, 5)

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
		self.armr = randint(1, 4)
		self.atk = round(uniform(.6, 1)*level, 2)
		self.fullname = self.name + " " + self.title

	def __repr__(self):
		return f"{self.name} {self.title} is level {self.level}."

def fight(enemy_type):
	#variables that control how the fight goes and tracks who wins
	HP = 10.0
	battle_state = None
	enemy = enemy_type(1)
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
				print("NoPE!")
			

		#get time it took to answer
		elapsed = round(time.time()-time_0, 2)

		#check answer
		if  answer == number1*number2:
			damage = round(elapsed - (enemy.armr / randint(1, 4)), 2)
			print("Correct")
			print("------------")
			print(f"You did {damage} points of damage.")
			enemy.hp = round(enemy.hp - (2/elapsed), 2)

			if elapsed >= enemy.spd:
				damage = round(enemy.atk/elapsed, 2)
				print(f"You took {damage} points of damage.")
				HP = HP - damage

		else:
			damage = round(enemy.atk*(elapsed/2), 2)
			print("Incorrect")
			print(f"The answer is {number1*number2}")
			time.sleep(0.5)
			print("------------")
			HP = HP - damage
			print(f"You took {damage} points of damage!")

	time.sleep(1)
	if HP >= 0.0:
		print("You Won!")
		battle_state = "w"
	elif enemy.hp >= 0.0:
		print("You Lost!")
		battle_state = "l"
	time.sleep(2)


fight(Soldier)

fight(Guard)

fight(Archer)

fight(Knight)

fight(Warior)

fight(Warior)