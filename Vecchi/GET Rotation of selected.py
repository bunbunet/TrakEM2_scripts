from ini.trakem2 import *
from ini.trakem2.display import Display, Patch
from java.awt.geom import AffineTransform
import math
p = Display.getFront().getActive()
aff = p.getAffineTransform()
rot = math.atan2(aff.getShearY(), aff.getScaleY()); 
conv=180/3.14
print("rotation in degrees: ",rot*57.2958)

# math.atan2 return the arc tangent o a x/y coordinates in radians
# https://www.w3schools.com/python/ref_math_atan2.asp