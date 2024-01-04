
X={1:[12,13,14,15],2:[14,15,16,17],6:[21,23,24]}

Names=["ck","cKD","ciccio","io","tu","noi"]

counter=1
for name in Names:
	try:
		X[name]=X.pop(counter)
	except KeyError:
		pass
	counter+=1
	
print(X)
