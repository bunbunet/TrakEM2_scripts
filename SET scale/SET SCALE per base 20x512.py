#Scale patches to fit the 20x512 resolution (1.5166)
from ini.trakem2.display import Display, Patch
from java.awt.geom import AffineTransform

for layer in Display.getFront().getLayerSet().getLayers():
	patches = layer.getDisplayables(Patch)
	for patch in patches:
		if "scan" in patch.title:
			aff = AffineTransform()
			CurrentScale = patch.getAffineTransform().getScaleX()
			aff.scale(23.9266/CurrentScale, 23.9266/CurrentScale)
			patch.preTransform(aff, True)
			patch.updateBucket()
		if "40x512" in patch.title:
			aff = AffineTransform()
			CurrentScale = patch.getAffineTransform().getScaleX()
			aff.scale(0.4990/CurrentScale, 0.4990/CurrentScale)
			patch.preTransform(aff, True)
			patch.updateBucket()
		if "NeLu" in patch.title:
			aff = AffineTransform()
			CurrentScale = patch.getAffineTransform().getScaleX()
			aff.scale(0.4866/CurrentScale, 0.4866/CurrentScale)
			patch.preTransform(aff, True)
			patch.updateBucket()
		if "20x256" in patch.title:
			aff = AffineTransform()
			CurrentScale = patch.getAffineTransform().getScaleX()
			aff.scale(1.9961/CurrentScale, 1.9961/CurrentScale)
			patch.preTransform(aff, True)
			patch.updateBucket()
		
							