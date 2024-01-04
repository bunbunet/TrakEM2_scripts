from ini.trakem2.display import Display, Ball
from ij.text import TextWindow
from ini.trakem2 import Project

#Ball names positions: 
#PreS_pz4_CX_ACAv_layer2/3_CTIP2-_
#  0   1   2  3     4        5

#Position to filter
#filterPos=1
#String filter
#filterString="pz4"

#filter by string
#fiterByString="PreS_pz4_CX"

#old string
old="Nbl-CTIP2+"
#new string
new="Nbl+CTIP2+"

ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)
#alternative selections are for getZDisplayables(Patch) getZDisplayables(AreaList)


for ball_ob in ball_obs:
	title = ball_ob.getTitle()
	g=title.split("_")
	if len(g)>6:
		if g[2]=="SVZ": 
		#and g[1]=="pz4" and g[2]=="AMY":
		#if fiterByString in title:
		#modify the string name according to the position of you want to change
			if g[5]==old:
				ball_ob.title=str(g[0]+"_"+g[1]+"_"+g[2]+"_"+g[3]+"_"+g[4]+"_"+new+"_"+g[6]+"_")
				print (title,ball_ob.title)
				
	ball_ob.repaint(True, None)				