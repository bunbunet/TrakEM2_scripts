from ini.trakem2.display import Display, Ball, Profile
from ini.trakem2.utils import M, Utils

#Get currrent layer
Current_layer=Display.getFrontLayer()
#Get current layer index
Layers= Display.getFront().getLayerSet().getLayers()
Base_layer_index=Layers.index(Current_layer)+1

print(Current_layer,Base_layer_index)

