import ROOT

ROOT.gStyle.SetOptStat(0)

def binx(module, roc):
    if roc > 7:
        roc = 15 - roc
    x  = 36 + 1 + 8 * module
    x += (roc-4)
    return x

def biny(ladder, roc):
    y  = 21 + 1 + 2 * ladder #- (ladder<0)
    if ladder > 0:
        pass
        #y += (roc>7)
    else:
        y -= (roc<7)
    return y


danek = [
    'BPix_BmO_SEC1_LYR3_LDR3F_MOD2_ROC4',
    'BPix_BmO_SEC2_LYR2_LDR3F_MOD3_ROC12',
    'BPix_BmO_SEC2_LYR3_LDR4F_MOD1_ROC2',
    'BPix_BmO_SEC3_LYR3_LDR7F_MOD1_ROC13',
    'BPix_BmO_SEC3_LYR3_LDR9F_MOD1_ROC10',
    'BPix_BmO_SEC4_LYR2_LDR8F_MOD3_ROC11',
    'BPix_BmO_SEC5_LYR3_LDR12F_MOD1_ROC15',
    'BPix_BmO_SEC7_LYR2_LDR14F_MOD4_ROC11',
    'BPix_BmO_SEC7_LYR3_LDR17F_MOD1_ROC11',
    'BPix_BmO_SEC7_LYR3_LDR17F_MOD4_ROC3',
    'BPix_BmO_SEC8_LYR1_LDR10H_MOD3_ROC11',
    'BPix_BmI_SEC1_LYR1_LDR1H_MOD1_ROC11',
    'BPix_BmI_SEC1_LYR1_LDR1H_MOD1_ROC15',
    'BPix_BmI_SEC1_LYR1_LDR1H_MOD2_ROC9',
    'BPix_BmI_SEC1_LYR1_LDR2F_MOD2_ROC1',
    'BPix_BmI_SEC2_LYR1_LDR3F_MOD1_ROC2',
    'BPix_BmI_SEC2_LYR1_LDR3F_MOD3_ROC8',
    'BPix_BmI_SEC2_LYR3_LDR6F_MOD3_ROC8',
    'BPix_BmI_SEC4_LYR3_LDR10F_MOD2_ROC11',
    'BPix_BmI_SEC5_LYR1_LDR6F_MOD1_ROC4',
    'BPix_BmI_SEC5_LYR1_LDR6F_MOD4_ROC9',
    'BPix_BmI_SEC5_LYR3_LDR12F_MOD3_ROC12',
    'BPix_BmI_SEC6_LYR2_LDR12F_MOD4_ROC14',
    'BPix_BmI_SEC7_LYR1_LDR8F_MOD3_ROC9',
    'BPix_BmI_SEC7_LYR1_LDR8F_MOD4_ROC14',
    'BPix_BmI_SEC7_LYR2_LDR13F_MOD4_ROC15',
    'BPix_BmI_SEC8_LYR1_LDR9F_MOD2_ROC8',
    'BPix_BmI_SEC8_LYR1_LDR9F_MOD3_ROC15',
    'BPix_BmI_SEC8_LYR2_LDR15F_MOD4_ROC3',
    'BPix_BmI_SEC8_LYR3_LDR21F_MOD2_ROC4',
    'BPix_BpO_SEC1_LYR3_LDR3F_MOD3_ROC7',
    'BPix_BpO_SEC4_LYR1_LDR5F_MOD2_ROC3',
    'BPix_BpO_SEC4_LYR1_LDR5F_MOD4_ROC11',
    'BPix_BpO_SEC4_LYR3_LDR10F_MOD4_ROC0',
    'BPix_BpO_SEC4_LYR3_LDR11F_MOD2_ROC10',
    'BPix_BpO_SEC6_LYR3_LDR14F_MOD3_ROC4',
    'BPix_BpO_SEC7_LYR1_LDR8F_MOD1_ROC15',
    'BPix_BpO_SEC8_LYR3_LDR20F_MOD3_ROC0',
    'BPix_BpO_SEC8_LYR3_LDR21F_MOD1_ROC8',
    'BPix_BpI_SEC1_LYR2_LDR1H_MOD4_ROC3',
    'BPix_BpI_SEC1_LYR2_LDR2F_MOD4_ROC4',
    'BPix_BpI_SEC2_LYR3_LDR6F_MOD1_ROC13',
    'BPix_BpI_SEC2_LYR3_LDR6F_MOD4_ROC7',
    'BPix_BpI_SEC3_LYR1_LDR4F_MOD2_ROC12',
    'BPix_BpI_SEC4_LYR1_LDR5F_MOD1_ROC7',
    'BPix_BpI_SEC5_LYR1_LDR6F_MOD4_ROC8',
    'BPix_BpI_SEC5_LYR1_LDR6F_MOD4_ROC15',
    'BPix_BpI_SEC6_LYR2_LDR11F_MOD2_ROC8',
    'BPix_BpI_SEC7_LYR1_LDR8F_MOD4_ROC10',
    'BPix_BpI_SEC7_LYR2_LDR13F_MOD4_ROC3',
    'BPix_BpI_SEC8_LYR2_LDR15F_MOD2_ROC7',
    'BPix_BmO_SEC1_LYR1_LDR2F_MOD4_ROC9',
    'BPix_BmO_SEC1_LYR3_LDR3F_MOD3_ROC5',
    'BPix_BmO_SEC4_LYR2_LDR8F_MOD1_ROC2',
    'BPix_BmI_SEC5_LYR1_LDR6F_MOD1_ROC3',
    'BPix_BmI_SEC8_LYR3_LDR21F_MOD2_ROC15',
    'BPix_BpI_SEC2_LYR3_LDR6F_MOD4_ROC6',
    'BPix_BpI_SEC5_LYR1_LDR6F_MOD2_ROC13',
    'BPix_BpI_SEC6_LYR2_LDR11F_MOD3_ROC2',
    'BPix_BpI_SEC6_LYR2_LDR11F_MOD3_ROC11',
]


