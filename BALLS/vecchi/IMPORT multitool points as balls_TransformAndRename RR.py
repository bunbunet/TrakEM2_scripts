#This code read X,Y coordinates of muti-point selections from Result Table and import them to TrakEM2 as Balls with spacific names.
#To run first add the multipoint to ROI manager, 
#RESET IMAGE CALIBRATION, than "measure" and check that a Rsult Tables opens, select the corresponding image in TrakEM2 and run the script
#The added points are automatically transformed and linked to the original image.
#You only need to specify the ball radius, the markers names and their colors. 

from ini.trakem2.display import Display, Ball, Profile
from ini.trakem2.utils import M, Utils
from ij.measure import ResultsTable
from ij import IJ
from java.awt import Color

#specify the ball radius
radius=10

#SPECIFY Marker's name. The Names are set for 3 cell types either positive or negative for a marker. Total of 6 markers
BaseNamePos="pz1_STR_ _ _DCX+_v2cl3rw1pz1"
BaseNameNeg="pz1_STR_ _ _DCX-_v2cl3rw1pz1"
CellType1="PreS_"
CellType2="Retro_"
CellType3="STARTER_"
#set the colors of the cell types
color1=Color.green
color2=Color.red
color3=Color.yellow

p=Display.getFront().getActive()

aff= p.getAffineTransform()

#import point coordinates and names from resultTable
rt = ResultsTable.getResultsTable()
xA = rt.getColumn(rt.getColumnIndex('X'))
yA = rt.getColumn(rt.getColumnIndex('Y'))
Label = rt.getColumn(rt.getColumnIndex('Counter'))

#Empty dictionaries to collect the coordinates for each counter type
X={}
Y={}

for key in Label:
	if key in Label:
		X[key]=[]
		Y[key]=[]
	for i in range(0,len(Label)):
		if Label[i]==key:
			X[key].append(xA[i])
			Y[key].append(yA[i])
			
for key in X:
	print key
	for a,b in zip(X[key],Y[key]):	
			print a,b
			
#rename the first 6 markers (non including 0) according to the code
try:
	X[str(CellType1)+BaseNamePos]=X.pop(1.0)
except KeyError:
	pass
try:	
	X[str(CellType1)+BaseNameNeg]=X.pop(2.0)
except KeyError:
	pass
try:
	X[str(CellType2)+BaseNamePos]=X.pop(3.0)
except KeyError:
	pass
try:
	X[str(CellType2)+BaseNameNeg]=X.pop(4.0)
except KeyError:
	pass
try:
	X[str(CellType3)+BaseNamePos]=X.pop(5.0)
except KeyError:
	pass
try:
	X[str(CellType3)+BaseNameNeg]=X.pop(6.0)
except KeyError:
	pass

#must do it also for Y to maintain X and Y matching
try:
	Y[str(CellType1)+BaseNamePos]=Y.pop(1.0)
except KeyError:
	pass
try:	
	Y[str(CellType1)+BaseNameNeg]=Y.pop(2.0)
except KeyError:
	pass
try:
	Y[str(CellType2)+BaseNamePos]=Y.pop(3.0)
except KeyError:
	pass
try:
	Y[str(CellType2)+BaseNameNeg]=Y.pop(4.0)
except KeyError:
	pass
try:
	Y[str(CellType3)+BaseNamePos]=Y.pop(5.0)
except KeyError:
	pass
try:
	Y[str(CellType3)+BaseNameNeg]=Y.pop(6.0)
except KeyError:
	pass

#Functions to create Balls
def createBall(name):
#Create a Ball object, that can contain numerous x,y,z,r balls
  layer = Display.getFrontLayer()
  ball = Ball(layer.project,name, 0, 0)
  layer.getParent().add(ball)
  layer.project.getProjectTree().insertSegmentations([ball])
  return ball
 
def addBall(ballob, x, y, radius, layer):
  ballob.addBall(x, y, radius, layer.id)
  ballob.repaint()
  
#Running the function for each Counter Type
for key in X:
	Ball_Name= str(key)
	#Ball_Name=patch_name + "_"+ str(key)
	ballob = createBall(Ball_Name)
	for i,j in zip(X[key],Y[key]):
		addBall(ballob, i,j, radius, Display.getFrontLayer())
	ballob.setAffineTransform(aff)
	




