
# This Jython script is meant to be run from Fiji with TrakEM2 
# to extract all pipes and convert them to an SWC tree file 
# 
# Jan Kybic, January 2011 (based on Albert Cardona's example) 


from ini.trakem2.display import Display, Pipe 
import re 

def save_as_swc(pattern,fn): 
    """ Get all pipes in the current TrakEM2 project the name of which 
    corresponds to given regular pattern. The centerlines of these 
    pipes are saved in an SWC file 'fn'. Note that the pipes are not 
    connected in the SWC file. """ 

    layerset = Display.getFront().getLayerSet() 
    calibration = layerset.getCalibrationCopy() 
    f=file(fn,'w') 
    f.write('# Generated by pipes2swc.py from a TrakEM2 project\n') ; 
    ptnum=0 

    for pipe in layerset.getZDisplayables(Pipe): 
        id = pipe.getId() 
        if re.match(pattern,repr(pipe)): 
            vs = pipe.asVectorString3D() 
            vs.calibrate(calibration) 
            x = vs.getPoints(0) 
            y = vs.getPoints(1) 
            z = vs.getPoints(2) 
            prev=-1 
            for i in xrange(len(x)): 
                ptnum=ptnum+1 
                f.write('%d 0 %f %f %f 1 %d\n' % 
(ptnum,x[i],y[i],z[i],prev)) 
                prev=ptnum 

    f.close() ; 


if __name__ == "__main__": 
    # just an example 
    save_as_swc('ves','livevessels.swc') ;