danek = [
    'BPix_BpO_SEC2_LYR1_LDR3F_MOD3_ROC1',
    'BPix_BpI_SEC3_LYR1_LDR4F_MOD2_ROC3',
    'BPix_BmO_SEC8_LYR1_LDR9F_MOD2_ROC8',
    'BPix_BmI_SEC8_LYR1_LDR9F_MOD2_ROC4',
    'BPix_BpI_SEC8_LYR1_LDR9F_MOD1_ROC6',
    'BPix_BmI_SEC1_LYR1_LDR1H_MOD2_ROC10',
    'BPix_BmI_SEC1_LYR1_LDR2F_MOD2_ROC2',
    'BPix_BmI_SEC7_LYR1_LDR8F_MOD2_ROC7',
    'BPix_BmI_SEC1_LYR1_LDR2F_MOD2_ROC1',
    'BPix_BpO_SEC4_LYR1_LDR5F_MOD3_ROC9',
    'BPix_BpI_SEC7_LYR1_LDR8F_MOD4_ROC5',
    'BPix_BpO_SEC8_LYR1_LDR9F_MOD2_ROC14',
    'BPix_BpI_SEC1_LYR1_LDR2F_MOD1_ROC0',
    'BPix_BpI_SEC3_LYR1_LDR4F_MOD2_ROC14',
    'BPix_BpI_SEC1_LYR1_LDR2F_MOD1_ROC6',
    'BPix_BmI_SEC4_LYR1_LDR5F_MOD2_ROC6',
    'BPix_BpO_SEC1_LYR1_LDR2F_MOD2_ROC13',
    'BPix_BpO_SEC8_LYR1_LDR9F_MOD1_ROC4',
    'BPix_BpO_SEC8_LYR1_LDR9F_MOD1_ROC1',
    'BPix_BmI_SEC8_LYR1_LDR9F_MOD3_ROC0',
    'BPix_BmI_SEC3_LYR1_LDR4F_MOD2_ROC15',
    'BPix_BmO_SEC2_LYR1_LDR3F_MOD2_ROC8',
    'BPix_BmO_SEC8_LYR1_LDR9F_MOD1_ROC13',
    'BPix_BmI_SEC1_LYR1_LDR2F_MOD1_ROC2',
    'BPix_BmI_SEC2_LYR1_LDR3F_MOD2_ROC3',
    'BPix_BpI_SEC2_LYR1_LDR3F_MOD2_ROC13',
    'BPix_BmO_SEC8_LYR1_LDR9F_MOD3_ROC4',
    'BPix_BpI_SEC2_LYR1_LDR3F_MOD1_ROC8',
    'BPix_BpI_SEC2_LYR1_LDR3F_MOD2_ROC14',
    'BPix_BmI_SEC4_LYR1_LDR5F_MOD2_ROC10',
    'BPix_BmO_SEC5_LYR1_LDR6F_MOD1_ROC0',
    'BPix_BpI_SEC7_LYR1_LDR8F_MOD3_ROC9',
    'BPix_BmI_SEC8_LYR1_LDR9F_MOD4_ROC15',
    'BPix_BmI_SEC3_LYR1_LDR4F_MOD2_ROC1',
    'BPix_BmO_SEC7_LYR1_LDR8F_MOD4_ROC7',
    'BPix_BmI_SEC8_LYR1_LDR9F_MOD4_ROC14',
    'BPix_BpI_SEC7_LYR1_LDR8F_MOD1_ROC10',
    'BPix_BmO_SEC3_LYR1_LDR4F_MOD1_ROC1',
    'BPix_BpI_SEC1_LYR1_LDR1H_MOD1_ROC2',
    'BPix_BmI_SEC5_LYR1_LDR6F_MOD1_ROC2',
    'BPix_BmO_SEC1_LYR1_LDR2F_MOD2_ROC7',
    'BPix_BpI_SEC7_LYR1_LDR8F_MOD2_ROC4',
]

