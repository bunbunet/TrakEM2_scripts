from ini.trakem2.display import Display, Patch


Show_selection_only= True

# To have only a specific image type, first hide all images and than unhide the ones you want
stains=["section"]
#stains=["scan","WSsp"]
stains=["scan","WSsp"]

if Show_selection_only:
#First Hide All patches
	for layer in Display.getFront().getLayerSet().getLayers():
		patches = layer.getDisplayables(Patch)
		for patch in patches:
			patch.visible = False
#Unhide the filtered ones	
	for layer in Display.getFront().getLayerSet().getLayers():
					patches = layer.getDisplayables(Patch)
					for patch in patches:
						for visible in stains:
							if visible in patch.title:
								patch.visible = True	
else:
	for layer in Display.getFront().getLayerSet().getLayers():
					patches = layer.getDisplayables(Patch)
					for patch in patches:
						for stain in stains:
							if stain in patch.title:
								patch.visible = True