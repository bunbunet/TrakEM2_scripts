from ini.trakem2.display import Display, Ball, Profile
from ij.measure import ResultsTable
from ij import IJ

rt = ResultsTable.getResultsTable()
xA = rt.getColumn(rt.getColumnIndex('X'))
yA = rt.getColumn(rt.getColumnIndex('Y'))
zA = rt.getColumn(rt.getColumnIndex('Slice'))
#Label = rt.getColumn(rt.getColumnIndex('Counter'))


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

#Create multiple ball in each layer at the same position
ballob=createBall("prova")
for layer in Display.getFront().getLayerSet().getLayers():
	for x,y in zip(xA,yA):
		addBall(ballob,x,y,10,layer)
ballob.repaint()