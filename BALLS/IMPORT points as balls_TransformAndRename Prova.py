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

selected_image=Display.getFront().getActive()
aff= selected_image.getAffineTransform()

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
	




