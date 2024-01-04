from ini.trakem2.display import Display, Ball
from ij.text import TextWindow
from ini.trakem2 import Project
#export id, title and coordinates of balls in balls objects,
#split names according to the convention : Type_pz_region_subregion_sub-subregion_label_notes

ProjName= Project.getProjects()
Spec= str(ProjName).split(".xml")[0]
Specimen=Spec.split("[")[1]

#Uncomment to give a specific name to the specimen
#Specimen="RRGEF6"

ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)
 
# One entry for each id,x,y,z,r 
rows_Mapped = []
rows_Unmapped= []
rows_REF= []
 
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
				rows_Mapped.append(str(Specimen)+","+str(id)+","+g[0]+","+g[1]+","+g[2]+","+g[3]+","+g[4]+","+g[5]+","+g[6]+","+title+","+",".join(str(c) for c in ball_coords))
			elif "REF" in title:
				rows_REF.append(str(Specimen)+","+str(id)+","+title+","+",".join(str(c) for c in ball_coords))
			else: 
				rows_Unmapped.append(str(Specimen)+","+str(id)+","+title+","+",".join(str(c) for c in ball_coords))
#here the header
rows_Mapped.insert(0,str("Specimen")+","+str("ID")+","+str("CellType")+","+str("pz")+","+str("Region")+","+str("Subregion")+","+str("SubSubregion")+","+str("Marker")+","+str("notes")+","+str("FullName")+","+str("x")+","+str("y")+","+str("z")+","+str("radius"))

csv = "\n".join(rows_Mapped)
csv2 = "\n".join(rows_Unmapped)
csv3 =  "\n".join(rows_REF)
 
t = TextWindow(str(ProjName)+"balls COORD", csv, 400, 400)
t2 = TextWindow(str(ProjName)+"unmapped balls", csv2, 400, 400)
t3 = TextWindow(str(ProjName)+"unmapped REF", csv3, 400, 400)