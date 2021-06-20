username = [["dev", 10, 10, "Sword", True], ["Dov", 5, 2, "Dagger", False], ["Lanceback", 3, 9, "Bow", False], ["Will", 1, 0, "Rock", False]]



for sublist in username: 
	for username in sublist: 
		print(sublist)
		with open('profiles.txt', 'a+') as file:
			file.write(str(username))
			file.write(" ")
	with open('profiles.txt', 'a+') as file:
		file.write("\r\n")