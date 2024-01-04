from ini.trakem2.display import Display, Ball
from java.awt import Color

#set the value of the new radius in pixels
display = Display.getFront()
layerset = display.getLayerSet()

ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)

for ball_ob in ball_obs:
 	title = ball_ob.getTitle()
 	NewTitle= title + "_alessia"
 	ball_ob.title=NewTitle
			