**``astrometry.net``과 ``solve-field``**를 도커로 사용하는 간단한 방법에 관한 것이며,혹시 또 도움이 될 **관측연구자**가 계실까 하여 정보를 공유합니다.

어제 처음 시도해본 것이라 최선의 방법인지, 더 좋은 방법이 있는지는 아직 모르지만 연구/교육용 자료에 테스트해본 결과 원래 알고 있던 속도와 정확도로 잘 작동해서 만족했습니다.



### TL;DR (혹은 아래 [사용법](# 사용법) 참고)

1. ``$ docker pull dm90/astrometry``
2. ``$ docker run --name nova --restart unless-stopped -v <path/to/index/files>:/usr/local/astrometry/data -v <path/to/FITS/files>:/Downloads -p 8000:8000 dm90/astrometry``
3. Go to Docker Dashboard, click CLI, use ``solve-field`` as you wish!
4. *Write papers*



-----

-----

-----

**목차**

* 문제 배경설명
* 해결책
  * 사용법 요약
  * 테스트 (benchmark)
* 향후 사용방안



## 문제 배경설명

``astrometry.net``에서 제공하는 ``solve-field``는 WCS가 없는 이미지에 WCS를 입히기 위해 대단히 중요한 역할을 하고 있습니다. 그러나 이를 설치하는 건 아주 고된 일인데, 설치 자체가 복잡할 뿐더러 이 복잡한 과정이 모든 컴퓨터에서 동일하지 않기 때문입니다. 심지어 공식 메뉴얼의 설치 스크립트도 그대로 돌리면 설치되지 않습니다.

2018년 이후 macOS를 사용하는 경우 설치가 더 복잡해져서 한때 페이스북 천문학자 그룹에서도 몇몇 연구자들이 수 일에 걸쳐 설치법을 찾아냈으나, 너무나 수고로운 일이었습니다 (찾아낸 방법도 복잡하기 그지없습니다). 윈도즈의 경우 2020년 5월 WSL 2의 도입으로 WSL 1에 비해 혁신적인 효율로 리눅스계열 터미널 사용이 가능한 것으로 알지만 이 역시 결국 해당 가상 OS에 solve-field가 설치되도록 많은 설치과정을 거쳐야 합니다. 윈도즈 환경에서 연구업무를 보지 않은지 오래되어 WSL 2를 테스트해보지 못해서 다른 불편함은 잘 알지 못합니다.



## 해결책

