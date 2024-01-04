#Scale patches to fit the 40x512 resolution ( 0.7568361)
from ini.trakem2.display import Display, Patch
from java.awt.geom import AffineTransform

for layer in Display.getFront().getLayerSet().getLayers():
	patches = layer.getDisplayables(Patch)
	for patch in patches:
		if "scan" in patch.title:
				print(patch.title)
				aff = AffineTransform()
				CurrentScale = patch.getAffineTransform().getScaleX()
				aff.scale(47.9481/CurrentScale, 47.9481/CurrentScale)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "20x512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(2.0040/CurrentScale2, 2.0040/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "40x512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(1/CurrentScale2, 1/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "NeLu" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.9752/CurrentScale2, 0.9752/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "20x1024" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(1.0004/CurrentScale2, 1.0004/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()	
		elif "40x1024" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.5/CurrentScale2, 0.5/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "NeLu" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.9752/CurrentScale2, 0.9752/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()		
		elif "63x1024" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.2501/CurrentScale2, 0.2501/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "63x2048" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.2501/CurrentScale2, 0.2501/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "63x3072" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.2501/CurrentScale2, 0.2501/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "63x512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.5003/CurrentScale2, 0.5003/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()		
							