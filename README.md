**Install**  
`git clone git@github.com:rmanzoni/pixeltools.git`

**Content**  

* `objects              ` contains PixelDetector.py and ROC.py 
* `data                 ` contains: 
    * `pixel_coordinates.txt ` equal to coordinate map by Danek http://dkotlins.web.cern.ch/dkotlins/CMS/MyDocs/phase0_dets.txt  
    * `pixel_modules_bpix.txt` equal to pixel translation map by Danek http://dkotlins.web.cern.ch/dkotlins/CMS/P5/translation.dat (for BPix) 
    * `pixel_modules_fpix.txt` equal to pixel translation map by Danek http://dkotlins.web.cern.ch/dkotlins/CMS/P5/translation.dat (for FPix) 
* `test                 ` contains (to be revised): 
    * `readPixels.py` produces a dictionary containing one entry per ROC and serialises it into `pixels.pkl`  
    * `pixels.pkl   ` this is persistent and in principle shouldn't change
    * `findPixel.py ` read the collection of Pixel ROC objects and play with it, few examples towards the end of the file

**Warning, very preliminary**


**Offline DQM plots can be downloaded from**  
`https://cmsweb.cern.ch/dqm/offline/data/browse/ROOT/`  


