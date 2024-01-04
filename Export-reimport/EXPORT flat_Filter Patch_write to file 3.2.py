#This script export flat images from the reconstruction with a number of user difined options,
#such as patch and Displayables visibility, scale, layer range and file format
#By default it export image sequence with _s based code and .png format for QuickNII import
#To save as _z based and .tif format set "QuickNII as False
#To export an x,y crop of the reconstruction draw a ROI in the display.
#User defined options are listed in the "USER DEFINED OPTIONS" section of the macro.

#---IMPORT LIBRARIES----#
from ij import ImagePlus
from ini.trakem2 import Project
from ini.trakem2.display import Patch,Display,Displayable
from ij.io import FileSaver
from java.awt import Color

#-----------------USER DEFINED OPTIONS--------------------------#
# SPECIFY THE DIRECTORY TO SAVE FILES
Directory="F:\\p60_mice_whole_brain\\FmrWT2\\Pi_10perc\\"
#Specify additional tag in file name
tag="_Pi_10perc"

# LAYER RANGE
index_first_section = 1
index_last_section = 253

# SCALE 
# in % e.g 0.05=5% of Project pixel size
scale = 0.10

# CHOOSE EXPORT COLOR: 
# For RGB: ImagePlus.COLOR_RGB or For Greyscale: ImagePlus.GRAY8
Export_Color=ImagePlus.COLOR_RGB

# FILTER FOR CODES IN IMAGE TITLE, 
#  multiple codes can be specified if separated by commas, e.g ["scan","WSsp","series_"]; set [] to leave visibility as it is
visible_patches=[]
#visible_patches=["_series"]

# LEAVE THE DISPLAYABELS (Arealists, balls etc..) AS THEY ARE: SET True
LeaveDisp=True

# SEE ALL THE DISPLAYABELS: SET TRUE, SET FALSE to hide them all
Show_Displayabels=True

# EXPORT FOR QuckNII: SET True
QuikNII=False
pad="03"

#--------------------------------------------------------------#

#Displayabels Hide/Unhide
if not LeaveDisp:
	Zdisp=Display.getFront().getLayerSet().getZDisplayables()
	for Z in Zdisp:
		Z.visible = Show_Displayabels

#Patch Hide/Unhide
if len(visible_patches)>0:
#First Hide All patches
	for layer in Display.getFront().getLayerSet().getLayers():
		patches = layer.getDisplayables(Patch)
		for patch in patches:
			patch.visible = False
#Unhide the filtered ones	
	for layer in Display.getFront().getLayerSet().getLayers():
					patches = layer.getDisplayables(Patch)
					for patch in patches:
						for visible in visible_patches:
							if visible in patch.title:
								patch.visible = True


project = Project.getProjects()[0]
front = Display.getFront()
layerset = front.getLayerSet()
layers = layerset.getLayers().subList(index_first_section-1,
index_last_section)
loader = layerset.getProject().getLoader()

roi = front.getRoi()
bounds = roi.getBounds() if roi else layerset.get2DBounds()
backgroundColor = Color.black

#Format the speciman name from the project name
Specimen= str(project).split(".xml")[0]

targetDir = Directory+Specimen+tag
# ImagePlus options: COLOR_256 o COLOR_RGB
for i, layer in enumerate(layers):
  print layer
#makeFlatImage starts from the original images
  ip = loader.getFlatImage(layer, bounds, scale, -1,Export_Color, Displayable, False)
  if QuikNII:
  	FileSaver(ip).saveAsPng(targetDir + "_s"+str(format(i + index_first_section, pad)) + ".png")
  else:
  	FileSaver(ip).saveAsTiff(targetDir + "_z"+str(i + index_first_section -1) + "_.tif")

