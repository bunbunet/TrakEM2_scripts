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

#SPECIFY Marker's name. 
Marker1="1"
Marker2="2"
Marker3="3"
Marker4="4"
Marker5="5"
Marker6="6"
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

#in multitool the counter variable assing the marker type and can thus be repeted
#two parallel dictionaries are built in which the list of coordinates are divided by marker type
#this makes it easier to rename the files
#{Label[1]:[x1,x2,x3,x4..xn]; Label[2]:[x1,x2,x3,x4,5]
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
	X[Marker1]=X.pop(1.0)
except KeyError:
	pass
try:	
	X[Marker2]=X.pop(2.0)
except KeyError:
	pass
try:
	X[Marker3]=X.pop(3.0)
except KeyError:
	pass
try:
	X[Marker4]=X.pop(4.0)
except KeyError:
	pass
try:
	X[Marker5]=X.pop(5.0)
except KeyError:
	pass
try:
	X[Marker6]=X.pop(6.0)
except KeyError:
	pass

#must do it also for Y to maintain X and Y matching
try:
	Y[Marker1]=Y.pop(1.0)
except KeyError:
	pass
try:	
	Y[Marker2]=Y.pop(2.0)
except KeyError:
	pass
try:
	Y[Marker3]=Y.pop(3.0)
except KeyError:
	pass
try:
	Y[Marker4]=Y.pop(4.0)
except KeyError:
	pass
try:
	Y[Marker5]=Y.pop(5.0)
except KeyError:
	pass
try:
	Y[Marker6]=Y.pop(6.0)
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

ballob.repaint()	




