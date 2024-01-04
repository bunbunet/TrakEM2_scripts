#This script add a ball object to the open TrakEM2 project form point coordinates
#listed in the Result Table where x,y and layers values are indicated in columns
#names X,Y and Slice

from ini.trakem2.display import Display, Ball, Profile
from ij.measure import ResultsTable
from ij import IJ

#Set True if you want to apply the transform of an existing patch (must be selected)
register_to_image=False
#Set True if you want to add balls to a single Ball Objects
#Set False if you want each point to have its nmed ball abjects
single_ball=False
#Specify the Ball Name (if single_ball=True)
Ball_name="Ball"
#Specify the Ball Radius
radius=10
#Set False to import balls with existing names
Do_not_reimport=True

if Do_not_reimport:
	ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)
else:
	ball_obs=[]


if register_to_image:
	p=Display.getFront().getActive()
	aff= p.getAffineTransform()

#Check that column names matches those listed in the Result Table
rt = ResultsTable.getResultsTable()
xA = rt.getColumn(rt.getColumnIndex('X'))
yA = rt.getColumn(rt.getColumnIndex('Y'))
zA = rt.getColumn(rt.getColumnIndex('Z'))
Label = rt.getColumnAsVariables('name')

#Use the slice as an index to retrive the Layer and create a list of the Layars sequence for the points
Layers= Display.getFront().getLayerSet().getLayers()
zSeries=[]
for item in zA:
	zSeries.append(Layers[int(item-1)])

#Functions to create Balls
def createBall(name):
#Create a Ball object, that can contain numerous x,y,z,r balls
  layer = Display.getFrontLayer()
  ball = Ball(layer.project,str(name), 0, 0)
  layer.getParent().add(ball)
  layer.project.getProjectTree().insertSegmentations([ball])
  return ball
 
def addBall(ballob, x, y, radius, layer):
  ballob.addBall(x, y, radius, layer.id)
  ballob.repaint()

if single_ball:
#Create balls as part of the Ball Object
	ballob=createBall(Ball_name)
	for x,y,layer in zip(xA,yA,zSeries):
		addBall(ballob,x,y,radius,layer)
		if register_to_image:
			ballob.setAffineTransform(aff)
			ballob.repaint()
else:
	for name,x,y,layer in zip(Label,xA,yA,zSeries):
		if not name in ball_obs:
			ballob=createBall(name)
			addBall(ballob,x,y,radius,layer)
			if register_to_image:
				ballob.setAffineTransform(aff)
				ballob.repaint()
		else:
			print (name, name.type)
