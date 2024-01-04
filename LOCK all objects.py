from ini.trakem2.display import Display, Patch
from java.awt import Color

Lock=False

for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables()
				for patch in patches:
					#if "" in patch.title:
					 	patch.setLocked(Lock)

Zdisp = Display.getFront().getLayerSet().getZDisplayables()
for z in Zdisp:
	z.setLocked(Lock)
						
Display.repaint()