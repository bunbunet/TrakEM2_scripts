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

# Get ball lists to avoid reimporting
ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)
ball_names=[]
for ball_ob in ball_obs:
	title = ball_ob.getTitle()
	ball_names.append(title)
	
#for ball in range(0,len(ball_obs)):
	

#specify the ball radius
radius=10

#Functions to create Ball object and add balls
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

# Get the transformation of the active image
p=Display.getFront().getActive()
aff= p.getAffineTransform()

#import point coordinates and names from resultTable
rt = ResultsTable.getResultsTable()
Xs = rt.getColumn(rt.getColumnIndex('X'))
Ys = rt.getColumn(rt.getColumnIndex('Y'))
Labels = rt.getColumnAsVariables('ID')

for label in Labels:
	print(label)

#Running the function for each Counter Type
for label,x,y in zip(Labels,Xs,Ys):
	Ball_Name= str(label)
	if not Ball_Name in ball_names:
		ballob = createBall(Ball_Name)
		addBall(ballob, x,y, radius, Display.getFrontLayer())
		ballob.setAffineTransform(aff)
		ballob.repaint()

 

	




