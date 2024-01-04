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

Markers=["0","cK_no","cKcKD_no","cKD_no","cK_RFP","cKcKD_RFP","cKD_RFP","cK_Mem","cKcKD_Mem","cKD_Mem","cK_Cyt","cKcKD_Cyt","cKD_Cyt"]

#set the colors of the cell types (not active for the moment)
#color1=Color.green  e così via per tutti i color che vuoi

#-----------------------------CODE--------------------------
Do_not_reimport=False
if Do_not_reimport:
	ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)
else:
	ball_obs=[]

p=Display.getFront().getActive()
aff= p.getAffineTransform()
Current_layer=Display.getFrontLayer()

#import point coordinates and names from resultTable
rt = ResultsTable.getResultsTable()
xA = rt.getColumn(rt.getColumnIndex('X'))
yA = rt.getColumn(rt.getColumnIndex('Y'))
zA = rt.getColumn(rt.getColumnIndex('Slice'))
Label = rt.getColumn(rt.getColumnIndex('Counter'))
#For String Columns use:
#Label = rt.getColumnAsVariables('Name')

#Get currrent layer
Current_layer=Display.getFrontLayer()

#Get current layer index
Layers= Display.getFront().getLayerSet().getLayers()
Base_layer_index=Layers.index(Current_layer)

#Create a List of layer indexes from the Slice
zSeries=[]
for item in zA:
	zSeries.append(Layers[int(item-1+Base_layer_index)])

# print("current layer:",Current_layer,Base_layer_index)

#Empty dictionaries to collect the coordinates for each counter type
X={}
Y={}
Z={}
#L={}

#in multitool the counter variable assing the marker type and can thus be repeted
#two parallel dictionaries are built in which the list of coordinates are divided by marker type
#this makes it easier to rename the files
#{Label[1]:[x1,x2,x3,x4..xn]; Label[2]:[x1,x2,x3,x4,5]

for key in Label:
	if key in Label:
		X[key]=[]
		Y[key]=[]
		Z[key]=[]
#		L[key]=[]
	for i in range(0,len(Label)):
		if Label[i]==key:
			X[key].append(xA[i])
			Y[key].append(yA[i])
			Z[key].append(zSeries[i])
#			L[key].append(Label[i])
			
# rename the markers (da 1,2,3,4, ecc a nome giusto "Markers" all'inizio)
counter=0
for marker in Markers:
	try:
		X[marker]=X.pop(counter)
	except KeyError:
		pass
	counter+=1

print(X)

counter=0
for marker in Markers:
	try:
		Y[marker]=Y.pop(counter)
	except KeyError:
		pass
	counter+=1
print(Y)

counter=0
for marker in Markers:
	try:
		Z[marker]=Z.pop(counter)
	except KeyError:
		pass
	counter+=1

print(Z)


# giusto per avere una verifica
for key in X:
	print(key)
	for i,j,h in zip(X[key],Y[key],Z[key]):
		print("  x:",i)
		print("  y:",j)
		print("  z:",h)

#for marker in Markers:
# 	try:
#		L[marker]=L.pop(counter)
#	except KeyError:
#		pass
#	counter+=1


### non c'è mai un punto in cui si definisce la corrispondenza tra marker e nome nuovo da dare a ball!!
# provato a modificare un po' sopra... ma forse il problema è qua sotto... impostato per creare ball che contengono diverse ball
#  forse se si mette stringente, fai una ball per ciascuno non c'è il problema?

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
		for x,y,layer in zip(X[key],Y[key],Z[key]):
			addBall(ballob,x,y,radius,layer)
		ballob.setAffineTransform(aff)
		ballob.repaint()
			



