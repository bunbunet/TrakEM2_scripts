Markers = ['a',' b', 'c ', ' d ']
Label = [1,2,1,4]

#https://tutorialdeep.com/knowhow/update-list-elements-python/

#copy the list (otherwise they will refer to the same python object)
Label_rename=Label[:]

for i in range(len(Label)):
	if Label[i]==1:
		Label[i]="a"

print (Label)





''' non funziona
#copy the list (otherwise they will refer to the same python object)
Label_rename=Label[:]

for i in range(len(Label)):
	print("counter:",i)
	for Lab in Label:
		print("item:",Lab)
		Index=Label.index(Lab)
		if int(Lab)==i:
			print("Match, Index:",Index)
			print(Label_rename)
			Label_rename[Index]=Markers[i]
				
print(Label_rename)
'''