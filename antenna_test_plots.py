import numpy as np
import matplotlib.pyplot as plt

FLUX_integrated=np.loadtxt('ANTENNA_TEST_flux_integrated.dat')
FLUX_peak=np.loadtxt('ANTENNA_TEST_flux_peak.dat')
RMS=np.loadtxt('ANTENNA_TEST_rms.dat')     
RMS_std=np.loadtxt('ANTENNA_TEST_rms_std.dat')
SNR=np.loadtxt('ANTENNA_TEST_snr.dat')
N_removed_ants=np.arange(1,2*len(SNR[:,0])+1,2)



plt.figure(1)
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9,11)])
#plt.subplot(4,1,1)
for i in range(len(SNR[0,:])):
    plt.errorbar(N_removed_ants,FLUX_integrated[:,i],
              yerr=RMS[:,i], fmt='-o')
plt.ylabel(u'Integrated Flux (Jy)')
plt.ticklabel_format(axis='y', style='sci',scilimits=(0,0))
plt.xlabel(u'Number of removed antennas')
plt.title(u'Integrated Flux for GX 339-4 -Meerkat  Ring')

#plt.subplot(4,1,2)
plt.figure(2)
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9,11)])
for i in range(len(SNR[0,:])):
    plt.errorbar(N_removed_ants,FLUX_peak[:,i],
              yerr=RMS[:,i], fmt='-o')
plt.ylabel(u'Peak Flux (Jy/beam)')
plt.ticklabel_format(axis='y', style='sci',scilimits=(0,0))
plt.xlabel(u'Number of removed antennas')
plt.title(u'Peak Flux for GX 339-4 - Meerkat Ring')

plt.figure(3)
#plt.subplot(4,1,3)
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9,11)])
for i in range(len(SNR[0,:])):
    plt.errorbar(N_removed_ants,RMS[:,i],
              yerr=RMS_std[:,i], fmt='-o')
plt.ylabel(u'RMS (Jy/beam)')
plt.ticklabel_format(axis='y', style='sci',scilimits=(0,0))
plt.xlabel(u'Number of removed antennas')
plt.title(u'Noise - Meerkat Ring')

plt.figure(4)
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9,11)])
#plt.subplot(4,1,4)
for i in range(len(SNR[0,:])):
    plt.plot(N_removed_ants,SNR[:,i],'-o')
plt.ylabel(u'SNR')
plt.ticklabel_format(axis='y', style='sci',scilimits=(0,0))
plt.title(u'Signal to noise ratio - Meerkat Ring')

plt.xlabel(u'Number of removed antennas')


#plt.savefig('antenna_test_ring_plot.eps',format='eps')