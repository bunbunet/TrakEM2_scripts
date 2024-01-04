import csv
import os
WORKING_DIR="C:\\Users\\Federico Luzzati\\Desktop\\Rabies XML 11 2020 bkp\\"
file_name="bellissimo.obj"
file_path = os.path.join(WORKING_DIR, file_name)
rows=["Specimen,CellType,pz,Region,Subregion,SubSubregion,Marker,notes,FullName,x,y,z"]
rows2=["name,x,y,z"]
Coordinates_file=open(file_path,"w+")

Coordinates_file.write("\n".join(rows))