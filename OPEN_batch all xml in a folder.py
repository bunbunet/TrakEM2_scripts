from ini.trakem2 import Project
import os

folder = "C:/Users/feder/Documents/LAB\ProgettoQA/Dynamic/Time_Course_TrakEM2/all xml/" # MUST have ending slash

filenames = os.listdir(folder)

for name in filenames:
	if ".xml" in name:
		#open project without display
		project = Project.openFSProject(folder + name, False)