from ini.trakem2.display import Display, Ball

Visible=True

CellTypes=["PreS"]
pzs=[""]
Regions=[""]
Subregions=[""]
SubSubregions=[""]
Markers=[""]
																
for ball_ob in Display.getFront().getLayerSet().getZDisplayables(Ball):
  	title = ball_ob.getTitle()
	g=title.split("_")
	if len(g)>6:
		for CellType in CellTypes:
			for pz in pzs:
				for Rigion in Regions:
					for Subregion in Subregions:
						for SubSubregion in SubSubregions:
							for Marker in Markers:
								if g[0].find(CellType) !=-1 and g[1].find(pz) !=-1:
									print(title)
									ball_ob.visible = Visible
