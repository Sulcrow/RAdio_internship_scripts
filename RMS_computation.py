# -*- coding: utf-8 -*-
import numpy as np

regions=('RMS_region1.reg','RMS_region2.reg','RMS_region3.reg',
'RMS_region4.reg','RMS_region5.reg','RMS_region6.reg','RMS_region7.reg')
radicalname='GX_339-4.RMS.'

def rms_1im(image,regions):
    rms=np.empty((len(regions),))
    for k in range(len(regions)):
        myoutput=imstat(imagename=image,region=regions[k])
        rms[k]=myoutput['rms']
    return rms

#première image à 1 min et dernière à 10 min :

RMS=np.empty((10,len(regions)))    

for i in range(10):
    imname=radicalname+str(i+1)+'min.image'
    RMS[i]=rms_1im(imname,regions)
    
moyRMS=np.mean(RMS,axis=1)
stdRMS=np.std(RMS,axis=1)

result=np.transpose(np.array([moyRMS,stdRMS]))
print(result)
np.savetxt('RMS_computation_log.dat',result)