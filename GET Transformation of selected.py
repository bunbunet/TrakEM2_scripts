from ini.trakem2.display import Display

p=Display.getFront().getActive()
g=p.getAffineTransform()
print(g)