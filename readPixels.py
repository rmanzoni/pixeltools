import pickle
from collections import OrderedDict

class PixelROC(object):
    '''
    '''
    def __init__(self, name, FEC, mfec, mfecchannel, hubaddress, 
                 portadd, rocid, FED, channel):
        self.name        = name       
        self.FEC         = FEC
        self.mfec        = int(mfec       )
        self.mfecchannel = int(mfecchannel)
        self.hubaddress  = int(hubaddress )
        self.portadd     = int(portadd    )
        self.rocid       = int(rocid      )
        self.FED         = int(FED        )
        self.channel     = int(channel    )
        self.r           = -99.
        self.phi         = -99.
        self.z           = -99.
        self.layer       = -99
        self.ladder      = -99
        self.module      = -99
        self.side        = -99
        self.disk        = -99
        self.blade       = -99
        self.pannel      = -99
        self.plaq        = -99
    
    def setcoordinates(self, r, phi, z):
        self.r   = float(r)
        self.phi = float(phi)
        self.z   = float(z)          

    def _setcmslabelBPIX(self, layer, ladder, module):
        self.layer  = int(layer)
        self.ladder = int(ladder)
        self.module = int(module)          

    def _setcmslabelFPIX(self, side, disk, blade, pannel, plaq):
        self.side   = int(side)
        self.disk   = int(disk)
        self.blade  = int(blade)          
        self.pannel = int(pannel)          
        self.plaq   = int(plaq)          

    def setcmslabel(self, coords):
        if len(coords) == 3:
            self._setcmslabelBPIX(coords[0], coords[1], coords[2])
        if len(coords) == 5:
            self._setcmslabelFPIX(coords[0], coords[1], coords[2], coords[3], coords[4])

    def __str__(self):
        toprint = '{name}\n'\
            '\tFEC          {FEC}\n'\
            '\tmfec         {mfec}\n'\
            '\tmfecchannel  {mfecchannel}\n'\
            '\thubaddress   {hubaddress}\n'\
            '\tportadd      {portadd}\n'\
            '\trocid        {rocid}\n'\
            '\tFED          {FED}\n'\
            '\tchannel      {channel}\n'\
            '\tr            {r}\n'\
            '\tphi          {phi}\n'\
            '\tz            {z}\n'\
            '\tlayer        {layer}\n'\
            '\tladder       {ladder}\n'\
            '\tmodule       {module}\n'\
            '\tside         {side}\n'\
            '\tdisk         {disk}\n'\
            '\tblade        {blade}\n'\
            '\tpannel       {pannel}\n'\
            '\tplaq         {plaq}\n'.format(
                 name        = self.name       ,
                 FEC         = self.FEC        ,
                 mfec        = self.mfec       ,
                 mfecchannel = self.mfecchannel,
                 hubaddress  = self.hubaddress ,
                 portadd     = self.portadd    ,
                 rocid       = self.rocid      ,
                 FED         = self.FED        ,
                 channel     = self.channel    ,
                 r           = self.r          ,
                 phi         = self.phi        ,
                 z           = self.z          ,
                 layer       = self.layer      ,
                 ladder      = self.ladder     ,
                 module      = self.module     ,
                 side        = self.side       ,
                 disk        = self.disk       ,
                 blade       = self.blade      ,
                 pannel      = self.pannel     ,
                 plaq        = self.plaq       ,
            )
        return toprint
    


if __name__ == '__main__':

    pixels = OrderedDict()

    modules = open('pixel_modules.txt', 'r')
    
    for line in modules:
        if line.split()[0] == '#':
            continue
        infos = line.split()
        
        if len(infos) == 10:
            pixel = PixelROC(
                name        = infos[0],
                FEC         = infos[1],
                mfec        = infos[2],
                mfecchannel = infos[3],
                hubaddress  = infos[4],
                portadd     = infos[5],
                rocid       = infos[6],
                FED         = infos[7],
                channel     = infos[8],
            )
        elif len(infos) == 11:
            pixel = PixelROC(
                name        = infos[0],
                FEC         = infos[1] + ' ' + infos[2],
                mfec        = infos[3],
                mfecchannel = infos[4],
                hubaddress  = infos[5],
                portadd     = infos[6],
                rocid       = infos[7],
                FED         = infos[8],
                channel     = infos[9],
            )
        
        pixels.update({infos[0]:pixel})
    
    modules.close()

    coordinates = open('pixel_coordinates.txt', 'r')
    for line in coordinates:
        if line.split()[0] == '#':
            continue
        infos = line.split()
        
        name = infos[1]
        
        x, y, z = infos[4].split('/')
        cmscoords = infos[7].split('/')
        
        names = [nn for nn in pixels.keys() if name in nn]
        
        for nn in names:
            pixels[nn].setcoordinates(x, y, z)
            pixels[nn].setcmslabel(cmscoords)

    coordinates.close()

    pixel_file = open('pixels.pkl', 'w+')
    
    pickle.dump(pixels, pixel_file)
    
    pixel_file.close()
    

