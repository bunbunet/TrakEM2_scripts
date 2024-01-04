from ini.trakem2.display import Display, Ball

calibrated_radius = 40  # in microns, nm, whatever
 
display = Display.getFront()
layerset = display.getLayerSet()
cal = layerset.getCalibration()
# bring radius to pixels
new_radius = calibrated_radius / cal.pixelWidth
 
for ballOb in layerset.getZDisplayables(Ball):
  for i in range(ballOb.getCount()):
  	aff = ballOb.getAffineTransform()
	scal = aff.getScaleX()
	ballOb.setRadius(i, new_radius/scal)
  ballOb.repaint(True, None)