#This script add a ball object to the open TrakEM2 project form point coordinates
#listed in the Result Table where x,y and layers values are indicated in columns
#names X,Y and Slice

from ini.trakem2.display import Display, Ball, Profile
from ij.measure import ResultsTable
from ij import IJ


#Specify the Ball Name
Ball_name="Ball"

#Specify the Ball Radius
radius=10

#Set True if you want to apply the transform of an existing patch
#in that case the patch sould be selected (getActive())
register_to_image=True
if register_to_image:
	p=Display.getFront().getActive()
	aff= p.getAffineTransform()

rt = ResultsTable.getResultsTable()
xA = rt.getColumn(rt.getColumnIndex('X'))
yA = rt.getColumn(rt.getColumnIndex('Y'))
zA = rt.getColumn(rt.getColumnIndex('Slice'))
#Label = rt.getColumn(rt.getColumnIndex('Counter'))

Layers= Display.getFront().getLayerSet().getLayers()

#Use the slice as an index to retrive the Layer and create a list of the Layars sequence for the points
zSeries=[]
for item in zA:
	zSeries.append(Layers[int(item-1)])

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

#Create balls as part of the Ball Object
ballob=createBall(Ball_name)
for x,y,layer in zip(xA,yA,zSeries):
	addBall(ballob,x,y,radius,layer)
if register_to_image:
	ballob.setAffineTransform(aff)
ballob.repaint()
