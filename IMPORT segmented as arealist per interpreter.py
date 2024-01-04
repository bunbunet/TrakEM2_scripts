from ini.trakem2 import Project
from ini.trakem2.utils import AreaUtils
from ini.trakem2.display import AreaList
from java.awt import Color
from ij import IJ

 
# Obtain an image stack
imp = IJ.getImage()
#imp = WindowManager.getImage("prova.tif")
 
# Obtain the opened TrakEM2 project
p = Project.getProjects()[0]
 
# Obtain the LayerSet
layerset = p.getRootLayerSet()
 
# Create a new AreaList, named "synapses"
ali = AreaList(p, "GFP", 0, 0)
 
# Add the AreaList to the datastructures:
layerset.add(ali)
p.getProjectTree().insertSegmentations([ali])
 
# Obtain the image stack
stack = imp.getImageStack()
 
# Iterate every slice of the stack
for i in range(1, imp.getNSlices() +1):
  ip = stack.getProcessor(i) # 1-based
  # Extract all areas (except background) into a map of value vs. java.awt.geom.Area
  m = AreaUtils.extractAreas(ip)
  # Report progress
  print i, ":", len(m)
  # Get the Layer instance at the corresponding index
  layer = layerset.getLayers().get(i-1) # 0-based
  # Add the first Area instance to the AreaList at the proper Layer
  ali.addArea(layer.getId(), m.values().iterator().next())
 
# Change the color of the AreaList
ali.setColor(Color.magenta)
 
# Ensure bounds are as constrained as possible
ali.calculateBoundingBox(None)
 
Display.repaint()