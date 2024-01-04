from ini.trakem2.display import Display, Ball
from java.awt import Color

display = Display.getFront()
layerset = display.getLayerSet()

ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)

for ballOb in ball_obs:
 	if "Retro" in ballOb.title:
		ballOb.color=Color.red
	elif "PreS" in ballOb.title:
		ballOb.color=Color.green
	elif "STARTER" in ballOb.title:
			ballOb.color=Color.yellow
	ballOb.repaint(True, None)
