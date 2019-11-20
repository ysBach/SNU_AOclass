# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
import glob
from astropy.io import fits
from astropy.table import Table, Column
import numpy as np


from AO2tutorial.util import preproc, filemgmt
from importlib import reload
reload(preproc)
reload(filemgmt)

#%%
allfits = glob.glob(os.path.join('data', '*.fits'), recursive=True)

# save one example header file
os.chmod(allfits[0], 777)
ex_hdr = fits.getheader(allfits[0])
ex_hdr.totextfile('example_header.txt', overwrite=True)

# Which cards to save? What are their corresponding data types?
cards = ['DATE-OBS', 'NAXIS1', 'NAXIS2',
         'XBINNING', 'YBINNING', 'EXPTIME', 'AIRMASS',
         'OBJECT', 'GRATING', 'SLIT-WID', 'ORDERCUT']

#dtypes = ['U24', int, int,
#          int, int, float, float,
#          'U16', int, float, 'U16']
dtypes = ['U30'] * len(cards)

# Initialize the table and fill it, save it.
summarytab = Table(names=cards, dtype=dtypes)
fnames = []

for fitsfile in allfits:
    os.chmod(fitsfile, 777)
    fnames.append(fitsfile)    
    hdr = fits.getheader(fitsfile)
    row = []
    for card in cards:
        row.append(hdr[card])
    summarytab.add_row(row)

fnames = Column(data=fnames, name='file')
summarytab.add_column(fnames, index=0)
summarytab.sort('file')
summarytab.write('summary.csv', format='ascii.csv', overwrite=True)

'''
# You may want to use
from ccdproc import ImageFileCollection
# set the keywords we are interested in.
# Also, you don't have to use upper case but you **MUST be consistent** in the
# later codes.
cards = ['DATE-OBS', 'NAXIS1', 'NAXIS2',
         'XBINNING', 'YBINNING', 'EXPTIME', 'AIRMASS',
         'OBJECT', 'COMPLAMP', 'FLATLAMP', 'LAMP_SW']

IC = ImageFileCollection(os.getcwd(),            # in current working directory
#                         glob_include='FCSA*',   # files starts with 'FCSA'
                         keywords=cards)         # only the predefined keys
# the ``glob_include`` will be available from ``ccdproc`` version 1.3.
# TODO: Change this part after ccdproc 1.3 release

# Make a summary file.
fits_tab = IC.summary
fits_tab.write('summary.csv', format='ascii.csv', overwrite=True)
'''
#EXPTIME =                   5. / duration of exposure in seconds                
#XBINNING=                    1 / binning factor used on X axis                  
#YBINNING=                    1 / binning factor used on Y axis                  
#DATE-OBS= '2017-02-13T21:59:43' / date of observation (UTC)                     
#OBJECT  = 'DARK    '           / Target description                             
#AIRMASS =                1.000 / Typical air mass during exposure               
#GRATING =                  150 / gratOBJ_GRATING = 150 # lines per mming(l/mm)                                  
#GRT_ANG =     29.7995882352941 / Grating angle(deg)                             
#ORDERCUT= 'WG320   '           / Order cut filter Name                          
#SLIT-WID=                  1.6 / Slit width(arcsec)                             
#SLIT-LEN=                  300 / Slit length(arcsec)                            
#COMPLAMP= '        '           / Comparison lamp(ON/OFF)                        
#FLATLAMP= 'OFF     '           / Flat lamp(ON/OFF)                              
#LAMP_SW = 'INSTFLAT'           / Selected lamp(COMPARISON/INSTFLAT)             

#%%
OBJ_SLITWID = 1.6 # arcsecond
OBJ_ORDERCUT= 'WG320' # Order cut filter name
OBJ_GRATING = 150 # lines per mm

# http://www.nhao.jp/~malls/malls_wiki/index.php?MALLS
# 150 lines/mm (3700A--9500A, wavelengh range = 5700A), R~600 (550nm, 1.2")

