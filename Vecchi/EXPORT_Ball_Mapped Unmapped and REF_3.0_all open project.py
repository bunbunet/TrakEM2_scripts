from ini.trakem2.display import Display, Ball
from ij.text import TextWindow
from ini.trakem2 import Project
import os
import csv

#export id, title and coordinates of balls in balls objects,
#split names according to the convention : Type_pz_region_subregion_sub-subregion_label_notes
# BE CAREFUL! ONLY ONE PROJECT SHOULD BE OPEN, otherwise specimen names could not correspond
#to the display balls exported

Output_DIR_mapped="G:\\Progetto QA\\RR\\Export Results\\txt\\" # MUST have ending slash
Output_DIR_REF="G:\\Progetto QA\\RR\\Export Results\\obj\\" # MUST have ending slash
Output_DIR_unmapped="G:\\Progetto QA\\RR\\Export Results\\unmapped\\" # MUST have ending slash

#Setting true text windows with the results are directly opened in ImageJ
open_text_window=False

#set as "" to process only already opened projects
#set a path to open all the .xml file in a folder

batch_folder="G:\\Progetto QA\\RR\\Export Results\\txt\\"
filenames = os.listdir(folder)

if len(batch_folder)=0:
	for name in filenames:
		if ".xml" in name:
			#open project without display
			project = Project.openFSProject(batch_folder + name, False)
			specimen= str(name).split(".xml")[0]
			print(specimen)

projects=Project.getProjects()
for project in projects:
	specimen= str(project).split(".xml")[0]
	ball_obs = project.getRootLayerSet().getZDisplayables(Ball)
	print(specimen, len(ball_obs))
	# One entry for each id,x,y,z,r 
	rows = []
	rows2= []
	rows3= []
 	txt1_path = os.path.join(Output_DIR_mapped, specimen+"_"+"mapped"+".txt")
 	txt2_path = os.path.join(Output_DIR_unmapped, specimen+"_"+"unmapped"+".txt")
 	txt3_path = os.path.join(Output_DIR_REF, specimen+"_"+"REF"+".txt")
	txt1_file=open(txt1_path,"w+")
	txt2_file=open(txt2_path,"w+")
	txt3_file=open(txt3_path,"w+")   
	# Iterate every Ball instance, which contains one or more x,y,z,r balls
	for ball_ob in ball_obs:
		id = ball_ob.getId()
	 	title = ball_ob.getTitle()
		g=title.split("_")
		# Iterate every x,y,z,r ball of a Ball instance, calibrated
		wbs = ball_ob.getWorldBalls()
		for ball_coords in wbs:
	    # Store every ball as a row with id, x, y, z, r; for brain mapped balls the name is parsed into separated columns 
	    # this is not necessary, but facilitate analysis in softwares where parsing the names is not as straightforward as in python (i.e Excel, SPSS, R etc..)
				if len(g)>6: #Balls 
					rows.append(str(specimen)+","+str(id)+","+g[0]+","+g[1]+","+g[2]+","+g[3]+","+g[4]+","+g[5]+","+g[6]+","+title+","+",".join(str(c) for c in ball_coords))
				else: # add all other balls to a separate list.
					if "REF" in title:
						rows3.append(str(specimen)+","+str(id)+","+title+","+",".join(str(c) for c in ball_coords))
					else:
						rows2.append(str(specimen)+","+str(id)+","+title+","+",".join(str(c) for c in ball_coords))
	
	#here the header for the mapped file
	rows.insert(0,str("Specimen")+","+str("ID")+","+str("CellType")+","+str("pz")+","+str("Region")+","+str("Subregion")+","+str("SubSubregion")+","+str("Marker")+","+str("notes")+","+str("FullName")+","+str("x")+","+str("y")+","+str("z")+","+str("radius"))

	csv = "\n".join(rows)
	csv2 = "\n".join(rows2)
	csv3 = "\n".join(rows3)
	
	txt1_file.write("\n".join(rows))
	txt2_file.write("\n".join(rows2))
	txt3_file.write("\n".join(rows3))
	
	txt1_file.close
	txt2_file.close
	txt3_file.close
	
	if open_text_window: 
		t = TextWindow(Specimen+"_balls", csv, 400, 400)
		t2 = TextWindow(Specimen+"_unmapped", csv2, 400, 400)
		t3 = TextWindow(Specimen+"_REF", csv2, 400, 400)
