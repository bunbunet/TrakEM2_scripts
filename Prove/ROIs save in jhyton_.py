from ij.plugin.frame import RoiManager;

rm = RoiManager.getInstance();
if (rm==None):
    rm = RoiManager();
imp = IJ.openImage("http://imagej.nih.gov/ij/images/blobs.gif");
imp.setRoi(100, 80, 50, 80);
rm.addRoi(imp.getRoi());
imp.setRoi(180, 140, 30, 40);
rm.addRoi(imp.getRoi());
rm.runCommand("Deselect"); # deselect ROIs to save them all
rm.runCommand("Save", IJ.getDirectory("home") + "RoiSet.zip");
imp.show();