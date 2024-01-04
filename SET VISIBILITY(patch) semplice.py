from ini.trakem2.display import Display, Patch

Areas=["scan","GFP","RFP","CTIP2","DCX","DAPI"]
for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					for area in Areas:
						if area in patch.title:
							patch.visible = False
						
						
						