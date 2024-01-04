from ini.trakem2.display import Display, Ball
from java.awt import Color

#set the value of the new radius in pixels
display = Display.getFront()
layerset = display.getLayerSet()

for ballOb in layerset.getZDisplayables(Ball):
  	for i in range(ballOb.getCount()):
		if "Retro" in ballOb.title:
			ballOb.color=Color.red
		elif "PreS" in ballOb.title:
			ballOb.color=Color.green
		if "DCX-" and not "CTIP2-" and "STARTER" in ballOb.title:
			ballOb.color=Color.yellow
		elif "STARTER" in ballOb.title and "DCX+" in ballOb.title:
					ballOb.color=Color.cyan
		elif "STARTER" in ballOb.title and "CTIP2+" in ballOb.title: 
					ballOb.color=Color.magenta		
	ballOb.repaint(True, None)