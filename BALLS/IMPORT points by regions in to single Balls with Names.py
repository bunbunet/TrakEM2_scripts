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

#Specify the Ball Name
Ball_name="Ball"

#Specify the Ball Radius
radius=10

#Set True if you want to apply the transform of an existing patch
#in that case the patch sould be selected (getActive())
register_to_image=False
if register_to_image:
	p=Display.getFront().getActive()
	aff= p.getAffineTransform()

#Check that column names matches those listed in the Result Table
rt = ResultsTable.getResultsTable()
xA = rt.getColumn(rt.getColumnIndex('X'))
yA = rt.getColumn(rt.getColumnIndex('Y'))
zA = rt.getColumn(rt.getColumnIndex('Z'))
Label = rt.getColumn(rt.getColumnIndex('Name'))

#Use the slice as an index to retrive the Layer and create a list of the Layars sequence for the points
Layers= Display.getFront().getLayerSet().getLayers()
zSeries=[]
for item in zA:
	zSeries.append(Layers[int(item-1)])

#Empty dictionaries to collect the coordinates for each counter type
X={}
Y={}
Z={}

#Point Tools
#two parallel dictionaries are built in which the list of coordinates are divided by marker type
#this makes it easier to rename the files
#{Label[1]:[x1,x2,x3,x4..xn]; Label[2]:[x1,x2,x3,x4,5]

for key in Label:
	X[key]=[]
	Y[key]=[]
	Z[key]=[]
	for i in range(0,len(Label)):
		if Label[i]==key:
			X[key].append(xA[i])
			Y[key].append(yA[i])
			Z[key].append(zSeries[i])
			
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




