# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

flux_data=np.loadtxt('FLUX_computation3_log.dat')
freq=(flux_data[:,0]+25)*1.671875e6+856.731e6
position=np.loadtxt('Positions_maxflux.dat')

def JybeamtoJy(jybeam,imname):
    output=imhead(imagename=imname,mode='list')
    bmaj=(output['beammajor']['value']/3600)*np.pi/180
    bmin=(output['beamminor']['value']/3600)*np.pi/180
    cdelt1,cdelt2=abs(output['cdelt1']),abs(output['cdelt2'])
    solidangle=np.pi*bmin*bmaj/(4*cdelt1*cdelt2*np.log(2))
    return jybeam*solidangle

#Fit des données en supprimant les points ne convergeant pas:

S=flux_data[:,2]
lognu=np.log10(freq[S!=0])
S=S[S!=0]
logS=np.log10(S)

lin=lambda x,a,b:a*x+b

param,covar=curve_fit(lin,lognu,logS)

def limitsize(datamin,datamax,percent):
    valmin=datamin-abs(datamin-datamax)*percent
    valmax=datamax+abs(datamin-datamax)*percent
    return valmin,valmax


plt.figure(1)
for i in range(len(position[:,0])):
    plt.plot(position[i,0],position[i,1],'o',label='chan '+str(i*50),markersize=5)
plt.ticklabel_format(useOffset=False)
plt.legend(loc=4)
plt.xlim(limitsize(min(position[:,0]),max(position[:,0]),0.20))
plt.ylim(limitsize(min(position[:,1]),max(position[:,1]),0.20))
plt.xlabel(r'Ra')
plt.ylabel(r'Dec')
plt.savefig('Positions_maxflux.eps',format='eps')

plt.figure(2)
plt.errorbar(freq,flux_data[:,1],
              yerr=flux_data[:,3], fmt='-o',)
plt.errorbar(freq,flux_data[:,2],
              yerr=flux_data[:,3], fmt='-o',)
plt.legend(['Integrated flux in Jy','Peak flux in Jy/beam'],loc=4)
plt.xlabel(u'Mid Frequency for each channel set (in Hz)')
plt.ylabel(u'Flux')
plt.title('Flux for sets of 50 channels each with a width of 1671.875 kHz')
plt.ticklabel_format(axis='both', style='sci',scilimits=(0,0))
plt.tight_layout()
plt.savefig('FLUX_plot2.eps',format='eps')

plt.figure(3)
plt.plot(lognu,logS,'-o')
plt.plot(lognu,lin(lognu,param[0],param[1]),'c-')
plt.legend(['Data',r'Linear Fit $\alpha ='+str(param[0])+'$'],loc=4)
plt.xlabel(r'$log( \nu )$')
plt.ylabel(r'$log(S)$')
plt.ticklabel_format(axis='both', style='sci',scilimits=(0,0))
plt.savefig('FLUX_loglog2_fit.eps',format='eps')




