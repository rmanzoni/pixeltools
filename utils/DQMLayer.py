#!/usr/bin/python

import ROOT
import sys
sys.path.append('..')
from itertools import product
import numpy as np

def setbinx(module, roc):
    if roc > 7 and module < 0:
        roc = 15 - roc
    if roc <= 7 and module > 0:
        roc = 7 - roc
    if roc > 7 and module > 0:
        roc = roc - 8 
    x  = 36 + 1 + 8 * module
    x += (roc-4)
    return x

def setbiny(ladder, roc, layer):
    if layer==1: half_n_bins = 21
    if layer==2: half_n_bins = 33
    if layer==3: half_n_bins = 45

    y  = half_n_bins + 2 * ladder + (ladder<0)
    if   ladder > 0 and abs(ladder)!=1 and abs(ladder)!=10:
        y += (roc>7)
    elif ladder < 0 and abs(ladder)!=1 and abs(ladder)!=10:
        y -= (roc<=7)
    else:
        pass
    
    y += (ladder==1)
    y -= (ladder==-1)
    
    return y



def readOccupancyPlot(occupancy):
    '''
    '''
    # ROC / Module
    xx = range(occupancy.GetNbinsX()+1)
    
    # ROC / Ladder
    yy = range(occupancy.GetNbinsY()+1)
    
    points = []
    
    for ix, iy in product(xx, yy):
        point = occupancy.GetBinContent(ix, iy)
          
        xbinlow = occupancy.GetXaxis().GetBinLowEdge(ix)  
        xbinup  = occupancy.GetXaxis().GetBinUpEdge (ix)
        ybinlow = occupancy.GetYaxis().GetBinLowEdge(iy)  
        ybinup  = occupancy.GetYaxis().GetBinUpEdge (iy)
                            
        x = int(xbinup - 0.5) if ix < np.average(xx) + 1 else int(xbinlow + 0.5)
        y = int(ybinup - 0.5) if iy < np.average(yy) + 1 else int(ybinlow + 0.5)
        
        roc_one_half = 1

        if y<0:
            roc_one_half = 2 if abs(y - int(ybinlow + 0.5)) > 0.5 else 1
        else:
            roc_one_half = 2 if abs(y - int(ybinup - 0.5)) < 0.5 else 1
                   
        roc_one_eight = int(((xbinlow - x) + 0.5) * 8)
    
        if x < 0:
            if roc_one_half == 1:
                roc = roc_one_eight
            elif roc_one_half == 2:
                roc = 15 - roc_one_eight 
            else:
                print 'fuck you' 

        if x > 0:
            if roc_one_half == 1:
                roc = 7 - roc_one_eight
            elif roc_one_half == 2:
                roc = 8 + roc_one_eight 
            else:
                print 'fuck you' 
           
        if x==0:
            continue

        # true only for layer-1
        if iy==1 or iy==42:
            continue
        if iy>=20 and iy<=23:
            continue
 
        # flipped ladders
        if (np.sign(x)*y)%2 == (x*y>0):
           roc = 15 - roc
       
        points.append((x, y, roc, point, ix, iy))    
        # points.append((x, y, roc, point))    
    
    # sort by occupancy
    points.sort(key=lambda t : t[3])
    
    return points

def fillOccupancyPlot(rocs, layer):
    
    if layer == 1: 
        histo = ROOT.TH2F('occupancy', 'occupancy', 72, -4.5, 4.5, 42, -10.5, 10.5)
    elif layer == 2: 
        histo = ROOT.TH2F('occupancy', 'occupancy', 72, -4.5, 4.5, 66, -16.5, 16.5)
    elif layer == 3: 
        histo = ROOT.TH2F('occupancy', 'occupancy', 72, -4.5, 4.5, 90, -22.5, 22.5)
    else: 
        print 'fuck you'

    for roc in rocs:
        x = setbinx(roc.module, roc.roc)
        y = setbiny(roc.ladder, roc.roc, layer)     
        content = histo.GetBinContent(x, y)
        #histo.SetBinContent(x, y, content+roc.roc+1)
        if hasattr(roc, 'counts'):
            histo.SetBinContent(x, y, content+roc.counts)
        else:
            histo.SetBinContent(x, y, content+1.)
        
    return histo
        
    
    
    
if __name__ == '__main__':
    pass    
    
    
    