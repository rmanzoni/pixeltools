import pickle
from collections import OrderedDict
from  readPixels import PixelROC


pixel_file = open('pixels.pkl', 'r')
pixels = pickle.load(pixel_file)
pixel_file.close()


def findByCoordinates(pixels, r, phi, z, 
                      r_tolerance = 1., 
                      phi_tolerance = 0.1, 
                      z_tolerance = 1.):
    
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





# example of how to select all ROCs belonging to Layer-1
lyrone = []
for k,v in pixels.iteritems():
    if 'LYR1' in k:
        lyrone.append((v.FED, v.channel))

print set(lyrone)



# example of how to select ROCs based on their r, phi and z position. 
# r coordinate identifies the layer
holes = {}
holes.update(findByCoordinates(pixels, 4, 0.5, 10))
holes.update(findByCoordinates(pixels, 4, 1.2,  3))
for k,v in bb.items(): 
    print k, v.FED, v.channel, v.phi, v.z