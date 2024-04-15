import os, re

folder = "C:/Users/feder/Documents/LAB/LGE_interneurons_postnatal/P3to10.4/MAX/"

filenames = os.listdir(folder)
zList = []
for filename in filenames:
	try:
		found = re.search(".*_z(.+?)_.*\.tif", filename).group(1)
	except AttributeError:
	    # AAA, ZZZ not found in the original string
	    found = ''
	zList.append(found)

zList=list(sorted(set(zList)))

for z in zList:
	print(z)