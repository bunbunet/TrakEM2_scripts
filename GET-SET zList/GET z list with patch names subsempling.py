from ini.trakem2.display import Display, Patch
from ini.trakem2 import Project
from ij.text import TextWindow

ProjName= Project.getProjects()

# define patch name code to select only the layers 
# that contains patches with that code 
search="_scan"
rows = []

for layer in Display.getFront().getLayerSet().getLayers():
				patches = layer.getDisplayables(Patch)
				for patch in patches:
					title = patch.getTitle()
					p=patch.getAffineTransform()
					if search in patch.title:
							z = layer.getZ()
							rows.append(str(title)+","+str(z))

csv = "\n".join(rows)
 
t = TextWindow(str(ProjName)+"Transform", csv, 400, 400)