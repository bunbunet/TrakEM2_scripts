from ini.trakem2.display import Display, Patch
from ini.trakem2 import Project
from ij.text import TextWindow

ProjName= Project.getProjects()

zList=[]

for layer in Display.getFront().getLayerSet().getLayers():
							print layer
							z = layer.getZ()
							zList.append(str(z))

csv = ",".join(zList)
 
t = TextWindow(str(ProjName)+"zList", csv, 400, 400)