biastab = summarytab[((summarytab['OBJECT'] == 'DARK')
                     & (summarytab['EXPTIME'] == 0.5 )) ]

darktab = summarytab[((summarytab['OBJECT'] == 'DARK')
                     & (summarytab['EXPTIME'] > 100 )) ]

flattab = summarytab[((summarytab['OBJECT'] == 'flat')
                     & (summarytab['GRATING'] == OBJ_GRATING)
                     & (summarytab['SLIT-WID'] == OBJ_SLITWID)
                     & (summarytab['ORDERCUT'] == OBJ_ORDERCUT))]

bias_fname = 'bias.fits'
dark_fname = 'dark1s.fits'
flat_fname = 'flat.fits'

if os.path.exists(bias_fname):
    mbias = fits.getdata(bias_fname)
else:
    mbias = preproc.make_master_bias(biastab, sigma=3, iters=5, min_value=0,
                                     output = bias_fname)

if os.path.exists(dark_fname):
    mdark = fits.getdata(dark_fname)    
else:
    mdark = preproc.make_master_dark(darktab, mbias=mbias, sigma=3, iters=5,
                                     min_value=0, 
                                     output = dark_fname)
if os.path.exists(flat_fname):
    mflat = fits.getdata(flat_fname)
else:
    mflat = preproc.make_master_flat(flattab, mbias=mbias, sigma=3, iters=5,
                                     min_value=5000, 
                                     output = flat_fname)

#%%
objtab = summarytab[( ((summarytab['OBJECT'] == '45P')
                       |(summarytab['OBJECT'] == 'HD129184') )
                     & (summarytab['AIRMASS'] < 1.5)) ]
    
comptab = summarytab[( (summarytab['OBJECT'] == 'comparison')
                      & (summarytab['GRATING'] == OBJ_GRATING)
                      &(summarytab['SLIT-WID'] == OBJ_SLITWID)
                      &(summarytab['ORDERCUT'] == OBJ_ORDERCUT)) ]

# Preprocess
GAIN = 2.20 # electrons/ADU 
RONOISE = 12.3 # electrons
# above from http://www.nhao.jp/~malls/malls_wiki/index.php?%BB%C5%CD%CD

# I will trim the data with [350:1250,50:-50], where +- 50 is due to the overscan.
TRIM = [350, 1250, 50, 2098] # y_lower, y_upper, x_lower, x_upper

for fname in objtab['file']:
    outputname = 'pobj_' + os.path.split(fname)[-1]
    preproc.bdfgt_process(fname=fname,
                          mbiasname=bias_fname,
                          mdarkname=dark_fname,
                          mflatname=flat_fname,
                          mdark_seconds=1.0,
                          trim=TRIM,
                          gain=GAIN,
                          exposure_key='EXPTIME',
                          dtype=np.float32,
                          output=outputname)
    
for fname in comptab['file']:
    outputname = 'pcomp_' + os.path.split(fname)[-1]
    preproc.bdfgt_process(fname=fname,
                          mbiasname=bias_fname,
                          mdarkname=dark_fname,
                          mflatname=flat_fname,
                          mdark_seconds=1.0,
                          trim=TRIM,
                          gain=GAIN,
                          exposure_key='EXPTIME',
                          dtype=np.float32,
                          output=outputname)
    
#%%
comp_orig = np.empty((TRIM[1] - TRIM[0], TRIM[3] - TRIM[2], 3), dtype=np.float32)
header0 = fits.getheader(comptab['file'][0])

for i in range(len(comptab['file'])):
    pfname = 'pcomp_' + os.path.split(comptab['file'][i])[-1]
    comp_orig[:, :, i] = fits.getdata(pfname).astype(np.float32)

comp_comb = preproc.clip_median_combine(comp_orig, iters=0)
fits.writeto('pcomp_medcomb.fits', data=comp_comb.data, header=header0, 
             output_verify='fix', overwrite=True)
