# Export an ImageStack from a range of TrakEM2 layers

from ini.trakem2.display import Display, Displayable
from ini.trakem2 import Project
from ij import ImagePlus, ImageStack

# SPECIFY THE LAYER RANGE
index_first_section = 13
index_last_section = 15

# SPECIFY THE MAGNIFICATION
magnification = 0.05

#CHOOSE EXPORT COLOR: ImagePlus.COLOR_RGB or ImagePlus.GRAY8
Export_Color=ImagePlus.COLOR_RGB

#FILTER FOR SPECIFIC IMAGE TYPES

front = Display.getFront()
layerset = front.getLayerSet()
layers = layerset.getLayers().subList(index_first_section-1,index_last_section)
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
  imp = loader.getFlatImage(layer, bounds, magnification, -1, Export_Color, Displayable, False)
  stack.addSlice(imp.getProcessor())

ImagePlus("stack", stack).show()
###################
