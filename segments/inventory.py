import time

weapons = {
"None":{"damage":0, "type":"close"},
"Rock":{"damage":.05, "type":"range"},
"Sword":{"damage":1, "type":"close"}, 
"Dagger":{"damage":.4, "type":"close"}, 
"Bow":{"damage":.2, "type":"range"}
}
# define player template
class Player:
	def __init__(self, name , level, rep, inventory):
		self.name = name
		self.level = level
		self.xp = 0
		self.hp = int(level)*2
		self.rep = rep
		self.inventory = ({f"weapon":inventory})
		
	def __repr__(self):
		return f"{self.name} is level {self.level}."
	#Check reputation
	def check_rep(self):
		if int(self.rep) > 10:
			print("You are a Hero.")
		elif int(self.rep) > 5:
			print("You are somewhat famous.")
		elif int(self.rep) > 2:
			print("You are well liked.")
		elif int(self.rep) > -1:
			print("You are fairly average.")
		elif int(self.rep) > -5:
			print("You aren't well liked.")
		elif int(self.rep) > -10:
			print("You generally disliked.")
		elif int(self.rep) <= -10:
			print("You are a villain.")
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

#saved characters (temporary solution)
profiles = [["Dov", 10, 4, "Sword"], ["Will", 1, 0, "Bow"], ["Silverstr", 1, 0, "Sword"]]

#login loop
while True:
	#Begin login
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

		disguise_rep = input(f"Accepted level: {disguise_lvl}, what would you like your general reputation to be? ")
		disguise_weapon = input(f"Accepted reputation: {disguise_lvl}, what weapon would you like? ")
		while True:
			if disguise_weapon not in weapons:
				print("Weapon not available.")
				disguise_weapon = input(f"Accepted reputation: {disguise_lvl}, what weapon would you like? ")
			else:
				break
		curent_player = Player(disguise_name, disguise_lvl, disguise_rep, disguise_weapon)
	#new login
	else:
		print("Signing you in...")
		curent_player = Player(login, 1, 0, "None")
		for n in profiles:
			if login == n[0]:
				print(f"Loading {login}...")
				print(f"Name: {n[0]}")
				print(f"Level: {n[1]}")
				print(f"Reputation: {n[2]}")
				print(f"Weapon: {n[3]}")
				curent_player = Player(n[0], n[1], n[2], n[3])

	#general game loop
	while True:
		print("----------")
		print("move")
		print("stats")
		print("logout")
		print("exit")
		print("----------")
		usr_says = input("")
		if usr_says == "move":
			print(usr_says)
		elif usr_says == "stats":
			curent_player.stats()
		elif usr_says == "logout":
			break
		elif usr_says == "exit":
			exit()
		else:
			print("Invalid action")