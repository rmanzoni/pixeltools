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


def findByCMScoordinates(pixels, coords):
    selectedPix = OrderedDict()

    if len(coords) == 3:
        for kpix, vpix in pixels.iteritems():
            if vpix.layer  != coords[0]: continue
            if vpix.ladder != coords[1]: continue
            if vpix.module != coords[2]: continue
            selectedPix.update({kpix:vpix})

    if len(coords) == 5:
        for kpix, vpix in pixels.iteritems():
            if vpix.side   != coords[0]: continue
            if vpix.disk   != coords[1]: continue
            if vpix.blade  != coords[2]: continue
            if vpix.pannel != coords[3]: continue
            if vpix.plaq   != coords[4]: continue
            selectedPix.update({kpix:vpix})

    return selectedPix





# example of how to select all ROCs belonging to Layer-1
lyrone = []
for k,v in pixels.iteritems():
    if 'LYR1' in k:
        lyrone.append((v.FED, v.channel))

# print set(lyrone)



# example of how to select ROCs based on their r, phi and z position. 
# r coordinate identifies the layer
holes = {}
holes.update(findByCoordinates(pixels, 4, 0.5, 10))
holes.update(findByCoordinates(pixels, 4, 1.2,  3))
# for k,v in bb.items(): 
#     print k, v.FED, v.channel, v.phi, v.z
    
    
# example: get ROC names corresponding to a set of cms coordinates (only layer-1)
tofind = [
    (4 ,  8, 5	),# module 4	ladder 8	roc 5	
    (-1,  3, 3	),# module -1	ladder 3	roc 3	
    (-2,  5, 10	),# module -2	ladder 5	roc 10	
    (-2,  2, 1	),# module -2	ladder 2	roc 1	
    (-1, -1, 2	),# module -1	ladder -1	roc 2	
    (-4,  5, 9	),# module -4	ladder 5	roc 9	
    (4 ,  4, 5	),# module 4	ladder 4	roc 5	
    (-1, -7, 14	),# module -1	ladder -7	roc 14	
    (-4,  9, 15	),# module -4	ladder 9	roc 15	
    (-3, -9, 4	),# module -3	ladder -9	roc 4	
    (-3,  9, 0	),# module -3	ladder 9	roc 0	
    (-4,  9, 14	),# module -4	ladder 9	roc 14	
    (0 , -7, 8	),# module 0	ladder -7	roc 8	
    (-4, -8, 0	),# module -4	ladder -8	roc 0	
    (-2,  5, 13	),# module -2	ladder 5	roc 13	
    (-4, -1, 15	),# module -4	ladder -1	roc 15	
    (-4,  9, 13	),# module -4	ladder 9	roc 13	
    (-3,  6, 3	),# module -3	ladder 6	roc 3	
    (-3,  5, 13	),# module -3	ladder 5	roc 13	
    (-1, -7, 12	),# module -1	ladder -7	roc 12	
    (-4, -8, 1	),# module -4	ladder -8	roc 1	
    (-4, -8, 7	),# module -4	ladder -8	roc 7	
    (-4,  4, 3	),# module -4	ladder 4	roc 3	
    (-4,  9, 12	),# module -4	ladder 9	roc 12	
    (-4, -8, 2	),# module -4	ladder -8	roc 2	
    (-4, -7, 15	),# module -4	ladder -7	roc 15	
    (-4, -6, 0	),# module -4	ladder -6	roc 0	
    (0 ,  1, 10	),# module 0	ladder 1	roc 10	
    (-3,  5, 1	),# module -3	ladder 5	roc 1	
    (-4,  8, 0	),# module -4	ladder 8	roc 0	
]






