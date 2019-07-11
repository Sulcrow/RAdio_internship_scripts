# -*- coding: utf-8 -*-
import numpy as np

N=10
dchan=50
FLUX=np.empty((N,3))
for i in range(N):
    output=imfit(imagename='GX_339-4.chan'+str(i*dchan)+'.image',region='FLUX_region2.reg',
    excludepix = [(-1e10),0])
    #exclude negative pixels
    if output['converged'][0]==False:
        peak=0
        integrated=np.array([0])
    else:
        peak=output['results']['component0']['peak']['value']
        integrated=output['results']['component0']['flux']['value']
    FLUX[i]=np.array([i*dchan,integrated[0],peak])

#integrated in Jy and peak in Jy/beam
#integrated is an array

regions=('FLUX_rms_regions1.reg','FLUX_rms_regions2.reg','FLUX_rms_regions3.reg',
'FLUX_rms_regions4.reg','FLUX_rms_regions5.reg','FLUX_rms_regions6.reg')
radicalname='GX_339-4.chan'

def rms_2im(image,regions):
    rms=np.empty((len(regions),))
    for k in range(len(regions)):
        myoutput=imstat(imagename=image,region=regions[k])
        rms[k]=myoutput['rms']
    return rms

#premiÃ¨re image Ã  1 min et derniÃ¨re Ã  10 min :

RMS=np.empty((N,len(regions)))    

for i in range(N):
    imname=radicalname+str(i*dchan)+'.image'
    RMS[i]=rms_2im(imname,regions)
    
moyRMS=np.mean(RMS,axis=1)

results=np.concatenate((FLUX,np.transpose(np.array([moyRMS]))),axis=1)
np.savetxt('FLUX_computation2_log.dat',results)