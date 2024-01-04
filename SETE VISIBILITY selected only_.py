from ini.trakem2.display import Display, Patch

#FILTER FOR CODES IN IMAGE TITLE 
visible_patches=["GFP"]
visible_patches=["Third","GFP"]

#Patch Hide/Unhide
#First Hide All patches
for layer in Display.getFront().getLayerSet().getLayers():
	patches = layer.getDisplayables(Patch)
	for patch in patches:
		patch.visible = False
#Unhide the filtered ones	
for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					for visible in visible_patches:
						if visible in patch.title:
							patch.visible = True