from ini.trakem2 import Project
from ini.trakem2.display import AreaList, Display
from org.scijava.vecmath import Color3f
from customnode import WavefrontExporter, CustomTriangleMesh
from java.io import StringWriter
from ij.text import TextWindow
import csv
import os

#This Macro Export mesh from Arealists. It process all the opened xml files and save the obj files in a 
#user specified folder. Options include the selection of the objects to export and the possibility
#to batch open all the .xml files in a folder

#-------------------------------------USER DEFINED OPTIONS----------------------------------------

#Specify the path to the output directory for the .obj files
Output_DIR="G:\\Progetto QA\\RR\\Export Results\\obj2 prova\\" # MUST have ending slash

#Export only arealists containing specific string codes, it accepts lists e.g. ["An_LV","An_InjQA"] 
AreaSelection=["An_LV"]

#Increasing the resempling will reduce the complexity of the mesh
resample = 50

#to batch open multiple xml file from a single folder set True and specify path
open_first=True
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
	print(specimen)
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
	
				#TextWindow(name+".obj", meshData.toString(), 400, 400)
				obj_file.write(meshData.toString())
				obj_file.close
				#TextWindow(materialFileName, materialData.toString(), 400, 400)
		
	#Close the project if close_after_opening was set as True
	if close_after_opening:
		project.getLoader().setChanged(False) #Avoid dialog at closing
		project.destroy()
			
print("Done!")