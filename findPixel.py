import pickle
from collections import OrderedDict
from  readPixels import PixelROC


pixel_file = open('pixels.pkl', 'r')
pixels = pickle.load(pixel_file)
pixel_file.close()


def findByCoordinates(pixels, r, phi, z, 
                      r_tolerance = 0.5, phi_tolerance = 0.1, z_tolerance = 1.):
    
    selectedPix = OrderedDict()
    
    for kpix, vpix in pixels.iteritems():
        if abs(vpix.r   - r  ) > r_tolerance: continue
        if abs(vpix.phi - phi) > phi_tolerance: continue
        if abs(vpix.z   - z  ) > z_tolerance: continue        
        selectedPix.update({kpix:vpix})
        
    return selectedPix


def findByFEDandChannel(pixels, fed, ch): 

    selectedPix = OrderedDict()
    
    for kpix, vpix in pixels.iteritems():
        if vpix.FED     != fed: continue
        if vpix.channel != ch : continue
        selectedPix.update({kpix:vpix})
                
    return selectedPix




centerPix = findByCoordinates(pixels, 6.13085, -1.43071, -33.8437)


lyrone = []

for k,v in pixels.iteritems():
    if 'LYR1' in k:
        print v.FED, v.channel
        lyrone.append((v.FED, v.channel))

print set(lyrone)



# 344018180 FPix_BmI_D1_BLD12_PNL1_PLQ1 r/phi/z = 6.23085/-1.46071/-33.6437 cmssw side/disk/blade/pannel/plaq=1/1/19/1/1 0.939693








# sector 3 or what? control power tripped 
# 
# monitor currents analog and digital
# 
# optical power current
# 
# address lv calib
# 
# delay 25 calib   make sure we're talking to the detector


