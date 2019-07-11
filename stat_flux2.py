# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def hexatodeg(hexa):
    ra,dec=hexa
    ra=ra.split(":")
    dec=dec.split(".",2)
    rh,rm,rs=[float(i) for i in ra]
    dd,dm,ds=[float(k) for k in dec]
    radeg=(rh+rm/(60)+rs/(60*60))*15
    decdeg=(abs(dd)+dm/(60)+ds/(60*60))
    if dd<0:
        decdeg=-decdeg
    return radeg,decdeg
    
    
def findmax(image):
    stats=imstat(imagename=image,region='imstat_max_region.reg')
    string=stats['maxposf']
    l=string.split(",")
    pos=l[:2]
    return pos
    
def ellipseregion(posmax):
    string='ellipse[['+posmax[0]+','+posmax[1]+'],[0.003deg,0.0045deg],0rad], coord=J2000'
    return string

N=10
dchan=50
DATA=np.empty((N,3))
POSITION_MAX=np.empty((N,2))
for i in range(N):
    image='GX_339-4.chan'+str(i*dchan)+'.image'
    posmax=findmax(image)
    POSITION_MAX[i]=np.array([hexatodeg(posmax)])
    output=imfit(imagename=image,region=ellipseregion(posmax),
    excludepix = [(-1e10),0])
    #exclude negative pixels
    if output['converged'][0]==False:
        peak=0
        integrated=np.array([0])
    else:
        peak=output['results']['component0']['peak']['value']
        integrated=output['results']['component0']['flux']['value']
    DATA[i]=np.array([i*dchan,integrated[0],peak])

#integrated in Jy and peak in Jy/beam
#integrated is an array

regions=('FLUX_rms_regions1.reg','FLUX_rms_regions2.reg','FLUX_rms_regions3.reg',
'FLUX_rms_regions4.reg','FLUX_rms_regions5.reg','FLUX_rms_regions6.reg','FLUX_rms_regions7.reg',
'FLUX_rms_regions8.reg','FLUX_rms_regions9.reg')
radicalname='GX_339-4.chan'

def rms_2im(image,regions):
    rms=np.empty((len(regions),))
    for k in range(len(regions)):
        myoutput=imstat(imagename=image,region=regions[k])
        rms[k]=myoutput['rms']
    return rms

#premiÃÂ¨re image Ã  1 min et derniÃÂ¨re Ã  10 min :

RMS=np.empty((N,len(regions)))    

for i in range(N):
    imname=radicalname+str(i*dchan)+'.image'
    RMS[i]=rms_2im(imname,regions)
    
moyRMS=np.mean(RMS,axis=1)

results=np.concatenate((DATA,np.transpose(np.array([moyRMS]))),axis=1)
np.savetxt('FLUX_computation3_log.dat',results)
np.savetxt('Positions_maxflux.dat',POSITION_MAX)