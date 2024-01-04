from ij import ImagePlus
from ini.trakem2 import Project
from ini.trakem2.display import Patch
from ij.io import FileSaver
from java.awt import Color

project = Project.getProjects()[0]
layerset = project.getRootLayerSet()

roi = layerset.get2DBounds()
scale = 1.0
backgroundColor = Color.black

# NOTE: EDIT THIS PATH
targetDir = "G:\\Collaborations\\Delfino\\Prova 1\\export"
# ImagePlus options: COLOR_256 o COLOR_RGB
for i, layer in enumerate(layerset.getLayers()):
  print layer
  # Export the image here, e.g.:
  tiles = layer.getDisplayables(Patch)
  ip = Patch.makeFlatImage(
           ImagePlus.COLOR_RGB,
           layer,
           roi,
           scale,
           tiles,
           backgroundColor,
           True)  # use the min and max of each tile

  imp = ImagePlus("Flat montage", ip)
  FileSaver(imp).saveAsTiff(targetDir + str(i + 1) + ".tif")