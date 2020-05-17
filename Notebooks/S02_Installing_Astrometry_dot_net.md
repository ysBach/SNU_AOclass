# Using Docker (Recommended)

0. Download *Index files* (shell script [here](https://github.com/dam90/astrometry/blob/master/index/download_index_files.sh))

1. [Install Docker Desktop](https://www.docker.com/get-started) and open (run) Docker.

2. Download the astrometry docker image

   ``$ docker pull dm90/astrometry`` (~ 1.33 GB)

3. Run:

   * ``$ docker run --name nova --restart unless-stopped -v <path/to/index/files>:/usr/local/astrometry/data -v <path/to/FITS/files>:/Downloads -p 8000:8000 dm90/astrometry``
   * You have to share the files between the Docker container and host computer, so you need to specify the path to index files and FITS files manually.
   * Example: ``docker run --name nova --restart unless-stopped -v ~/Downloads/astrometry.net/data:/usr/local/astrometry/data -v ~/Downloads:/Downloads -p 8000:8000 dm90/astrometry``

4. Docker → Dashboard → (you can see a new container "nova") → click CLI (Command-line interface) to open the terminal → use ``solve-field`` as you know.

   * If you do ``$ cd Downloads``, the folder shared above will be accessed. Once you modify files here, those in host will be modified, too.

* **TIP**: You can improve the performance by changing Docker → Settings → Resources (CPU, Memory, ...).

* **NOTE**: I have used Docker for only 1-day as of the time I am writing this. There may be better ways, but this is the best I can do.

* Tested on MBP 2018 15" macOS 10.14.6. The disk space used by Docker and image files (except Index files) is ~ 2 GB.



# Naive Installation

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

