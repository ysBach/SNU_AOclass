Download index files of 2MASS (for small field of view)

```
$ wget -r --no-parent -A '*' http://data.astrometry.net/4200
```

> You may download Tycho index (wide field)
>
> ```
> $ wget -r --no-parent -A '*' http://data.astrometry.net/4100
> ```
>
> and GAIA DR2:
>
> ```
> $ wget -r --no-parent -A '*' http://data.astrometry.net/5000
> ```
>
>

Install dependencies before goring further:

```
sudo apt-get install libcairo2-dev libnetpbm10-dev netpbm libpng-dev libjpeg-dev python-numpy python-pyfits python-dev zlib1g-dev libbz2-dev swig libcfitsio-dev
sudo apt-get install astrometry.net
```

> ``libpng12-dev`` ---> ``libpng-dev``??
>
> Official manual uses ``cfitsio-dev`` instead of ``libcfitsio-dev``, which does not work and gives much confusion to users. (-_-)

Then

```
sudo vi /etc/astrometry.cfg
```



- Uncomment `inparallel` in `~/astrometry.net/etc/astrometry.cfg` (or `/etc/astrometry.cfg`)
  - I was helped by this [Link](https://www.scivision.co/setting-up-astrometry-net-program/)
- Change ``add_path blahblah`` to, e.g., ``add_path /home/ysbach/Downloads/data``

```
mv 20181013/raw/0419_R_SA95218_60.0.fits 20181013/raw/input.fits
solve-field 20181013/raw/input.fits -N 20181013/raw/0419_R_SA95218_60.0.fits --sigma 5 --downsample 4 --ra 58.71 --dec 0.17 --radius 0.2 -u app -L 0.30 -U 0.33 --no-plot --overwrite
rm *.axy *.wcs *.corr *.match
rm infpath
```





--------

Other way



Download astrometry code:

```
cd ~
git clone https://github.com/dstndstn/astrometry.net.git
```

> Official manual gives strange broken link (``wget http://astrometry.net/downloads/astrometry.net-latest.tar.bz2``). As of 2018 November, and when I tried the same thing months ago, this link never worked. 
>
> All the HomeBrew codes they provide for Mac also never works. I think the best is not to believe the official manual -_-...





 cd to the downloaded directory  and

```
cd ~/astrometry.net
make
make extra
sudo make install
```

>Even if ``swig`` error happens, the ``sudo make install`` says 
>
>> ``Errors in the previous make command are not fatal -- we try to build and install some optional code.``
>
>If error occurs, the simplest way is to
>
>```
>sudo apt-get autoremove gcc
>sudo apt-get install gcc
>```



I was helped by this [Link](https://www.scivision.co/setting-up-astrometry-net-program/):

* Uncomment `inparallel` in `~/astrometry.net/etc/astrometry.cfg` (or `/etc/astrometry.cfg`)



Copy (I don't know why export PATH (``export PATH="$PATH:$HOME/astrometry.net/bin"``) does not work on my computer)

```
sudo cp ~/astrometry.net/bin/* /usr/local/bin
sudo cp ~/astrometry.net/etc/* /usr/local/etc
```

solve-field 0008_R_155140_60.0.fits --sigma 5 --downsample 4 --no-plots --overwrite

