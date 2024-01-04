from ini.trakem2.display import Display, Patch
from java.awt import Color

stain= "GFP"
mode=1

for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if stain in patch.title:
						# Set the transparency (alpha value)
						patch.alpha = 1
						# Set 1 for ADD, 0 for Normal
						patch.setCompositeMode(mode)
						
Display.repaint()