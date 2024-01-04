from ini.trakem2.display import Display, Patch
from ini.trakem2 import Project
from ij.text import TextWindow

ProjName= Project.getProjects()

rows = []

for layer in Display.getFront().getLayerSet().getLayers():
					z = layer.getZ()
					rows.append(str(z))

csv = "\n".join(rows)
 
t = TextWindow(str(ProjName)+"zLevels", csv, 400, 400)