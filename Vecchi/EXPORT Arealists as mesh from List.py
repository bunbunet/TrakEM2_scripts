from ini.trakem2.display import AreaList, Display
from org.scijava.vecmath import Color3f
from customnode import WavefrontExporter, CustomTriangleMesh
from java.io import StringWriter
from ij.text import TextWindow

AreaSelection=["An_"]
specimen="RR11"
# Create the triangle mesh with resample of 1 (no resampling)
# CAUTION: may take a long time. Try first with a resampling of at least 10.
resample = 50
# Get the selected AreaList
arealists = Display.getFront().getLayerSet().getZDisplayables(AreaList) 
for arealist in arealists:
	for sel in AreaSelection:
		if sel in arealist.title:  

			triangles = arealist.generateTriangles(1, resample)
 
# Prepare a 3D Viewer object to provide interpretation
			color = Color3f(1.0, 1.0, 0.0)
			transparency = 0.0
			mesh = CustomTriangleMesh(triangles, color, transparency)
 
# Write the mesh as Wavefront
			name = specimen +"_"+ arealist.title + " " + str(arealist.id)
			m = {name : mesh}
			meshData = StringWriter()
			materialData = StringWriter()
			materialFileName = name + ".mtl"
			WavefrontExporter.save(m, materialFileName, meshData, materialData)
 
# Show the text of the files in a window
# then you save it with "File - Save"
			TextWindow(name+".obj", meshData.toString(), 400, 400)
		#TextWindow(materialFileName, materialData.toString(), 400, 400)