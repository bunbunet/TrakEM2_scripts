from ini.trakem2.display import Display, Patch
from java.awt import Color

for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if "series" in patch.title:
					 	patch.setLocked(True)
						
Display.repaint()