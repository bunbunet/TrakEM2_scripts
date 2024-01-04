from ini.trakem2.display import AreaList, Display, Patch

arealists=Display.getFront().getLayerSet().getZDisplayables(AreaList)

selection=["STR_MOp"]

for arealist in arealists:
	for sel in selection:
		if sel in arealist.title:
			#print(arealist.title)
			arealist.visible = True
						