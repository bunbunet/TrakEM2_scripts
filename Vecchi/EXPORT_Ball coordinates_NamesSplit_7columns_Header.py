from ini.trakem2.display import Display, Ball
from ij.text import TextWindow
from ini.trakem2 import Project
#export id, title and coordinates of balls in balls objects,
#split names according to the convention : Type_pz_region_subregion_sub-subregion_label_notes
#Specify the name of the specimen

Specimen="RR2"

ProjName= Project.getProjects()

ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)
 
# One entry for each id,x,y,z,r 
rows = []
 
# Iterate every Ball instance, which contains one or more x,y,z,r balls
for ball_ob in ball_obs:
	id = ball_ob.getId()
 	title = ball_ob.getTitle()
	g=title.split("_")
	# Iterate every x,y,z,r ball of a Ball instance, calibrated
	wbs = ball_ob.getWorldBalls()
	for ball_coords in wbs:
    # Store every ball as a row with id, x, y, z, r
			if len(g)>6:
				rows.append(str(Specimen)+","+str(id)+","+g[0]+","+g[1]+","+g[2]+","+g[3]+","+g[4]+","+g[5]+","+g[6]+","+title+","+",".join(str(c) for c in ball_coords))
			else:
				rows.append(str(Specimen)+","+str(id)+","+title+","+",".join(str(c) for c in ball_coords))
#here the header
rows.insert(0,str("Specimen")+","+str("ID")+","+str("CellType")+","+str("pz")+","+str("Region")+","+str("Subregion")+","+str("SubSubregion")+","+str("Marker")+","+str("notes")+","+str("FullName")+","+str("x")+","+str("y")+","+str("z")+","+str("radius"))

csv = "\n".join(rows)
 
t = TextWindow(str(ProjName)+"balls COORD", csv, 400, 400)