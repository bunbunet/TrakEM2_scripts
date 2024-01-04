from ini.trakem2.display import Display, AreaList
from ij.gui import ShapeRoi
from ij.plugin.frame import RoiManager

# Before running the script open ROI manager and select an AreaList

def getRoiManager():
  """ Obtain a valid instance of the ROI Manager.
  Notice that it could still be null if its window is closed."""
  if RoiManager.getInstance() is None:
    RoiManager()
  return RoiManager.getInstance()
 
def putAreas(arealist):
  """ Take all areas of an AreaList and put them in the ROI Manager."""
  for layer in arealist.getLayerRange():
    area = arealist.getAreaAt(layer)
    if area is not None and not area.isEmpty():
      roi = ShapeRoi(area)
      getRoiManager().addRoi(roi)
 
def run():
  front = Display.getFront()
  layers = front.getLayerSet().getLayers()
  arealists = front.getSelection().getSelected(AreaList)
  if arealists.isEmpty():
    IJ.log("No arealists selected!")
    return
  # Extract areas as ROIs for the first one:
  putAreas(arealists[0])
 
run()