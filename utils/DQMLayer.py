#!/usr/bin/python

import ROOT
import sys
sys.path.append('..')
from itertools import product
import numpy as np

def binx(module, roc):
    if roc > 7:
        roc = 15 - roc
    x  = 36 + 1 + 8 * module
    x += (roc-4)
    return x

def biny(ladder, roc, layer):
    if layer==1: half_n_bins = 21
    if layer==2: half_n_bins = 33
    if layer==3: half_n_bins = 45

    y  = half_n_bins + 1 + 2 * ladder - (ladder<0)
    if ladder > 0:
        y += (roc>7)
    else:
        y -= (roc<=7)
    return y

def readOccupancyPlot(occupancy):
    '''
    '''
    # ROC / Module
    xx = range(occupancy.GetNbinsX())
    
    # ROC / Ladder
    yy = range(occupancy.GetNbinsY())
    
    points = []
    
    for ix, iy in product(xx, yy):
        point = occupancy.GetBinContent(ix, iy)
            
        x = int(occupancy.GetXaxis().GetBinUpEdge(ix)-0.5) if ix < np.average(xx)+1 else int(occupancy.GetXaxis().GetBinLowEdge(ix)+0.5)
        y = int(occupancy.GetYaxis().GetBinUpEdge(iy))     if iy < np.average(yy)+1 else int(occupancy.GetYaxis().GetBinLowEdge(iy))
            
        if y<0:
            roc_one_half = 2 if abs(y - int(occupancy.GetYaxis().GetBinLowEdge(iy))) < 0.5 else 1
        elif y>0:
            roc_one_half = 2 if abs(y - int(occupancy.GetYaxis().GetBinUpEdge(iy))) > 0.5 else 1
           
        roc_one_eight =int(((occupancy.GetXaxis().GetBinLowEdge(ix) - x) + 0.5) * 8)
    
        if roc_one_half == 1:
            roc = roc_one_eight
        elif roc_one_half == 2:
            roc = 15 - roc_one_eight 
        else:
            print 'fuck you' 
        
        # true only for layer-1
        if x==0  or y==0 or abs(y)>9 or abs(x)>4:
            continue
        
        points.append((x, y, roc, point))    
    
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

    for roc in matched:
        x = binx(roc.module, roc.roc)
        y = biny(roc.ladder, roc.roc, layer)                
        content = histo.GetBinContent(x, y)
        if hasattr(roc, 'counts'):
            histo.SetBinContent(x, y, content+roc.counts)
        else:
            histo.SetBinContent(x, y, content+1.)
        
    return histo
        
    
    
    
if __name__ == '__main__':
    
    f1 = ROOT.TFile.Open('/Users/riccardomanzoni/Downloads/DQM_V0011_R000285244__StreamExpressPA__PARun2016B-Express-v1__DQMIO.root', 'r')
    f1.cd()
    occupancy = f1.Get('DQMData/Run 285244/Pixel/Run summary/Clusters/OnTrack/pix_bar Occ_roc_ontracksiPixelDigis_layer_1')    
    points = readOccupancyPlot(occupancy)
    f1.Close()
    
    import pickle
    from objects.PixelDetector import PixelDetector
    
    pixel_file = open('../data/pixels.pkl', 'r')
    pixels = pickle.load(pixel_file)
    pixel_file.close()

    matched = []
    
    for module, ladder, roc, counts in points:
        if counts <= 0: 
            continue
        matched += pixels.get(layer=1, module=module, ladder=ladder, roc=roc)
        matched[-1].counts = counts
        
    hh = fillOccupancyPlot(matched, 1)
    
    
    
    