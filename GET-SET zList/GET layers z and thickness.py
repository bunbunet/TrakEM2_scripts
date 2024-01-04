from ini.trakem2.display import Display, Patch
from ini.trakem2 import Project
from ij.text import TextWindow

layerset = Display.getFront().getLayerSet()
#
for layer in layerset.getLayers():
  print layer.getZ()
  print layer.getThickness()