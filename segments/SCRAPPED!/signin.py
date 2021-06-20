import time


#username, level, reputation, inventory)
profiles = [
["dev", 10, 10, ["Dagger"]], 
["Will", 0, 0, [None]]
]
curent_player = None

def signin():
	Name = input("Who are you? ")
	print(f"Hello {Name}, Let me check the profiles...")
	time.sleep(1)

	for x in profiles:
		if Name in x[0]:
			print("Aha! There you are!")
			print("Let me sign you in.")
			curent_player = Name
			print("")
			print(f"Welcome back {curent_player}!")
			break
		else:
			print("No...")
	if curent_player == None:
		print(f"Nope! '{Name}' is not on my list. Bye now!")
		exit()
	print(curent_player)

signin()
print(curent_player)
print("Done.")