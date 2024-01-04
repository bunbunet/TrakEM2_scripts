#Scale patches to fit the 40x512 resolution ( 0.7568361)
from ini.trakem2.display import Display, Patch
from java.awt.geom import AffineTransform

for layer in Display.getFront().getLayerSet().getLayers():
	patches = layer.getDisplayables(Patch)
	for patch in patches:
		if "section" in patch.title:
				aff = AffineTransform()
				CurrentScale = patch.getAffineTransform().getScaleX()
				aff.scale(34/CurrentScale, 34/CurrentScale)
				patch.preTransform(aff, True)
				patch.updateBucket()	
		if "scan" in patch.title:
				aff = AffineTransform()
				CurrentScale = patch.getAffineTransform().getScaleX()
				aff.scale(10.5646/CurrentScale, 10.5646/CurrentScale)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "20X512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(1.5166/CurrentScale2, 1.5166/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "40X512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.7568/CurrentScale2, 0.7568/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "NeLu" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.0148/CurrentScale2, 0.0148/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "20X1024" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.757/CurrentScale2, 0.757/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()	
		elif "40X1024" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.3788/CurrentScale2, 0.3788/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()	
		elif "63xxxx" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.12/CurrentScale2, 0.12/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "63Xxxxx" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.2501/CurrentScale2, 0.2501/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "63Xxxxxx" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.2501/CurrentScale2, 0.2501/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "63Xxxxxx" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.5003/CurrentScale2, 0.5003/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "20Xim512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(1.5166/CurrentScale2, 1.5166/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()		
		elif "20Xim1024" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.757/CurrentScale2, 0.757/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()					