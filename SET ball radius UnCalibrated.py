from ini.trakem2.display import Display, Ball

#set the value of the new radius in pixels
display = Display.getFront()
layerset = display.getLayerSet()
new_radius = 100



for ballOb in layerset.getZDisplayables(Ball):
  	for i in range(ballOb.getCount()):
		aff = ballOb.getAffineTransform()
		scale = aff.getScaleX()
		ballOb.setRadius(i, new_radius/scale)
	ballOb.repaint(True, None)
	
Display.repaint()