xx = []
yy = []

h1 = ROOT.TH2F('low_threshold_roc', 'low_threshold_roc', 72, -4.5, 4.5, 42, -10.5, 10.5)


for danny in danek:
    infos = danny.split('_')
    if infos[3] != 'LYR1':
       continue
    ladder = 1 * (('I' in infos[1]) - 1 * ('O' in infos[1])) * int(infos[4].replace('LDR','').replace('H','').replace('F',''))
    module = 1 * (('p' in infos[1]) - 1 * ('m' in infos[1])) * int(infos[5].replace('MOD',''))
    roc = int(infos[6].replace('ROC',''))

    x = binx(module, roc)
    y = biny(ladder, roc)
    
    print 'danek %s\tmodule %d\tladder %d\troc %d\tx %d\ty %d' %(danny, module, ladder, roc, x, y)

    h1.SetBinContent(x, y, 10.)


h1.Draw('colz')
h1.GetXaxis().SetTitle('Module')
h1.GetYaxis().SetTitle('Ladder')

ROOT.gPad.Update()
# ROOT.gPad.SaveAs('danek.pdf')
ROOT.gPad.SaveAs('totune.pdf')


f1 = ROOT.TFile.Open('/Users/riccardomanzoni/Downloads/DQM_V0008_R000285090__StreamExpressPA__PARun2016B-Express-v1__DQMIO.root', 'r')
f1.cd()
occupancy = f1.Get('DQMData/Run 285090/Pixel/Run summary/Clusters/OnTrack/pix_bar Occ_roc_ontracksiPixelDigis_layer_1')

occupancy.Draw('colz')
ROOT.gPad.Update()
ROOT.gPad.SaveAs('ric.pdf')


