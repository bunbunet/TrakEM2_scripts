from ini.trakem2 import Project
from ini.trakem2.display import AreaList, Display
from org.scijava.vecmath import Color3f
from customnode import WavefrontExporter, CustomTriangleMesh
from java.io import StringWriter
from ij.text import TextWindow
import csv
import os

#project = Project.openFSProject(source_dir + path, False)
folder = "C:\\Users\\Federico Luzzati\\Desktop\\Rabies XML 11 2020 bkp" # MUST have ending slash
AreaSelection=["An_LV"]
filenames = os.listdir(folder)

displays = Display.getDisplays()
projects = {}
for display in displays:
	projects[display.project] = display

projects=Project.getProjects()
for project in projects:
	arealists = project.getRootLayerSet().getZDisplayables(AreaList) 
	for arealist in arealists:
		print(project,arealist)
				


	