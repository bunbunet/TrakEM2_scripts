# Export an ImageStack from a range of TrakEM2 layers
# User can control the scale, color and visibility of patches and displayables

from ini.trakem2.display import Displayable
from ini.trakem2.display import Display, Patch
from ij import ImagePlus, ImageStack

# SPECIFY THE LAYER RANGE
index_first_section = 1
index_last_section = 66

# SPECIFY THE MAGNIFICATION
magnification = 0.05

#CHOOSE EXPORT COLOR: ImagePlus.COLOR_RGB or ImagePlus.GRAY8
Export_Color=ImagePlus.COLOR_RGB

#FILTER FOR CODES IN IMAGE TITLE 
visible_patches=["scan","MAX"]

#SET TRUE TO SEE THE DISPLAYABELS (Arealists, balls etc..)
Show_Displayabels=False

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

front = Display.getFront()
layerset = front.getLayerSet()
layers = layerset.getLayers().subList(index_first_section-1,
index_last_section)
loader = layerset.getProject().getLoader()

# Can be null
roi = front.getRoi()

# The whole 2D area, or just that of the ROI
bounds = roi.getBounds() if roi else layerset.get2DBounds()

stack = ImageStack(int(bounds.width * magnification + 0.5),
                   int(bounds.height * magnification + 0.5))
print stack

#the getFlatImage function.
for layer in layers:
  imp = loader.getFlatImage(layer, bounds, magnification, -1,
Export_Color, Displayable, False)
  stack.addSlice(imp.getProcessor())

ImagePlus("stack", stack).show()
###################
