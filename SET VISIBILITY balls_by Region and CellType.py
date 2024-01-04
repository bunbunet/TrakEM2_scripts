from ini.trakem2.display import Display, Ball

Visible=True
selected_only=True
#select cells based on names written as Cell Type_series_Region_Subregion_SubSubregion_Marker_
#multiple strings can be searched simultanesously if in betwee "" and separated by ,

CellTypes=["STARTER"]
pzs=[""]
Regions=["SVZ"]
Subregions=[""]
SubSubregions=[""]
Markers=[""]

#first hide all balls	
if selected_only:															
	for ball_ob in Display.getFront().getLayerSet().getZDisplayables(Ball):
		ball_ob.visible = False
																																																
#Than unhide the selected ones																																																																																																																																																
for ball_ob in Display.getFront().getLayerSet().getZDisplayables(Ball):
  	title = ball_ob.getTitle()
	g=title.split("_")
	if len(g)>6:
		for CellType in CellTypes:
			for pz in pzs:
				for Region in Regions:
					for Subregion in Subregions:
						for SubSubregion in SubSubregions:
							for Marker in Markers:
								if g[0].find(CellType) !=-1 and g[1].find(pz) !=-1 and g[2].find(Region) !=-1 and g[3].find(Subregion) !=-1 and g[4].find(SubSubregion) !=-1 and g[5].find(Marker) !=-1:
									print(title)
									ball_ob.visible = Visible
