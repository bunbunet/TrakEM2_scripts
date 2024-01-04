from ij import ImagePlus
from ini.trakem2 import Project
from ini.trakem2.display import Patch,Display
from ij.io import FileSaver
from java.awt import Color

index_first_section = 1
index_last_section = 10
magnification = 0.05
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
for i, layer in enumerate(layerset.getLayers()):
  print layer
  # Export the image here, e.g.:
  tiles = layer.getDisplayables(Patch)
  ip = Patch.makeFlatImage(
           ImagePlus.COLOR_RGB,
           layer,
           bounds,
           scale,
           tiles,
           backgroundColor,
           True)  # use the min and max of each tile

  imp = ImagePlus("Flat montage", ip)
  FileSaver(imp).saveAsTiff(targetDir + str(i + 1) + ".tif")