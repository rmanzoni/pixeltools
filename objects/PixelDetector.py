#!/usr/bin/python

import sys
sys.path.append('..')
import pickle
import re
from collections import OrderedDict
from objects.ROC import ROC

class PixelDetector():
    '''
    WRITE THE DOCS!
    '''
 
    def __init__(self, 
                 modules_barrel='../data/pixel_modules_bpix.txt',
                 modules_forward='../data/pixel_modules_fpix.txt',
                 coordinates='../data/pixel_coordinates.txt'):
        '''
        WRITE THE DOCS!
        '''    
        self._init_bpix(modules_barrel)
        self._init_fpix(modules_forward)

        coord = open(coordinates, 'r')
        
        for line in coord:
            if line.split()[0] == '#':
                continue
            
            infos = line.split()
            
            name = infos[1]
            
            x, y, z = infos[4].split('/')
            cmscoords = infos[7].split('/')
            
            rocs = [pix for pix in self.BPix + self.FPix if name in pix.name]
            
            for roc in rocs:
                roc.setcoordinates(x, y, z)
        
        self.rocs = self.BPix + self.FPix
        
    def _init_bpix(self, modules_barrel):
        '''
        '''
        bpix = []
        
        modules_bpix = open(modules_barrel, 'r')
        
        for line in modules_bpix:
            if line.split()[0] == '#':
                continue
            infos = line.split()
            
            pixel = ROC(
                name        = infos[0],
                FEC         = infos[1] + ' ' + infos[2],
                mfec        = infos[3],
                mfecchannel = infos[4],
                hubaddress  = infos[5],
                portadd     = infos[6],
                rocid       = infos[7],
                FED         = infos[8],
                channel     = infos[9],
                roc         = infos[10],
                sector      = int(re.findall('SEC(\d+)', infos[0])[0]),
                layer       = int(re.findall('LYR(\d+)', infos[0])[0]),
                half        = infos[0].split('_')[4][-1],
                ladder      = (('I' in infos[0].split('_')[1]) - ('O' in infos[0].split('_')[1])) * int(re.findall('LDR(\d+)', infos[0])[0]),
                module      = (('p' in infos[0].split('_')[1]) - ('m' in infos[0].split('_')[1])) * int(re.findall('MOD(\d+)', infos[0])[0]),
            )
            
            bpix.append(pixel)
        
        modules_bpix.close()
        
        self.BPix = bpix

    def _init_fpix(self, modules_forward):
        '''
        plus minus to be checked!
        '''
        fpix = []
        
        modules_fpix = open(modules_forward, 'r')
        
        for line in modules_fpix:
            if line.split()[0] == '#':
                continue
            infos = line.split()
            
            # FPix_BpO_D1_BLD10_PNL1_PLQ4
            
            pixel = ROC(
                name        = infos[0],
                FEC         = infos[1],
                mfec        = infos[2],
                mfecchannel = infos[3],
                hubaddress  = infos[4],
                portadd     = infos[5],
                rocid       = infos[6],
                FED         = infos[7],
                channel     = infos[8],
                roc         = infos[9],
                disk        = int(re.findall('_D(\d+)_', infos[0])[0]),
                blade       = int(re.findall('BLD(\d+)', infos[0])[0]),
                pannel      = int(re.findall('PNL(\d+)', infos[0])[0]),
                plaq        = int(re.findall('PLQ(\d+)', infos[0])[0]),
            )
            
            fpix.append(pixel)
        
        modules_fpix.close()
        
        self.FPix = fpix

    def get(self, **kwargs):
        '''
        Get a list of portions of ROC.
        Apply selection criteria as named arguments passed to this method get
        Available selection criteria:
            - name        : string
            - FEC         : string 
            - mfec        : int
            - mfecchannel : int
            - hubaddress  : int
            - portadd     : int
            - rocid       : int
            - FED         : int
            - channel     : int
            - roc         : int
            - r           : tuple (center value, tolerance)
            - phi         : tuple (center value, tolerance)
            - z           : tuple (center value, tolerance)
            - sector      : int
            - layer       : int
            - half        : string, whether 'H' of 'F'
            - ladder      : int
            - module      : int
            - side        : int
            - disk        : int
            - blade       : int
            - pannel      : int
            - plaq        : int

        Each requirement will be applied a logical AND.
        
        For example, if you want to select all ROCs in layer-1, sector 3, module 4:
        pixels.get(module=4, sector=3, layer=1)
        '''
        selected_rocs = self.rocs
        for key in kwargs.keys():
            if key in ['r', 'phi', 'z']:
                selected_rocs = [roc for roc in selected_rocs if (getattr(roc, key) > (kwargs[key][0]-kwargs[key][1]) and getattr(roc, key) < (kwargs[key][0]+kwargs[key][1]))]        
            else:
                selected_rocs = [roc for roc in selected_rocs if getattr(roc, key) == kwargs[key]]        
        return selected_rocs
        
    def dump(self, filename='../data/pixels.pkl'):
        '''
        Serialise object
        '''
        print 'Saving current Pixel Detector into %s' %filename
        pixel_file = open(filename, 'w+')
        pickle.dump(self, pixel_file)
        pixel_file.close()





 
if __name__ == '__main__':
    pixels = PixelDetector()
    
    print '\nprinting ROCs belonging to layer-1, module 4 and sector 3:\n'
    selected_rocs = pixels.get(module=4, sector=3, layer=1)
    for i in selected_rocs: 
        print i.name
    

