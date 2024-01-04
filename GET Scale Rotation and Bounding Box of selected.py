from ini.trakem2 import *
from ini.trakem2.display import Display, Patch
from java.awt.geom import AffineTransform
import math

p = Display.getFront().getActive()
Type=p.getType()
Title=p.getTitle()
aff = p.getAffineTransform()
rot = math.atan2(aff.getShearY(), aff.getScaleY())
scal = aff.getScaleX()
tx = p.getBoundingBox()
print("Image Name: "+ Title)
print("Image Type: "+ str(Type))
print("scale: "+ str(scal))
print("rotation: "+str(rot*57.2958))
print("Bounding box: "+str(tx))