#SET layers distance as layer thickness

#This script calculate the distance between pairs of subsequent layers 
#and assign it as the section thickness of the first layer in the pair.
#This procedure allow to calculate correct arealists volumes for unevenly spaced sections.
#It requires that an open display

from ini.trakem2.display import Display, Patch
from ini.trakem2 import Project

#Compute the Section Thickness in Pixels, (pixel size * section thickness)
#this value will be assigned to the last layer of the layerset
section_thickness=50

#list all the layers in the project
layers=Display.getFront().getLayerSet().getLayers()

#Get the Z values
zList=[]
for layer in layers:
		z = layer.getZ()
		zList.append(z)

# Calculate the distance between layers:
thicknessList=[]
for i in range(len(zList)-1):
    thicknessList.append(abs(zList[i] - zList[i+1]))
thicknessList.append(section_thickness)

# Uncomment to print and verify thickness list
print(thicknessList)

#Set the computed thickness to each layers
for thickness,layer in zip(thicknessList,layers):
  		layer.setThickness(thickness)

# Update the GUI
Display.getFront().getLayerSet().getProject().getLayerTree().updateUILater()
