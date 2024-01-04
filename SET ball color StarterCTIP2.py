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
		elif "STARTER" in ballOb.title:
			ballOb.color=Color.yellow
			if "CTIP2+" in ballOb.title:
					ballOb.color=Color.magenta
			#if "DCX+" in ballOb.title: NON VA NON SO PERCHE'..
					#ballOb.color=Color.cyan		
	ballOb.repaint(True, None)