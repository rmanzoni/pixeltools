#!/usr/bin/python

import re
import ROOT
import pickle
import sys
sys.path.append('..')
import numpy as np
from itertools import product
from collections import OrderedDict

from objects.PixelDetector import PixelDetector
from utils.DQMLayer import readOccupancyPlot, fillOccupancyPlot

# load pixel detector object (containing all ROCs)
pixel_file = open('../data/pixels.pkl', 'r')
pixels = pickle.load(pixel_file)
pixel_file.close()

quadruplets = [
    ('../data/dqmfiles/DQM_V0006_R000283964__StreamExpress__Run2016H-Express-v2__DQMIO.root'    , 'DQMData/Run 283964/Pixel/Run summary/Clusters/OnTrack/pix_bar Occ_roc_ontracksiPixelDigis_layer_1', 'pp collisions - Run 283964', 'layer_one_occupancy_run283964.pdf'),
    ('../data/dqmfiles/DQM_V0008_R000285090__StreamExpressPA__PARun2016B-Express-v1__DQMIO.root', 'DQMData/Run 285090/Pixel/Run summary/Clusters/OnTrack/pix_bar Occ_roc_ontracksiPixelDigis_layer_1', 'pPb collisions - Run 285090', 'layer_one_occupancy_run285090.pdf'),
    ('../data/dqmfiles/DQM_V0020_R000285216__StreamExpressPA__PARun2016B-Express-v1__DQMIO.root', 'DQMData/Run 285216/Pixel/Run summary/Clusters/OnTrack/pix_bar Occ_roc_ontracksiPixelDigis_layer_1', 'pPb collisions - Run 285216', 'layer_one_occupancy_run285216.pdf'),
    ('../data/dqmfiles/DQM_V0011_R000285244__StreamExpressPA__PARun2016B-Express-v1__DQMIO.root', 'DQMData/Run 285244/Pixel/Run summary/Clusters/OnTrack/pix_bar Occ_roc_ontracksiPixelDigis_layer_1', 'pPb collisions - Run 285244', 'layer_one_occupancy_run285244.pdf'),
    ('../data/dqmfiles/DQM_V0007_R000285368__StreamExpressPA__PARun2016B-Express-v1__DQMIO.root', 'DQMData/Run 285368/Pixel/Run summary/Clusters/OnTrack/pix_bar Occ_roc_ontracksiPixelDigis_layer_1', 'pPb collisions - Run 285368', 'layer_one_occupancy_run285368.pdf'),
]

aaa = OrderedDict()

for tt in quadruplets:
    
    print '\n\n\n====> ', tt[2]
    print 'list of ROCs that deviate more than 2 sigma from the average'
    print 'occupancy in their own module x ladder block (16 ROCs)\n'
    
    f1 = ROOT.TFile.Open(tt[0], 'r')
    f1.cd()
    occupancy = f1.Get(tt[1])    

    points = readOccupancyPlot(occupancy)        
    f1.Close()

    # match the low occupancy ROCs to the ROC objects
    matched = []

    for module, ladder, roc, counts, dd, ddd in points:
        if counts <= 0: 
            continue
            
        #if any(i for i in pixels.get(layer=1, module=module, ladder=ladder, roc=roc) if i in matched):
        #    import pdb ; pdb.set_trace()
        
        matched += pixels.get(layer=1, module=module, ladder=ladder, roc=roc)
        matched[-1].counts = counts
        # matched[-1].counts = roc + 1 # only for debugging!
    
    # find low occupancy ROCs
    # those that deviate more than -2 RMS from the average of
    # their module-ladder block
    lowoccupancy = []

    for ladder, module in product(range(-9, 10), range(-4, 5)):
        block = [p for p in matched if p.module == module and p.ladder==ladder]
        average = np.average([i.counts for i in block])
        rms = np.std([i.counts for i in block])
        lowoccupancy.extend([i for i in block if i.counts < average - 2 * rms])

    # for roc in lowoccupancy:
    #     print roc.name#, roc.counts, roc.module, roc.ladder
        
    aaa.update({int(tt[2].split()[-1]):sorted(lowoccupancy, key=lambda x:x.name)})
     
#     hh = fillOccupancyPlot(matched, 1)
# 
#     histo = ROOT.TH2F('occupancy layer-1', 'occupancy layer-1', 72, -4.5, 4.5, 42, -10.5, 10.5)
#     for p in points:
#         histo.SetBinContent(p[4], p[5], p[2]+1)
#     ROOT.gStyle.SetOptStat(0)
#     histo.GetXaxis().SetTitle('Module')
#     histo.GetYaxis().SetTitle('Ladder')
#     histo.GetZaxis().SetTitle('ROC')
#     histo.Draw('colz')
#     ROOT.gPad.Update()




allrocs = []

for i in aaa.values():
    allrocs.extend(i)

allrocs = list(set(allrocs))


jj = ROOT.TH2F('lowOccVsRun', 'lowOccVsRun', len(allrocs), 0, len(allrocs)-1, 5, 0, 5)

for k, v in aaa.iteritems():
    for vv in v:
        jj.Fill(str(k), vv.name, 1.)
    
    



