## Observatory computer screenshot

* http://147.46.40.80:81/screenshot.png
* Every 3 minutes, the screenshot of the observatory Windows computer (which the JTCS will be running) is uploaded to here.

## Data server (NAS)

* https://147.46.40.80:5003
* All the data and screenshots are archived in this server.
* ID = tripol PW = (same as astro wifi)

## TRIPOL computer

* The Ubuntu computer in the observatory room.
* PW = tripol002

## Manual

* See the attached file. (Or contact TA: dbstn95@gmail.com)
* Chapter 3 and 4 will be important.
  * ``start_ccd``, ``set_temp``, ``print_temp``, ``TL``, ``Lo``, etc
* At the last page, the spec of the CCD is given. But this is **DIFFERENT** one from our TRIPOL! Do not use this information...



## SDSS Prime Standard Stars

The SDSS u'g'r'i'z' standard stars can be found at http://www-star.fnal.gov/ugriz/tab08.dat

For all the information for the standard stars (SDSS u'g'r'i'z'), see http://www-star.fnal.gov/

You may use the following code to make a single csv file of all the list of the "Extended Standard Stars" (after extracting the tar ball file) from the above link.

Attached, please find the SDSS u'g'r'i'z' standard star paper (Smith et al. 2002, AJ, 123, 2121).

```python
from astropy.table import Table, vstack, hstack
from pathlib import Path

directory = "usno40stds.clean.v3"
flist = list(Path(directory).glob("*"))

# http://www-star.fnal.gov/NorthEqExtension_ugriz/Data/README.txt
colnames = ["StarName", "RAJ2000", "DEJ2000", 
            "u'", "sig_u'", "n_u'",
            "g'", "sig_g'", "n_g'",
            "r'", "sig_r'", "n_r'",
            "i'", "sig_i'", "n_i'",
            "z'", "sig_z'", "n_z'"]

colinfo = ["Column 1:  star name",
           "Column 2:  RA(2000) in degrees",
           "Column 3:  DEC(2000) in degrees",
           "Column 4:  calibrated u' mag",
           "Column 5:  estimated rms error in u' mag",
           "Column 6:  number of observations that when into the calibrated u' mag",
           "Column 7:  calibrated g' mag",
           "Column 8:  estimated rms error in g' mag",
           "Column 9:  number of observations that when into the calibrated g' mag",
           "Column 10: calibrated r' mag",
           "Column 11: estimated rms error in r' mag",
           "Column 12: number of observations that when into the calibrated r' mag",
           "Column 13: calibrated i' mag",
           "Column 14: estimated rms error in i' mag",
           "Column 15: number of observations that when into the calibrated i' mag",
           "Column 16: calibrated z' mag",
           "Column 17: estimated rms error in z' mag",
           "Column 18: number of observations that when into the calibrated z' mag"]

alldata = []

for fname in flist:    
    data = Table.read(fname, format='ascii', data_start=1)  
    star = Table(data=[[fname.name.split('.')[0]] * len(data)])
    stacked = hstack([star, data])    
    alldata.append(stacked)
    
allstack = vstack(alldata)

for i, c in enumerate(colnames):
    allstack[f"col{i+1}"].description = colinfo[i]
    allstack[f"col{i+1}"].name = c

allstack.meta = {}
#allstack.write("extended.ecsv", delimiter=',', format="ascii.ecsv")
allstack.write("extended.csv", delimiter=',', format="ascii.csv")
    
```

