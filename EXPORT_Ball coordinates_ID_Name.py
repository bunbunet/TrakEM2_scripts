from ini.trakem2.display import Display, Ball
from ij.text import TextWindow

ball_obs = Display.getFront().getLayerSet().getZDisplayables(Ball)
 
# One entry for each id,x,y,z,r 
rows = []
 
# Iterate every Ball instance, which contains one or more x,y,z,r balls
for ball_ob in ball_obs:
  id = ball_ob.getId()
  title = ball_ob.getTitle()
  # Iterate every x,y,z,r ball of a Ball instance, calibrated
  wbs = ball_ob.getWorldBalls()
  for ball_coords in wbs:
    # Store every ball as a row with id, x, y, z, r
    rows.append(str(id) +","+ title + "," + ",".join(str(c) for c in ball_coords))
 
csv = "\n".join(rows)
 
t = TextWindow("Balls CSV", csv, 400, 400)