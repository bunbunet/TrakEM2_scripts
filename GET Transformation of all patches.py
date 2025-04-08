from ini.trakem2.display import Display, Patch
from ini.trakem2 import Project
from ij.text import TextWindow

ProjName= Project.getProjects()
filters= ["Sp8"]
rows = []

for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					title = patch.getTitle()
					for filter in filters:
						if filter in title:
							p=patch.getAffineTransform()
							rows.append(str(title) + "," + str(layer)+ "," +str (p))

csv = "\n".join(rows)
 
t = TextWindow(str(ProjName)+"Transform", csv, 400, 400)