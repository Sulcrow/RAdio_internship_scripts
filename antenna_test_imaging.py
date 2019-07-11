# -*- coding: utf-8 -*-
import numpy as np
from numpy import random
import matplotlib.pyplot as plt




ants=['m000', 'm001', 'm002', 'm003', 'm004', 'm005', 'm006', 'm007', 'm008',
       'm009', 'm010', 'm011', 'm012', 'm013', 'm014', 'm015', 'm016', 'm017', 
       'm019', 'm020', 'm021', 'm022', 'm023', 'm024', 'm025', 'm027', 'm028', 
       'm029', 'm030', 'm031', 'm032', 'm033', 'm034', 'm035', 'm037', 'm038', 
       'm039', 'm040', 'm041', 'm042', 'm043', 'm044', 'm045', 'm046', 'm047', 
       'm048', 'm049', 'm050', 'm051', 'm052', 'm053', 'm054', 'm055', 'm056', 
       'm057', 'm058', 'm059', 'm060', 'm061', 'm062', 'm063']
       

position=np.array([[ 5109224.28330101,  2006790.34830945, -3239100.60432023],
       [ 5109237.64002439,  2006805.67700518, -3239069.99463992],
       [ 5109224.98529035,  2006765.00133159, -3239115.19822119],
       [ 5109247.71453184,  2006736.9651357 , -3239096.13442916],
       [ 5109244.68809625,  2006674.4233089 , -3239139.81459295],
       [ 5109222.76106102,  2006688.94849795, -3239165.94167899],
       [ 5109186.50377258,  2006764.80047433, -3239176.68337993],
       [ 5109162.04943626,  2006678.52756466, -3239269.23486208],
       [ 5109101.14230795,  2006650.3768303 , -3239383.32036296],
       [ 5109132.82118802,  2006798.06539449, -3239242.19060095],
       [ 5109046.34250297,  2006823.98222895, -3239363.79206003],
       [ 5109122.96650556,  2006849.69137709, -3239225.88024209],
       [ 5109095.03327091,  2006898.89267808, -3239239.95073131],
       [ 5109048.21915394,  2006984.47473988, -3239261.95549118],
       [ 5109082.89642682,  2007045.23603689, -3239169.09259079],
       [ 5109139.53273202,  2006992.24816646, -3239111.37666584],
       [ 5109127.05382964,  2007070.62721378, -3239082.80305883],
       [ 5109193.73983259,  2007001.70002865, -3239019.08733502],
       [ 5109122.95791977,  2006942.91666107, -3239168.36029351],
       [ 5109142.92017108,  2006871.50044504, -3239180.65456621],
       [ 5109272.06096906,  2006500.0158821 , -3239203.48775662],
       [ 5109454.06397737,  2006488.737612  , -3238920.41294648],
       [ 5109368.62411322,  2006509.64441463, -3239043.72464686],
       [ 5109516.48026315,  2006536.84237589, -3238791.43132279],
       [ 5109490.75229631,  2006708.37893053, -3238726.60887038],
       [ 5109293.29281629,  2006869.8171357 , -3238941.79568057],
       [ 5109296.30326859,  2006772.52959848, -3238996.8399094 ],
       [ 5109292.53415626,  2006730.67157098, -3239028.6327578 ],
       [ 5109310.29127383,  2007017.0281266 , -3238823.74451789],
       [ 5109273.32106579,  2007083.3921749 , -3238841.20281526],
       [ 5109233.60461138,  2007298.46868832, -3238770.86696955],
       [ 5109514.19718732,  2007536.96354954, -3238177.04240031],
       [ 5109175.83074595,  2007164.61743518, -3238946.9156469 ],
       [ 5109093.99133207,  2007162.92190296, -3239078.77446058],
       [ 5108965.29600136,  2007106.0701934 , -3239319.10395304],
       [ 5108973.98033999,  2006930.08522405, -3239413.36524623],
       [ 5108948.62739779,  2006963.57418339, -3239433.44955682],
       [ 5108993.64985368,  2006679.78331066, -3239536.37157185],
       [ 5109111.47167591,  2006445.98643079, -3239491.95658249],
       [ 5109233.14297356,  2006414.09185624, -3239318.09527487],
       [ 5109486.39894156,  2006225.48452776, -3239031.01278849],
       [ 5109925.4853336 ,  2006111.83101997, -3238401.38994635],
       [ 5110109.88125185,  2005177.89828222, -3238688.71124854],
       [ 5110676.48688875,  2005793.15238642, -3237408.15875938],
       [ 5109284.53190335,  2006201.5866797 , -3239366.632053  ],
       [ 5111608.04686902,  2004721.20483031, -3236602.97342706],
       [ 5110840.85251123,  2003560.04260211, -3238544.12269104],
       [ 5109666.43943372,  2004767.92389666, -3239646.10826641],
       [ 5109264.13743653,  2005901.39039513, -3239583.34322023],
       [ 5108992.20867905,  2006070.76368467, -3239910.94149326],
       [ 5108701.44164709,  2006603.92632982, -3240047.18872095],
       [ 5108767.23797614,  2007556.53944891, -3239354.5357537 ],
       [ 5108927.44924923,  2007973.795158  , -3238840.15487935],
       [ 5108955.98614919,  2008411.12463564, -3238520.34638302],
       [ 5110746.30689899,  2007713.60467784, -3236109.83980962],
       [ 5109561.45185604,  2009946.09498361, -3236606.07759979],
       [ 5108335.4040351 ,  2010410.68776868, -3238271.57018566],
       [ 5107206.79941873,  2009680.81249961, -3240512.45552003],
       [ 5108231.34510839,  2006391.5921877 , -3240926.75349309],
       [ 5108666.76835707,  2005032.47183077, -3241081.69731166],
       [ 5109701.31226756,  2003312.68732032, -3240508.72191522]])
       

