from ini.trakem2 import Project
from ini.trakem2.display import AreaList, Display
from org.scijava.vecmath import Color3f
from customnode import WavefrontExporter, CustomTriangleMesh
from java.io import StringWriter
from ij.text import TextWindow
import csv
import os


folder = "C:\\Users\\Federico Luzzati\\Desktop\\Rabies XML 11 2020 bkp\\" # MUST have ending slash
Output_DIR="C:\\Users\\Federico Luzzati\\Desktop\\obj\\" # MUST have ending slash
AreaSelection=["An_"]
resample = 50

filenames = os.listdir(folder)
for name in filenames:
	if ".xml" in name:
		project = Project.openFSProject(folder + name, False)
		specimen= str(name).split(".xml")[0]
		print(specimen
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