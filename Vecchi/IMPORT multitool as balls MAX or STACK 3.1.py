#This code read X,Y coordinates of muti-point selections from Result Table and import them to TrakEM2 as Balls with spacific names.
#To run first add the multipoint to ROI manager, 
#RESET IMAGE CALIBRATION (forse non serve più), than "measure" and check that a Rsult Tables opens, select the corresponding image in TrakEM2 and run the script
#The added points are automatically transformed and linked to the original image.
#You only need to specify the ball radius, the markers names and their colors. 

from ini.trakem2.display import Display, Ball, Profile
from ini.trakem2.utils import M, Utils
from ij.measure import ResultsTable
from ij import IJ
from java.awt import Color

#--------------USER DEFINED VARIABLES AND OPTIONS---------
#Specify the Ball Radius
radius=10
#Set True to import in single plane (e.g on MAX projection)
MAX_project=False
#NOTE:TO IMPORT STACK SELECT THE FIRST PLANE
#SET FALSE ONLY IF SLICE LAYERS ALREADY EXISTS IN THE RECONSTRUCTION!
#-----------------------------MARKER NAMES--------------------------

#Set a base name for the imported balls
base_name="Point"
#Uncomment to use the selected patch name as title
#base_name=Display.getFront().getActive().title
Markers=["ck","cKD"]

#SPECIFY Marker's name. 
Marker1=base_name+"1"
Marker2=base_name+"2"
Marker3=base_name+"3"
Marker4=base_name+"4"
Marker5=base_name+"5"
Marker6=base_name+"6"
#set the colors of the cell types (not active for the moment)
#color1=Color.green
#color2=Color.red
#color3=Color.yellow

#-----------------------------CODE--------------------------

#Get currrent layer
Current_layer=Display.getFrontLayer()
#Get current layer index
Layers= Display.getFront().getLayerSet().getLayers()
Base_layer_index=Layers.index(Current_layer)

Layers= Display.getFront().getLayerSet().getLayers()
zSeries=[]
for item in zA:
	zSeries.append(Layers[int(item-1+Base_layer_index)])

print("current layer:",Current_layer,Base_layer_index)



Do_not_reimport=False
if Do_not_reimport:
	ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)
else:
	ball_obs=[]

p=Display.getFront().getActive()
aff= p.getAffineTransform()
tit= p.getTitle
Current_layer=Display.getFrontLayer()

#import point coordinates and names from resultTable
rt = ResultsTable.getResultsTable()
xA = rt.getColumn(rt.getColumnIndex('X'))
yA = rt.getColumn(rt.getColumnIndex('Y'))
zA = rt.getColumn(rt.getColumnIndex('Slice'))
Label = rt.getColumn(rt.getColumnIndex('Counter'))
#For String Columns use:
#Label = rt.getColumnAsVariables('Name')



#Empty dictionaries to collect the coordinates for each counter type
X={}
Y={}
Z={}
#in multitool the counter variable assing the marker type and can thus be repeted
#two parallel dictionaries are built in which the list of coordinates are divided by marker type
#this makes it easier to rename the files
#{Label[1]:[x1,x2,x3,x4..xn]; Label[2]:[x1,x2,x3,x4,5]
for key in Label:
	if key in Label:
		X[key]=[]
		Y[key]=[]
		Z[key]=[]
	for i in range(0,len(Label)):
		if Label[i]==key:
			X[key].append(xA[i])
			Y[key].append(yA[i])
			Z[key].append(zA[i])

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
#and Z 
try:
	Z[Marker1]=Z.pop(1.0)
except KeyError:
	pass
try:	
	Z[Marker2]=Z.pop(2.0)
except KeyError:
	pass
try:
	Z[Marker3]=Z.pop(3.0)
except KeyError:
	pass
try:
	Z[Marker4]=Z.pop(4.0)
except KeyError:
	pass
try:
	Z[Marker5]=Z.pop(5.0)
except KeyError:
	pass
try:
	Z[Marker6]=Z.pop(6.0)
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
	if MAX_project:
		for i,j in zip(X[key],Y[key]):
			addBall(ballob, i,j, radius, Display.getFrontLayer())
		ballob.setAffineTransform(aff)
		ballob.repaint()
	else:
		for x,y,layer in zip(xA,yA,zSeries):
			addBall(ballob,x,y,radius,layer)
		ballob.setAffineTransform(aff)
		ballob.repaint()
			




