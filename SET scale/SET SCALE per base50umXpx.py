#Scale patches to fit the 40x512 resolution ( 0.7568361)
from ini.trakem2.display import Display, Patch
from java.awt.geom import AffineTransform

for layer in Display.getFront().getLayerSet().getLayers():
	patches = layer.getDisplayables(Patch)
	for patch in patches:
		if "scan" in patch.title:
				aff = AffineTransform()
				CurrentScale = patch.getAffineTransform().getScaleX()
				aff.scale(0.2113/CurrentScale, 0.2113/CurrentScale)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "20X512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.0303/CurrentScale2, 0.0303/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "40X512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.0151/CurrentScale2, 0.0151/CurrentScale2)
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
				aff.scale(0.0151/CurrentScale2, 0.0151/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()	
		elif "40X1024" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.0076/CurrentScale2, 0.0076/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()	
		elif "63X1024" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.2501/CurrentScale2, 0.2501/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "63X2048" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.2501/CurrentScale2, 0.2501/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "63X3072" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.2501/CurrentScale2, 0.2501/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "63X512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.5003/CurrentScale2, 0.5003/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "section" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.6998/CurrentScale2, 0.6998/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()
		elif "20Xim512" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.0303/CurrentScale2, 0.0303/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()		
		elif "20Xim1024" in patch.title:
				aff = AffineTransform()
				CurrentScale2 = patch.getAffineTransform().getScaleX()
				aff.scale(0.0151/CurrentScale2, 0.0151/CurrentScale2)
				patch.preTransform(aff, True)
				patch.updateBucket()					