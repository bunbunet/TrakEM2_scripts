from ini.trakem2.display import Display, Ball, Profile

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

#Create a ball in each layer at the same position
ballob=createBall("prova")
for layer in layers:
	addBall(ballob,642,642,10,layer)
ballob.repaint()