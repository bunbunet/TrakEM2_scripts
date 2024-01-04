from ini.trakem2.display import Display, Patch
from ini.trakem2 import Project
from ij.text import TextWindow

#insert here the z-values from the zList Text files inside the [ ]
zList = [2.1,2.2,2.3,2.4,2.5,3.1,3.2,3.3,3.4,3.5,4.1,4.2,4.3,4.4,4.5,5.1,5.2,5.3,5.4,5.5,6.1,6.2,6.3,6.4,6.5,7.1,7.2,7.3,7.4,7.5,8.1,8.2,8.3,8.4,8.5,9.1,9.2,9.3,9.4,9.5,10.1,10.2,10.3,10.4,10.5,11.1,11.2,11.3,11.4,11.5,12.1,12.2,12.3,12.4,12.5,38.1]

project = Project.getProjects().get(0)
layerset = project.getRootLayerSet()

for i in zList:
  layerset.getLayer(i, 1, True)

# ... and update the LayerTree:
project.getLayerTree().updateList(layerset)
# ... and the display slider
Display.updateLayerScroller(layerset)