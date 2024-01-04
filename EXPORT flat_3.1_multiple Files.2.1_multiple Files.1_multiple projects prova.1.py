#This script export flat images from the reconstruction with a number of user difined options,
#such as patch and Displayables visibility, scale, layer range and file format
#By default it export image sequence with _s based code and .png format for QuickNII import
#To save as _z based and .tif format set "QuickNII as False
#To export an x,y crop of the reconstruction draw a ROI in the display.
#User defined options are listed in the "USER DEFINED OPTIONS" section of the macro.
#All imageis

#---IMPORT LIBRARIES----#
from ij import ImagePlus
from ini.trakem2 import Project
from ini.trakem2.display import Patch,Display,Displayable
from ij.io import FileSaver
from java.awt import Color

#-----------------USER DEFINED OPTIONS--------------------------#
# SPECIFY THE DIRECTORY TO SAVE FILES
Directory="C:\\Users\\feder\\Documents\\LAB\prove\\"
#Specify additional tag in file name
tag="_quickNII"

# LAYER RANGE
#set False to export all the images, empty layers will not be saved (but analyzed)
manual_set_layers =False
index_first_section = 1
index_last_section = 1

# SCALE 
# in % e.g 0.05=5% of Project pixel size
scale = 0.1

# CHOOSE EXPORT COLOR: 
# For RGB: ImagePlus.COLOR_RGB or For Greyscale: ImagePlus.GRAY8
Export_Color=ImagePlus.COLOR_RGB

# FILTER FOR CODES IN IMAGE TITLE, 
#  multiple codes can be specified if separated by commas, e.g ["scan","WSsp","series_"]; set [] to leave visibility as it is
visible_patches=["DCX"]
#visible_patches=["_series"]

# LEAVE THE DISPLAYABELS (Arealists, balls etc..) AS THEY ARE: SET True
LeaveDisp=True

# SEE ALL THE DISPLAYABELS: SET TRUE, SET FALSE to hide them all
Show_Displayabels=True

# EXPORT FOR QuckNII: SET True
QuikNII=False
pad="03"

#--------------------------------------------------------------#

projects=Project.getProjects()
for project in projects:
	specimen= str(project).split(".xml")[0]
	print("processing: " + specimen)
	#Displayabels Hide/Unhide
	if not LeaveDisp:
		Zdisp=project.getRootLayerSet().getZDisplayables()
		for Z in Zdisp:
			Z.visible = Show_Displayabels

		#Patch Hide/Unhide
	if len(visible_patches)>0:
	#First Hide All patches
		for layer in project.getRootLayerSet().getLayers():
			patches = layer.getDisplayables(Patch)
			for patch in patches:
				patch.visible = False
	#Unhide the filtered ones	
		for layer in project.getRootLayerSet().getLayers():
						patches = layer.getDisplayables(Patch)
						for patch in patches:
							for visible in visible_patches:
								if visible in patch.title:
									patch.visible = True
	
	layerset = project.getRootLayerSet()
	if manual_set_layers:
		layers = layerset.getLayers().subList(index_first_section-1,
		index_last_section)
	else: 
		layers = layerset.getLayers()
	loader = layerset.getProject().getLoader()
	
	bounds = layerset.get2DBounds()
	backgroundColor = Color.black

	targetDir = Directory+specimen+tag
	# ImagePlus options: COLOR_256 o COLOR_RGB
	for i, layer in enumerate(layers):
	  print layer
	#makeFlatImage starts from the original images
	  ip = loader.getFlatImage(layer, bounds, scale, -1,Export_Color, Displayable, False)
	  stat=ip.getStatistics()
	#skip empty images
	  if stat.mean>0:
		  if QuikNII:
		  	FileSaver(ip).saveAsPng(targetDir + "_s"+str(format(i + index_first_section, pad)) + ".png")
		  else:
		  	FileSaver(ip).saveAsTiff(targetDir + "_z"+str(format(i + index_first_section, pad)) + ".tif")

