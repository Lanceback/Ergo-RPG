import random
xy_co = []

for i in range(0, 15): 
    # Append an empty sublist inside the list 
	xy_co.append([]) 
	for j in range(0, 15): 
		xy_co[i].append([])
		
for i in range(0, 15):  
	for j in range(0, 15): 
		map_int = random.uniform(0, 10)
		print(map_int)
		if i == 0 or i == 14 or j == 0:
			xy_co[j][i] = 1
			xy_co[i][j] = 1
		elif j == 7 and i == 7:
			xy_co[j][i] = 2
		elif map_int > 9.6:
			xy_co[j][i] = 4
			xy_co[i][j] = 4
		elif map_int > 8.5:
			xy_co[j][i] = 3
			xy_co[i][j] = 3
		else:
			xy_co[j][i] = 0
			xy_co[i][j] = 0

for x in xy_co:
	print(x)