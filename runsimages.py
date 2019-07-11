# -*- coding: utf-8 -*-
for i in range(39,49,2):
    tclean(vis='1548489789_sdp_l0.full_1284.full_pol_x8_fg_wtspec_GX_339-4.ms',
    datacolumn='data',timerange='08:37:23.7~08:'+str(i)+':19.4',
    imagename='GX_339-4.RMS.'+str(i-37)+'min',imsize=200, cell='2arcsec',
    pblimit=(-0.1),gridder='widefield',weighting='briggs',niter=100000,
    robust=(-0.5),threshold='0.05mJy')