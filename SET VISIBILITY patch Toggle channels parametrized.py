from java.awt.event import KeyEvent, KeyAdapter
from ini.trakem2.display import Display, Patch
#This script toggle the visibility of patches based on their names. 
#specify the part of the patch name to search
shortCut1="GFP"
shortCut2="RFP"
shortCut3="DCX"
shortCut4="Dapi"
shortCut5="scan"
shortCut6="otherMk"
shortCut7="otherMk"
shortCut8="otherMk"
shortCut9="otherMk"
shortCut0="otherMk"


class MyKeyListener(KeyAdapter):
	def keyPressed(self, event):
		keyCode = event.getKeyCode()
		if KeyEvent.VK_1 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut1 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True
							
		elif KeyEvent.VK_2 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut2 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True
	
		elif KeyEvent.VK_3 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut3 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True
							
		elif KeyEvent.VK_4 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut4 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True
							
		elif KeyEvent.VK_5 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut5 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True

		elif KeyEvent.VK_6 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut6 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True
							
							
		elif KeyEvent.VK_7 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut7 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True
							
		elif KeyEvent.VK_8 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut8 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True
							
		elif KeyEvent.VK_9 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut9 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True
							
		elif KeyEvent.VK_0 == keyCode:
			for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if shortCut0 in patch.title:
						if patch.visible == True:
							patch.visible = False
						else:
							patch.visible = True
							
Display.getFront().getCanvas().addKeyListener(MyKeyListener())
