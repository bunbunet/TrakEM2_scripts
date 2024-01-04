from ini.trakem2 import Project
from ini.trakem2.display import AreaList, Display
from org.scijava.vecmath import Color3f
from customnode import WavefrontExporter, CustomTriangleMesh
from java.io import StringWriter
from ij.text import TextWindow
import csv
import os

#-------------------------------------USER DEFINED OPTIONS----------------------------------------

#Specify the path to the output directory for the .obj files
Output_DIR="G:\\Progetto QA\\RR\\Export Results\\obj2 prova\\" # MUST have ending slash

AreaSelection=["An_LV"]
resample = 50

#to batch open multiple xml file from a single folder set True and specify path
open_first=False
folder = "G:\\Progetto QA\\RR\\Export Results\\Rabies XML 11 2020 bkp\\" # MUST have ending slash

#Set False to keep the projects opened
close_after_opening=True

#--------------------------------------------SCRIPT--------------------------

if open_first:	
	filenames = os.listdir(folder)
	
	for name in filenames:
		if ".xml" in name:
			#open project without display
			project = Project.openFSProject(folder + name, False)

projects=Project.getProjects()
for project in projects:
	specimen= str(project).split(".xml")[0]
	arealists = project.getRootLayerSet().getZDisplayables(AreaList) 
	for arealist in arealists:
		for sel in AreaSelection:
			if sel in arealist.title:
				csv_path = os.path.join(Output_DIR, specimen+"_"+arealist.title+".obj")
				obj_file=open(csv_path,"w+")  
				print("processing: ",arealist.title)
				triangles = arealist.generateTriangles(1, resample)
	 
	# Prepare a 3D Viewer object to provide interpretation
				color = Color3f(1.0, 1.0, 0.0)
				transparency = 0.0
				mesh = CustomTriangleMesh(triangles, color, transparency)
				
	# Write the mesh as Wavefront
				name = specimen +"_"+ arealist.title + "_" + str(arealist.id)
				m = {name : mesh}
				meshData = StringWriter()
				materialData = StringWriter()
				materialFileName = name + ".mtl"
				WavefrontExporter.save(m, materialFileName, meshData, materialData)
	 
	# Show the text of the files in a window
	# then you save it with "File - Save"
	
				#TextWindow(name+".obj", meshData.toString(), 400, 400)
				obj_file.write(meshData.toString())
				obj_file.close
				#TextWindow(materialFileName, materialData.toString(), 400, 400)

print("Done!")