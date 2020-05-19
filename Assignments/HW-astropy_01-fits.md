## Goals

* Basics of ``astropy.io.fits`` and ``astropy.nddata.Cutout2D``
* Understand how to see header and data (HDU and HDUList)
* Understand how to cutout a portion of an image with WCS information, and save as a new FITS.





## 1. No-Code Problems

Answer the following [2 points each]

1. Search for the official documentation of ``astropy.io.fits``. What is the URL to this doc?
2. Read the doc. You don't have to read all but just skim through it and grasp an idea how ``astropy.io.fits`` is used, how the header is accessed, etc. Click many links in the doc, and familiarize yourself to it.  (I did|I didn't)

3. Go to a doc about ["Cutout images"](https://docs.astropy.org/en/stable/nddata/utils.html#cutout-images). You may have to have basic understanding of WCS as well as python. Find references by yourself. Also for WCS, you may have to learn ``astropy.wcs`` by clicking many links provided there. Familiarize yourself with the idea of ``Cutout2D`` and its usage. (I did|I didn't)





## 2. Coding Problems

### Instructions

* Prepare the FITS file ``SNUO_STX16803-kw4-4-4-20190602-135247-R-60.0_bdfw.fits`` from our Tutorial Data link (see README of our lecture note repo). As indicated in astronomy.net homework, this file has intentionally broken WCS information, but it does not matter for the problems below.
* Please use python 3.6+ (Never use python 2). 
* For other packages: Although I didn't run all the tests, likely there will be no problem if you use decently recent versions of any packages used in the homework (any version released after 2017).



Please run the following code before you start (**MODIFY APPROPRIATELY**):

```python
# If you are not using Jupyter, uncomment the "%" lines below
%config InlineBackend.figure_format = 'retina'
%matplotlib notebook

from pathlib import Path
from astropy.io import fits
from astropy.nddata import Cutout2D
from astropy.wcs import WCS

from matplotlib import pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.axes_grid1 import ImageGrid

# Modify below to the relative path to the directory where you saved the FITS file.
DATADIR = Path("../../Tutorial_Data/")

# We need to do it in a separate cell. See:
# https://github.com/jupyter/notebook/issues/3385
plt.style.use('default')
rcParams.update({'font.size':12})

allfits = list(DATADIR.glob("SNUO*_bdfw.fits"))

imgrid_kw = dict(
    nrows_ncols=(1, 1),
    axes_pad=(0.45, 0.15),
    label_mode="1",
    share_all=True,
    cbar_location="right",
    cbar_mode="each",
    cbar_size="7%",
    cbar_pad="2%"
)
```



Answer the following questions. Provide codes. Also provide results if something is printed out or plotted from the code. [2 pts each, unless specified]

1. Set ``fpath`` as the path to the file.
   
* Hint: ``fpath = allfits[<an int>]``
  
2. Set ``hdul`` as an HDUList object of that file.
   
   * Hint: ``hdul = fits.open(?)``
3. Print out the information of the ``hdul``.
   
   * Hint: ``hdul.info()``
4. How many header keywords are there in the 0-th extension of ``hdul``?
5. Print out the header of the 0th HDU.
   
* Hint: ``hdul[0].?`` or ``hdul["PRIMARY"].?``
  
6. From the header, what is the header keyword for [1 point each]:

   1. the start of the exposure
   2. the filter used
   3. the object observed
   4. the longitude of the observatory

   * Hint: No code is needed. Also, you may ignore all the ``COMMENT`` and ``HISTORY`` in headers.

7. Set ``hdr`` as the header of the primary header. What is the pixel scale (arcsecond per pixel)? Provide a code and result to calculate it from ``hdr``.
   * Hint: ``hdr = hdul[0].?``
   * Find the focal length of the telescope and pixel size from ``hdr``.
8. From ``PROCESS`` and the ``COMMENT`` after it, what "process" has been done to this file?

9. Display the data. You may use the following code (Tune ``?`` values to make y-axis value increase upwards). I intentionally used ``ImageGrid``, which is different from lecture notes so that you can learn different APIs.

   ```python
   vv = dict(vmin=1900, vmax=2000)
   
   fig = plt.figure()
   grid = ImageGrid(fig, 111, **imgrid_kw)
   for ax, cax in zip(grid, grid.cbar_axes):
       im = ax.imshow(hdul[0].data, **vv, origin=?)
       cb = cax.colorbar(im)
   
   plt.tight_layout()
   plt.show()
   ```

10. Cut a rectangular region centered at ``(555, 505)`` and size of ``(70, 70)`` in x, y directions, respectively.
    * Hint: ``cut = Cutout2D(hdul[0].data, position=(?, ?), size=(?, ?), wcs=WCS(hdul[0].header))``
    * **WARNING**: Python indexing is ``(y, x)``, **not** ``(x, y)``. Which one should we use, ``position = (505, 555)`` or ``(555, 505)``? Find and read the documentation for ``Cutout2D`` and write a proper answer. If you're wrong here, all of your answers below will be wrong.
    * ``wcs`` keyword is used to propagate WCS information ([link](https://docs.astropy.org/en/stable/nddata/utils.html#saving-a-2d-cutout-to-a-fits-file-with-an-updated-wcs))

11. Overplot where the rectangular cut is made. You may use the following code. Modify as you wish. Fill in the ``?`` parts by searching appropriate docs.

    ```python
    fig = plt.figure()
    grid = ImageGrid(fig, 111, **imgrid_kw)
    for ax, cax in zip(grid, grid.cbar_axes):
        im = ax.imshow(hdul[0].data, **vv, origin='lower')
        cb = cax.colorbar(im)
    
    
    cut.plot_on_original(ax, color='r', fill=True, alpha=0.3)
    # https://docs.astropy.org/en/stable/api/astropy.nddata.utils.Cutout2D.html#astropy.nddata.utils.Cutout2D.plot_on_original
    
    ### inset_axes tutorial: https://matplotlib.org/3.2.1/gallery/subplots_axes_and_figures/zoom_inset_axes.html
    # inset axes....
    axins = ax.inset_axes([0.55, 0.55, 0.4, 0.4])
    axins.imshow(hdul[0].data, extent=(*ax.get_xlim(), *ax.get_ylim()), **vv, origin="lower")
    
    # sub region of the original image
    x1, x2 = cut.bbox_original[?] 
    y1, y2 = cut.bbox_original[?]
    
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)
    axins.set_xticklabels('')
    axins.set_yticklabels('')
    ax.indicate_inset_zoom(axins, edgecolor='r')
    # https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.axes.Axes.indicate_inset.html#matplotlib.axes.Axes.indicate_inset
    
    plt.tight_layout()
    plt.show()
    ```

12. Save the cutout region as a new FITS file.

    ```python
    new_hdu = fits.PrimaryHDU(data=cut.data)    # set data
    new_hdu.header.update(cut.wcs.to_header())  # implement WCS information
    
    new_hdu.writeto("test.fits", overwrite=True, output_verify='fix')
    ```

13. Test whether WCS is correctly implemented.

    ```python
    hdu_orig = hdul[0]
    hdu_crop = fits.open("test.fits")[0]
    wcs_orig = WCS(hdu_orig)
    wcs_crop = WCS(hdu_crop)
    
    # Due to the API, we need 2-D
    pos_orig = np.atleast_2d(
        cut.to_original_position(cut.center_cutout)  # Center of the Cutout2D in the original (x, y)
    )
    pos_crop = np.atleast_2d(
         cut.center_cutout
    )
    
    radec_orig_wcs = wcs_orig.wcs_pix2world(pos_orig, 0)
    radec_crop_wcs = wcs_crop.wcs_pix2world(pos_crop, 0)
    radec_orig_all = wcs_orig.all_pix2world(pos_orig, 0)
    radec_crop_all = wcs_crop.all_pix2world(pos_crop, 0)
    
    print("Difference [ΔRA, ΔDEC] (arcsec) =", 3600*(radec_orig_wcs - radec_crop_wcs))
    print("Difference [ΔRA, ΔDEC] (arcsec) =", 3600*(radec_orig_all - radec_crop_all))
    # Difference [ΔRA, ΔDEC] (arcsec) = [[0. 0.]]
    # Difference [ΔRA, ΔDEC] (arcsec) = [[-0.47574813 -0.16822854]]
    ```

14. Delete the ``test.fits`` file.



### A note on WCS

In astropy, there are two ways to convert pixel (X/Y) ⟷ world coordinate (RA/DEC) described in [here](https://docs.astropy.org/en/stable/wcs/index.html#getting-started). Simply put:

1. ``wcs``: Only simple calculation is done
2. ``all``: Calculates all detailed calculations.

Therefore, calculations using ``all`` (``all_pix2world``) must be more correct than ``wcs`` (``wcs_pix2world``). From the code above, however, it is the opposite. What's wrong here?

First, the fact that our FITS file has an intentionally broken WCS information **does not** matter, because it only scales ``PC`` parameters in the WCS header: If you try with updated WCS, it still gives discrepancy of ~ 0.1 arcsec order in both RA/DEC (``Difference [ΔRA, ΔDEC] (arcsec) = [[0.24009913 0.02912163]]``). It seems like, when using ``Cutout2D``, **not all of the WCS information is transferred correctly** (not clearly stated but you can get some hint from the doc [here](https://docs.astropy.org/en/stable/api/astropy.nddata.utils.Cutout2D.html)). Thus, "details" of the original WCS is not propagated to cutout, and this is the reason why the ``wcs_pix2world`` gives identical result, while ``all_pix2world`` gives slightly different result. If ``Cutout2D`` correctly transfers all WCS information, then we would see the difference = 0 for ``all_pix2world``, and non-zero difference in ``wcs_pix2world``. 

