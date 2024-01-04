from ini.trakem2.display import Display, Ball
from ij.text import TextWindow
from ini.trakem2 import Project

ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)

for ball_ob in ball_obs:
	title = ball_ob.getTitle()
	if title=="1":
		ball_ob.title="cK_no"
	elif title==2:
		ball_ob.title="cKcKD_no"
	elif title==3:
		ball_ob.title="cKD_no"
	elif title==4:
		ball_ob.title="cK_RFP"
	elif title==5:
		ball_ob.title="cKcKD_RFP"
	elif title==6:
		ball_ob.title="cKD_RFP"
	elif title==7:
		ball_ob.title="cK_Mem"
	elif title==8:
		ball_ob.title="cKcKD_Mem"
	elif title==9:
		ball_ob.title="cKD_Mem"
	elif title==10:
		ball_ob.title="cK_Cyt"
	elif title==11:
		ball_ob.title="cKcKD_Cyt"
	elif title==12:
		ball_ob.title="cKD_Cyt"	
	ball_ob.repaint(True, None)		