tofind = [
    (4 ,  8, 5	),# module 4	ladder 8	roc 5	counts 1801
    (-1,  3, 3	),# module -1	ladder 3	roc 3	counts 6408
    (-2,  5, 10	),# module -2	ladder 5	roc 10	counts 8125
    (-2,  2, 1	),# module -2	ladder 2	roc 1	counts 10326
    (-1, -1, 2	),# module -1	ladder -1	roc 2	counts 13726
    (4 ,  4, 5	),# module 4	ladder 4	roc 5	counts 18559
    (-1, -7, 14	),# module -1	ladder -7	roc 14	counts 21922
    (-3, -9, 4	),# module -3	ladder -9	roc 4	counts 24428
    (-3,  9, 0	),# module -3	ladder 9	roc 0	counts 24799
    (1 , -7, 0	),# module 1	ladder -7	roc 0	counts 32012
    (-2,  5, 13	),# module -2	ladder 5	roc 13	counts 32917
    (-3,  6, 3	),# module -3	ladder 6	roc 3	counts 34381
    (-3,  5, 13	),# module -3	ladder 5	roc 13	counts 35197
    (-1, -7, 12	),# module -1	ladder -7	roc 12	counts 36612
    (1 ,  1, 2	),# module 1	ladder 1	roc 2	counts 45000
    (-3,  5, 1	),# module -3	ladder 5	roc 1	counts 46311
    (-1,  2, 8	),# module -1	ladder 2	roc 8	counts 51362
    (4 ,  9, 15	),# module 4	ladder 9	roc 15	counts 54775
    (1 ,  9, 4	),# module 1	ladder 9	roc 4	counts 54916
    (1 ,  9, 8	),# module 1	ladder 9	roc 8	counts 55823
    (1 ,  4, 2	),# module 1	ladder 4	roc 2	counts 58973
    (4 ,  9, 14	),# module 4	ladder 9	roc 14	counts 59077
    (2 ,  4, 3	),# module 2	ladder 4	roc 3	counts 60326
    (4 , -5, 12	),# module 4	ladder -5	roc 12	counts 60709
    (-3, -6, 12	),# module -3	ladder -6	roc 12	counts 61416
    (3 , -1, 3	),# module 3	ladder -1	roc 3	counts 63259
    (-2,  4, 1	),# module -2	ladder 4	roc 1	counts 65471
    (-2,  1, 4	),# module -2	ladder 1	roc 4	counts 67599
    (1 ,  5, 7	),# module 1	ladder 5	roc 7	counts 68104
    (-3,  1, 3	),# module -3	ladder 1	roc 3	counts 69274
    (3 , -5, 1	),# module 3	ladder -5	roc 1	counts 72452
    (4 ,  9, 13	),# module 4	ladder 9	roc 13	counts 72457
    (-1, -9, 13	),# module -1	ladder -9	roc 13	counts 72472
    (4 , -1, 15	),# module 4	ladder -1	roc 15	counts 73353
    (-3,  3, 7	),# module -3	ladder 3	roc 7	counts 73485
    (-3,  5, 9	),# module -3	ladder 5	roc 9	counts 74015
    (4 ,  1, 6	),# module 4	ladder 1	roc 6	counts 74331
    (-3, -9, 6	),# module -3	ladder -9	roc 6	counts 76512
    (1 ,  1, 9	),# module 1	ladder 1	roc 9	counts 77113
    (-3, -9, 7	),# module -3	ladder -9	roc 7	counts 77778
    (-3, -9, 1	),# module -3	ladder -9	roc 1	counts 78111
    (4 ,  9, 12	),# module 4	ladder 9	roc 12	counts 78227
    (-3, -9, 3	),# module -3	ladder -9	roc 3	counts 78396
    (3 , -3, 1	),# module 3	ladder -3	roc 1	counts 78985
    (3 , -5, 10	),# module 3	ladder -5	roc 10	counts 79263
    (4 , -8, 3	),# module 4	ladder -8	roc 3	counts 79765
    (-3,  1, 2	),# module -3	ladder 1	roc 2	counts 80668
    (-3, -9, 0	),# module -3	ladder -9	roc 0	counts 80700
    (-3, -9, 2	),# module -3	ladder -9	roc 2	counts 81122
    (4 ,  4, 1	),# module 4	ladder 4	roc 1	counts 81170
]

keys = pixels.keys()





for ff in tofind:
    rocs = keys
    
    print 'module %d ladder %d roc %d' %(ff[0], ff[1], ff[2])
    
    # layer
    rocs = [k for k in rocs if 'LYR1' in k]
    # module
    rocs = [k for k in rocs if 'MOD%d'%abs(ff[0]) in k]
    # sign of the module
    rocs = [k for k in rocs if (('Bm' in k and ff[0]<0) or ('Bp' in k and ff[0]>0))]
    # ladder
    rocs = [k for k in rocs if 'LDR%d'%abs(ff[1]) in k]
    # sign of the ladder
    rocs = [k for k in rocs if (('O_SEC' in k and ff[1]<0) or ('I_SEC' in k and ff[1]>0))]
    # roc
    rocs = [k for k in rocs if k.endswith('ROC%d'%ff[2])]

    print rocs



# 302056208 BPix_BmI_SEC2_LYR1_LDR3F_MOD1 r/phi/z = 4.61295/0.872665/-3.35 cmssw layer/ladder/module 1/3/4 0.872665


