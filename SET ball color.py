from ini.trakem2.display import Display, Ball
from java.awt import Color

#set the value of the new radius in pixels
display = Display.getFront()
layerset = display.getLayerSet()

for ballOb in layerset.getZDisplayables(Ball):
  	for i in range(ballOb.getCount()):
		if "com" in ballOb.title:
			ballOb.color=Color.yellow
	ballOb.repaint(True, None)