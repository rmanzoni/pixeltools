#!/usr/bin/python

import sys
sys.path.append('..')

class ROC():
    '''
    '''
    def __init__(self, 
                 name        = 'dummy', 
                 FEC         = 'dummy', 
                 mfec        = -999, 
                 mfecchannel = -999, 
                 hubaddress  = -999, 
                 portadd     = -999, 
                 rocid       = -999, 
                 FED         = -999, 
                 channel     = -999, 
                 roc         = -999,
                 r           = -999.,
                 phi         = -999.,
                 z           = -999.,
                 sector      = -999,
                 layer       = -999,
                 half        = 'dummy',
                 ladder      = -999,
                 module      = -999,
                 side        = -999,
                 disk        = -999,
                 blade       = -999,
                 pannel      = -999,
                 plaq        = -999):
        self.name        = name         
        self.FEC         = FEC
        self.mfec        = int  (mfec       )
        self.mfecchannel = int  (mfecchannel)
        self.hubaddress  = int  (hubaddress )
        self.portadd     = int  (portadd    )
        self.rocid       = int  (rocid      )
        self.FED         = int  (FED        )
        self.channel     = int  (channel    )
        self.roc         = int  (roc        )
        self.r           = float(r          )
        self.phi         = float(phi        )
        self.z           = float(z          )
        self.sector      = int  (sector     )
        self.layer       = int  (layer      )
        self.half        = 'dummy'
        self.ladder      = int  (ladder     )
        self.module      = int  (module     )
        self.side        = int  (side       )
        self.disk        = int  (disk       )
        self.blade       = int  (blade      )
        self.pannel      = int  (pannel     )
        self.plaq        = int  (plaq       )

    def set(name, FEC, mfec, mfecchannel, hubaddress, 
            portadd, rocid, FED, channel, roc):
        self.name        = name       
        self.FEC         = FEC
        self.mfec        = int(mfec       )
        self.mfecchannel = int(mfecchannel)
        self.hubaddress  = int(hubaddress )
        self.portadd     = int(portadd    )
        self.rocid       = int(rocid      )
        self.FED         = int(FED        )
        self.channel     = int(channel    )
        self.roc         = int(roc        )
    
    def setcoordinates(self, r, phi, z):
        self.r   = float(r)
        self.phi = float(phi)
        self.z   = float(z)          

    # this cmssw needs to be understood...
    
    # def _setcmslabelBPIX(self, layer, ladder, module):
    #     self.layer  = int(layer)
    #     self.ladder = int(ladder)
    #     self.module = int(module)          

    # def _setcmslabelFPIX(self, side, disk, blade, pannel, plaq):
    #     self.side   = int(side)
    #     self.disk   = int(disk)
    #     self.blade  = int(blade)          
    #     self.pannel = int(pannel)          
    #     self.plaq   = int(plaq)          

    # def setcmslabel(self, coords):
    #     if len(coords) == 3:
    #         self._setcmslabelBPIX(coords[0], coords[1], coords[2])
    #     if len(coords) == 5:
    #         self._setcmslabelFPIX(coords[0], coords[1], coords[2], coords[3], coords[4])

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
            '\troc          {roc}\n'\
            '\tr            {r}\n'\
            '\tphi          {phi}\n'\
            '\tz            {z}\n'\
            '\tsector       {sector}\n'\
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
                 roc         = self.roc        ,
                 r           = self.r          ,
                 phi         = self.phi        ,
                 z           = self.z          ,
                 sector      = self.sector     ,
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
    pass


