import ROOT
import numpy as np
from itertools import product

f1 = ROOT.TFile.Open('/Users/riccardomanzoni/Downloads/DQM_V0008_R000285090__StreamExpressPA__PARun2016B-Express-v1__DQMIO.root', 'r')
f1.cd()
occupancy = f1.Get('DQMData/Run 285090/Pixel/Run summary/Clusters/OnTrack/pix_bar Occ_roc_ontracksiPixelDigis_layer_1')

# ROC / Module
xx = range(occupancy.GetNbinsX())

# ROC / Ladder
yy = range(occupancy.GetNbinsY())

points = []

for ix, iy in product(xx, yy):
    point = occupancy.GetBinContent(ix, iy)
        
#     x = int(occupancy.GetXaxis().GetBinUpEdge(ix)*2)/2 if ix < np.average(xx)+1 else int(occupancy.GetXaxis().GetBinLowEdge(ix)*2)/2
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
    
    if x==0  or y==0 or abs(y)>9 or abs(x)>4:
        continue
    
    points.append((x, y, roc, point))    

# sort by occupancy
points.sort(key=lambda t : t[3])

low_but_not_zero = [p for p in points if p[3]>0]

low_but_not_zero_and_not_minus_four = [p for p in low_but_not_zero if p[0]>-4]

# print the 30 least occupied ROCs
# for p in low_but_not_zero[:50]:
#     print 'module %d\tladder %d\troc %d\tcounts %d' %(p[0], p[1], p[2], p[3])

# for p in points[:50]:
#     print 'module %d\tladder %d\troc %d\tcounts %d' %(p[0], p[1], p[2], p[3])

# print the 30 least occupied ROCs
for p in low_but_not_zero_and_not_minus_four[:50]:
    print 'module %d\tladder %d\troc %d\tcounts %d' %(p[0], p[1], p[2], p[3])


# module 4	ladder 8	roc 5	counts 1801    ok
# module -1	ladder 3	roc 3	counts 6408    ok
# module -2	ladder 5	roc 10	counts 8125    ok
# module -2	ladder 2	roc 1	counts 10326    ok
# module -1	ladder -1	roc 2	counts 13726    ok
# module -4	ladder 5	roc 9	counts 16580    ok
# module 4	ladder 4	roc 5	counts 18559    ok
# module -1	ladder -7	roc 14	counts 21922    ok
# module -4	ladder 9	roc 15	counts 23918
# module -3	ladder -9	roc 4	counts 24428
# module -3	ladder 9	roc 0	counts 24799
# module -4	ladder 9	roc 14	counts 30042
# module 0	ladder -7	roc 8	counts 32012
# module -4	ladder -8	roc 0	counts 32695
# module -2	ladder 5	roc 13	counts 32917
# module -4	ladder -1	roc 15	counts 33298
# module -4	ladder 9	roc 13	counts 33687
# module -3	ladder 6	roc 3	counts 34381
# module -3	ladder 5	roc 13	counts 35197
# module -1	ladder -7	roc 12	counts 36612
# module -4	ladder -8	roc 1	counts 37855
# module -4	ladder -8	roc 7	counts 38637
# module -4	ladder 4	roc 3	counts 39371
# module -4	ladder 9	roc 12	counts 40327
# module -4	ladder -8	roc 2	counts 41069
# module -4	ladder -7	roc 15	counts 43413
# module -4	ladder -6	roc 0	counts 44839
# module 0	ladder 1	roc 10	counts 45000
# module -3	ladder 5	roc 1	counts 46311
# module -4	ladder 8	roc 0	counts 47001