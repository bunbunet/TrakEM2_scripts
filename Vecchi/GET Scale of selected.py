from ini.trakem2 import *
from ini.trakem2.display import Display, Patch
from java.awt.geom import AffineTransform

p = Display.getFront().getActive()
aff = p.getAffineTransform()
scal = aff.getScaleX()
print(scal)

