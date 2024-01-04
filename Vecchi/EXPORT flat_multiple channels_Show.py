#This script export flat images from multichannel reconstructions under a ROI (if roi is not present the entire canvas is exported)
#The user must specify the Directory to save export, the name of the export, the tag identifying the channels and the layer index, 
#http://imagej.1557.x6.nabble.com/TrakEM-question-td5020256.html

#---IMPORT LIBRARIES----#
from ij import ImagePlus, ImageStack
from ij.io import FileSaver
from ij.plugin.frame import RoiManager
from ij import IJ
from ini.trakem2 import Project
from ini.trakem2.display import Patch,Display,Displayable
from java.awt import Color


#-----------------USER DEFINED OPTIONS--------------------------#
# SPECIFY THE DIRECTORY TO SAVE FILES
Directory="G:\\Progetto QA\\RR PSD Gephryn\\Export\\prove\\"
#Specify additional tag in file name
Export_Name="Nbl 1 e 2"

#Specify the channels to export as a python list
Markers=["DCX","GFP","Ki67","RFP"]
#add a potential additional tag specifying the image class (i.e. 40x, 20x etc..)
Vis_tag=".tif.tif"

# LAYER RANGE
index_first_section = 270
index_last_section = 272

# SCALE 
# in % e.g 0.05=5% of Project pixel size
scale = 1

# CHOOSE EXPORT COLOR: 
# For RGB: ImagePlus.COLOR_RGB or For Greyscale: ImagePlus.GRAY8
Export_Color=ImagePlus.GRAY8

# LEAVE THE DISPLAYABELS (Arealists, balls etc..) AS THEY ARE: SET True
LeaveDisp=False
# SEE ALL THE DISPLAYABELS: SET TRUE, SET FALSE to hide them all
Show_Displayabels=False


#-------------------------------------

rm = RoiManager.getInstance()
if not rm:
  rm = RoiManager()
 
#Displayabels Hide/Unhide
if not LeaveDisp:
	Zdisp=Display.getFront().getLayerSet().getZDisplayables()
	for Z in Zdisp:
		Z.visible = Show_Displayabels

Sing_ch_images=[]
project = Project.getProjects()[0]
front = Display.getFront()
layerset = front.getLayerSet()
layers = layerset.getLayers().subList(index_first_section-1,
index_last_section)
loader = layerset.getProject().getLoader()
roi = front.getRoi()
roi.setName(Export_Name+"_z"+str(index_first_section)+"_z"+str(index_last_section))
rm.addRoi(roi)

bounds = roi.getBounds() if roi else layerset.get2DBounds()
backgroundColor = Color.black


for mark in Markers:
#Patch Hide/Unhide
#First Hide All patches
	for layer in Display.getFront().getLayerSet().getLayers():
		for patch in layer.getDisplayables(Patch):
			patch.visible = False
#Unhide the selected marker
	for layer in Display.getFront().getLayerSet().getLayers():
		patches = layer.getDisplayables(Patch)
		for patch in patches:
			if mark in patch.title and Vis_tag in patch.title:
				patch.visible = True

	
	#Format the speciman name from the project name
	Specimen= str(project).split(".xml")[0]
	
	targetDir = Directory+Specimen+Export_Name
	
	stack = ImageStack(int(bounds.width * scale + 0.5),
	                   int(bounds.height * scale + 0.5))
	print mark
	print stack
	
	for layer in layers:
	  imp = loader.getFlatImage(layer, bounds, scale, -1,
	Export_Color, Displayable, False)
	  stack.addSlice(imp.getProcessor())
	
	ImagePlus(mark+"-"+Export_Name+"_z"+str(index_first_section)+"_z"+str(index_last_section), stack).show()
	current_image = IJ.getImage()
	FileSaver(current_image).saveAsTiff(Directory +mark+"-"+ Export_Name+"_z"+str(index_first_section)+"_z"+str(index_last_section) + ".tif")
	Sing_ch_images.append(mark+"-"+ Export_Name+"_z"+str(index_first_section)+"_z"+str(index_last_section))

Parameters=""
for i in range(len(Markers)):
	string="c"+str(i+1)+"=["+Sing_ch_images[i]+"] "
	Parameters +=string

IJ.run("Merge Channels...",""+Parameters+"  create");

current_image = IJ.getImage()
FileSaver(current_image).saveAsTiff(Directory + Export_Name+"_z"+str(index_first_section)+"_z"+str(index_last_section) + "_composite.tif")
	

