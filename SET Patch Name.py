from ini.trakem2.display import Display, Patch
#This macro add a specific expression to patch names.
#the purpouse is to group patches with different names in a single easily searchable entity.
stain= "GFAP"

for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					if stain in patch.title:
						patch.title = patch.title + "_otherMk"