rad=np.mean(np.sqrt(np.sum(position**2,axis=1)))

def carttospherical(cart):
    sphe=np.empty(cart.shape)
    sphe[:,0]=np.sqrt(np.sum(cart**2,axis=1))
    sphe[:,1]=np.arccos(cart[:,2]/sphe[:,0])
    sphe[:,2]=np.arctan(cart[:,1]/cart[:,0])
    return sphe
    
def localcoord(sphe):
    sphecentered=sphe-sphe[0,:]
    x_y=np.empty((sphe.shape[0],2))
    x_y[:,0]=sphecentered[:,2]*rad
    x_y[:,1]=-sphecentered[:,1]*rad
    return x_y

local=localcoord(carttospherical(position))
dist=np.sqrt(np.sum(local**2,axis=1))
#PARAM
coreradius=4.8e2

core=[]
ring=[]
local_core_x=[]
local_core_y=[]
local_ring_x=[]
local_ring_y=[]


for i in range(len(dist)):
    if dist[i]<coreradius:
        core.append(ants[i])
        local_core_x.append(local[i,0])
        local_core_y.append(local[i,1])
    else:
        ring.append(ants[i])
        local_ring_x.append(local[i,0])
        local_ring_y.append(local[i,1])
        
Ncore=len(core)
Nring=len(ring)
#RING OR CORE:
N=Ncore
Set=core
   
plt.figure(1)
plt.plot(local_core_x,local_core_y,'ro',label='Core')
plt.plot(local_ring_x,local_ring_y,'co',label='Ring')
plt.legend()
plt.savefig('antenna_test_core&ring_plot.eps',format='eps')

def takerandant(antennas,n):
    listants=list(antennas)
    if n==0:
        k=np.random.randint(0,len(listants))
        stringants=listants[k]
        remants=[listants[k]]
        return remants,stringants
    else:
        k=np.random.randint(0,len(listants))
        stringants=listants[k]
        remants=[listants[k]]
        listants.pop(k)
        for i in range(1,n):
            stringants+=','
            k=np.random.randint(0,len(listants))
            stringants+=listants[k]
            remants.append(listants[k])
            listants.pop(k)
    
        return remants,stringants
        
def findmax(image):
    stats=imstat(imagename=image,region='imstat_max_region.reg')
    string=stats['maxposf']
    l=string.split(",")
    pos=l[:2]
    return pos
    
def ellipseregion(posmax):
    string='ellipse[['+posmax[0]+','+posmax[1]+'],[0.003deg,0.0045deg],0rad], coord=J2000'
    return string
    

regions=('FLUX_rms_regions1.reg','FLUX_rms_regions2.reg','FLUX_rms_regions3.reg',
'FLUX_rms_regions4.reg','FLUX_rms_regions5.reg','FLUX_rms_regions6.reg','FLUX_rms_regions7.reg',
'FLUX_rms_regions8.reg','FLUX_rms_regions9.reg')
#PARAM RING OR CORE
radicalname='GX_339-4.core.without.'


def rms_2im(image,regions):
    rms=np.empty((len(regions),))
    for k in range(len(regions)):
        myoutput=imstat(imagename=image,region=regions[k])
        rms[k]=myoutput['rms']
    mean=np.mean(rms)
    std=np.std(rms)
    return mean,std
Ntest=10
step=2

FLUX_integrated=np.empty((np.floor(N/step),Ntest))
FLUX_peak=np.empty((np.floor(N/step),Ntest))
RMS=np.empty((np.floor(N/step),Ntest))
RMS_std=np.empty((np.floor(N/step),Ntest))
SNR=np.empty((np.floor(N/step),Ntest))
for i in range(int(np.floor(N/step))):
    print("i=",i)
    for k in range(Ntest):
        print("k=",k)
        #flux part
        remants,stringants=takerandant(Set,2*i+1)
        tclean(vis='1548489789_sdp_l0.full_1284.full_pol_x8_fg_wtspec_GX_339-4.ms',
               datacolumn='data',imagename=radicalname + stringants,
               imsize=1280, cell='2arcsec', antenna='!'+stringants,deconvolver='mtmfs',
               pblimit=(-0.1),gridder='widefield',weighting='uniform',niter=100000,
        robust=(-0.5),threshold='0.1mJy')
    
        image=radicalname + stringants+'.image.tt0'
        posmax=findmax(image)
        output=imfit(imagename=image,region=ellipseregion(posmax),
        excludepix = [(-1e10),0])
        #exclude negative pixels
        if output['converged'][0]==False:
            peak=0
            integrated=np.array([0])
        else:
            peak=output['results']['component0']['peak']['value']
            integrated=output['results']['component0']['flux']['value']
        FLUX_integrated[i,k]=integrated[0]
        FLUX_peak[i,k]=peak
        RMS[i,k],RMS_std[i,k]=rms_2im(image,regions)
        SNR[i,k]=FLUX_peak[i,k]/RMS[i,k]
        
np.savetxt('ANTENNA_TEST_core_flux_integrated.dat',FLUX_integrated)
np.savetxt('ANTENNA_TEST_core_flux_peak.dat',FLUX_peak)
np.savetxt('ANTENNA_TEST_core_rms.dat',RMS)     
np.savetxt('ANTENNA_TEST_core_rms_std.dat',RMS_std)
np.savetxt('ANTENNA_TEST_core_snr.dat',SNR) 


  