#This script add a ball object to the open TrakEM2 project form point coordinates
#listed in the Result Table where x,y and layers values are indicated in columns
#names X,Y and Slice

from ini.trakem2.display import Display, Ball, Profile
from ij.measure import ResultsTable
from ij import IJ


#Set True if you want to apply the transform of an existing patch (must be selected)
register_to_image=True
#Set True if you want to add balls to a single Ball Object
#Set False if you want each point to have its named ball Object
single_ball=False
#Specify the Ball Name (if single_ball=True)
Ball_name="Ball"
#Specify the Ball Radius
radius=10
#Set False to import balls with existing names
Do_not_reimport=False

Base_layer=94
print(Display.getFrontLayer())

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
zA = rt.getColumn(rt.getColumnIndex('Slice'))
Label = rt.getColumnAsVariables('Counter')

for lab in range(len(Label)):
	print(Label[lab])
	print(type(Label[lab]))
#Rename counter variables
#Markers=["0","cK_no","cKcKD_no","cKD_no","cK_RFP","cKcKD_RFP","cKD_RFP","cK_Mem","cKcKD_Mem","cKD_Mem","cK_Cyt","cKcKD_Cyt","cKD_Cyt"]

for i in range(len(Label)):
	if Label[i]==1:
		Label[i]="cK_no"
	elif Label[i]==2:
		Label[i]="cKcKD_no"
	elif Label[i]==3:
		Label[i]="cKD_no"
	elif Label[i]==4:
		Label[i]="cK_RFP"
	elif Label[i]==5:
		Label[i]="cKcKD_RFP"
	elif Label[i]==6:
		Label[i]="cKD_RFP"
	elif Label[i]==7:
		Label[i]="cK_Mem"
	elif Label[i]==8:
		Label[i]="cKcKD_Mem"
	elif Label[i]==9:
		Label[i]="cKD_Mem"
	elif Label[i]==10:
		Label[i]="cK_Cyt"
	elif Label[i]==11:
		Label[i]="cKcKD_Cyt"
	elif Label[i]==12:
		Label[i]="cKD_Cyt"			
						

#Use the slice as an index to retrive the Layer and create a list of the Layers sequence for the points
Layers= Display.getFront().getLayerSet().getLayers()
zSeries=[]
for item in zA:
	zSeries.append(Layers[int(item-1)+Base_layer-1])

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