이러한 문제 해결을 위해 개발자들은 Docker를 사용하는 것으로 알고 있는데, 찾아보니 약 2년 전 ``astrometry.net`` 웹 및 solve-field를 Docker image로 만들어 공개한 것이 있습니다 ([GitHub](https://github.com/dam90/astrometry)).

저는 지금까지는 mac에 Parallels를 설치하고, 여기에 Ubuntu 18.04를 가상머신으로 올린 뒤 여기에 ``astrometry.net``의 ``solve-field``를 깔아 사용했습니다. 최근 Parallels를 포맷하게 되어 다른 설치법을 알아보다가 이 해결책을 찾았습니다.



### 사용법 

([English here](https://github.com/ysBach/SNU_AOclass/blob/master/Notebooks/S02_Installing_Astrometry_dot_net.md))

0. 이미 있으면 패스하면 되지만, 평소 설치하듯이 약 30GB정도 되는 인덱스파일이 필요합니다 (간단한 shell script는 [여기](https://github.com/dam90/astrometry/blob/master/index/download_index_files.sh))

1. 도커 데스크톱을 [설치합니다](https://www.docker.com/get-started). 그리고 실행합니다.

2. astrometry docker image를 다운받습니다 

   ``$ docker pull dm90/astrometry`` (약 1.33 GB)

3. 도커로 run 합니다:

   * ``$ docker run --name nova --restart unless-stopped -v <path/to/index/files>:/usr/local/astrometry/data -v <path/to/FITS/files>:/Downloads -p 8000:8000 dm90/astrometry``
   * 이때 인덱스파일이 있는 폴더경로와 FITS파일이 있는 폴더경로는 host와 "file sharing"하는 것이기 때문에 직접 입력하셔야 합니다.
   * 예시: ``docker run --name nova --restart unless-stopped -v ~/Downloads/astrometry.net/data:/usr/local/astrometry/data -v ~/Downloads:/Downloads -p 8000:8000 dm90/astrometry``

4. 도커 → Dashboard → "nova" 라는 새 container가 실행중인 걸 보실 수 있습니다 → CLI(Command-line interface)를 클릭하여 터미널을 켜면 → ``solve-field``를 원래 알고계시는 그대로 터미널에서 사용할 수 있습니다. 

   * FITS 파일들은 ``cd Downloads`` 하시면 아까 공유한 폴더가 그대로 뜹니다. 여기서 파일들을 수정하면 원래 host 컴퓨터의 파일도 수정됩니다.

* **TIP**: 도커에서 컨테이너에 할당하는 리소스(cpu나 memory 등)를 조절하여 더 좋은 성능을 끌어낼 수 있습니다.
* **NOTE**: 도커를 처음 제대로 써본지 하루가 되었습니다. 이보다 좋은 방법이 있을 수 있겠지만 아직 잘 모르겠습니다...

* MBP 2018 15" macOS 10.14.6 에서 테스트하였고, 인덱스파일 외에는 도커 및 이미지파일을 포함하여 약 2GB 정도의 공간이 추가로 필요합니다.



### 테스트

2018-10-12 서울대 1-m 망원경으로 관측한 하루치 데이터 중 일부 (각 16-bit uint, 33MB) 에 대해 테스트하여 정상작동하는 것을 확인하였습니다. 한 개의 파일마다 사용한 bash script는 아래와 같습니다 (Docker CLI에서 bash test.sh 로 실행함):

```
current_date_time="`date +%Y-%m-%d\ %H:%M:%S`";echo $current_date_time;
mv 2005UD-60.fit input.fits
solve-field input.fits -N 2005UD-60.fits --nsigma 15 --downsample 4 --radius 0.2 -u app -L 0.30 -U 0.33 --cpulimit 300 --no-plot --overwrite --no-remove-lines
```

* **NOTE**: 제 컴퓨터 (MBP 2018 15" macOS 10.14.6, 2.6 GHz i7, RAM 16GB 2400MHz DDR4)에서 6 CPU, 3GB RAM을 할당하여 테스트하였을 때 CPU사용량은 최대 약 140% (아마 최대로 병렬계산하진 않는 듯), **이미지마다 10-20초 정도** 시간이 소요되었습니다



## 향후 사용방안

예를 들어 서울대 천문대를 포함한 일부 천문대에서는 관측 후 WCS가 자동으로 입력되지 않아 사용자입장에서 처리해야하는 번거로움이 있었습니다. 관측실 컴퓨터는 윈도즈 10이지만 Docker를 이용하여 ``solve-field`` 를 설치하는 경우 매일 박명 후 혹은 실시간으로 FITS 파일에 WCS를 입혀 관측자에게 제공할 수 있겠습니다. (여기 소개한 astrometry 도커 이미지 공유자 dam90의 경우도 본인의 천체사진에 그렇게 WCS를 입히고자 만들었다고 밝히고 있습니다.)

한편 저의 경우 서버를 사용하지 않고 개인 노트북으로 연구를 진행하므로 astrometry를 위해 가상머신을 따로 운용하는 건 힘든 일이었는데 이 기회에 이 불편함 + 가상머신의 용량 상당수(약 10GB)를 떼어낼 수 있었습니다.

향후 수-수십년 간은 많은 소프트웨어들이 Docker image형태로 배포될 것으로 생각됩니다. 개발자 본인이 아니어도 docker image를 만들 수 있기 때문에 예를 들어 항성진화 시뮬레이션 소프트웨어 [MESA의 도커 이미지](https://github.com/evbauer/MESA-Docker)가 그렇듯 "많이들 쓰는데 OS의존성이 심하거나 설치가 귀찮고, 다른 언어로 다시 짜긴 힘든" 것들이 도커로 배포되지 않을지.... 미래를 고려할 때 Docker를 설치하는데 사용한 디스크 공간이 효용 없을 것 같지는 않습니다.

~~그러나 가장 좋은 방법은 OS에 의존적인 코드를 애초에 만들지 않는 것...~~

