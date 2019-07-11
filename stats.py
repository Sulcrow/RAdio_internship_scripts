# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

rms_data=np.loadtxt('RMS_computation_log.dat')
rms_data_res=rms_data[:,0]
 
rms_data_im=rms_data[:,1]
 
flux_data=np.loadtxt('FLUX_computation_log.dat')
 
#rms for 15 minutes


RMS_res=rms_data_res[:,0]
RMS_res_error=rms_data_res[:,1]

RMS_im=rms_data_im[:,0]
RMS_im_error=rms_data_im[:,1]

numofpoints=10
TimeObs=np.arange(1,11)

plt.figure(1)
plt.subplot(211)
plt.errorbar(TimeObs,RMS_res, yerr=RMS_res_error, fmt='.')
plt.xlabel(u'Observation Duration (in min)')
plt.ylabel(u'RMS')
plt.title('RMS from residual')
plt.ticklabel_format(axis='y', style='sci',scilimits=(0,0))
plt.xlim(0,11)


plt.subplot(212)
plt.errorbar(TimeObs,RMS_im, yerr=RMS_im_error, fmt='.')
plt.xlabel(u'Observation Duration (in min)')
plt.ylabel(u'RMS')
plt.title('RMS from image')
plt.savefig('RMS_residual_3rdtry.eps',format='eps')
plt.xlim(0,11)

plt.ticklabel_format(axis='y', style='sci',scilimits=(0,0))
plt.tight_layout()

plt.figure(2)
plt.errorbar((flux_data[:,0]+5)*1.671875e6+856.731e6,flux_data[:,1],
              yerr=flux_data[:,3], fmt='-o',)
plt.errorbar((flux_data[:,0]+5)*1.671875e6+856.731e6,flux_data[:,2],
              yerr=flux_data[:,3], fmt='-o',)
plt.legend(['Integrated flux in Jy','Peak flux in Jy/beam'],loc=4)
plt.xlabel(u'Mid Frequency for each channel set (in Hz)')
plt.ylabel(u'Flux')
plt.title('Flux for sets of 10 channels each with a width of 1671.875 kHz')
plt.ticklabel_format(axis='both', style='sci',scilimits=(0,0))
plt.savefig('FLUX_GX.profile_1.pdf',format='pdf')