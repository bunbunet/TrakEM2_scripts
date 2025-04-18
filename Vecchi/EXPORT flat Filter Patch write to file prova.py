from ij import ImagePlus
from ini.trakem2 import Project
from ini.trakem2.display import Display,Patch
from ij.io import FileSaver
from java.awt import Color
from ini.trakem2.display import Displayable

#-----------------USER DEFINED OPTIONS--------------------------#

# LAYER RANGE
index_first_section = 1
index_last_section = 10

# SCALE 
# in % e.g 0.05=5% of Project pixel size
magnification = 0.05

# CHOOSE EXPORT COLOR: 
# For RGB: ImagePlus.COLOR_RGB or For Greyscale: ImagePlus.GRAY8
Export_Color=ImagePlus.COLOR_RGB

# FILTER FOR CODES IN IMAGE TITLE, 
#  multiple codes can be specified if separated by commas, e.g ["scan","WSsp","series_"]
visible_patches=["scan","WSsp","_series_"]
#visible_patches=["_series"]

# SET TRUE TO SEE THE DISPLAYABELS (Arealists, balls etc..)
Show_Displayabels=False

#--------------------------------------------------------------#

#Displayabels Hide/Unhide
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
layerset = project.getRootLayerSet()
front = Display.getFront()
layerset = front.getLayerSet()
layers = layerset.getLayers().subList(index_first_section-1,
index_last_section)
loader = layerset.getProject().getLoader()

roi = front.getRoi()
bounds = roi.getBounds() if roi else layerset.get2DBounds()
scale = magnification
backgroundColor = Color.black

# NOTE: EDIT THIS PATH
targetDir = "G:\\Prove"
# ImagePlus options: COLOR_256 o COLOR_RGB
for i, layer in layers:
  print layer
  # Export the image here, e.g.:
  tiles = layer.getDisplayables(Patch)
  ip = Patch.makeFlatImage(
           Export_Color,
           layer,
           bounds,
           scale,
           tiles,
           backgroundColor,
           True)  # use the min and max of each tile

  imp = ImagePlus("Flat montage", ip)
  FileSaver(imp).saveAsTiff(targetDir + str(i + 1) + ".png")