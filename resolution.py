# -*- coding: utf-8 -*-
import numpy as np
f=1283.8955e6
c=299792458
lam=c/f
divparam=7
angsizeparam=45

A1=np.array([5109264.137437,2005901.390395,-3239583.343220])
A2=np.array([5109701.312268,2003312.687320,-3240508.721915])


def radtoarcsec(theta):
    degtheta=theta*180/np.pi
    arcmintheta=60*degtheta
    arcsectheta=60*arcmintheta
    return arcsectheta
    
def resol(A1,A2,f):
    lam=c/f
    b=np.sqrt(sum((A1-A2)**2))
    res=lam/b
    resfinal=radtoarcsec(res)/divparam
    print('beam=',resfinal,' arcsec')
    angsize=60*angsizeparam/(f*10**(-9))
    print('angsize=',angsize,' arcsec')
    print('imsize=',angsize/resfinal,' pixels')

def goodresol(approxsize):
    n=0
    res=10
    while res<approxsize:
        n+=1
        res=10*2**n
    return res
    