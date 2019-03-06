# Make ColorBar with Dvorak Analysis

import os

name = input('Name your Colorbar: ')
outfile = open('ir-'+name+'.txt','w')

coldest = input('Import the RGB numbers of the coldest color (-273.15℃): ')
ecdg_wa = input('Import the RGB numbers of the warmest bound of ECDG (-87℃): ')
outfile.write('-273.15 %s -87 %s \n' %(coldest, ecdg_wa))

vcdg_co = input('Import the RGB numbers of the coldest bound of VCDG (-87℃): ')
vcdg_wa = input('Import the RGB numbers of the warmest bound of VCDG (-85℃): ')
outfile.write('-87 %s -85 %s \n' %(vcdg_co, vcdg_wa))

cdg_co = input('Import the RGB numbers of the coldest bound of CDG (-85℃): ')
cdg_wa = input('Import the RGB numbers of the warmest bound of CDG (-81℃): ')
outfile.write('-85 %s -81 %s \n' %(cdg_co, cdg_wa))

cmg_co = input('Import the RGB numbers of the coldest bound of CMG (-81℃): ')
cmg_wa = input('Import the RGB numbers of the warmest bound of CMG (-76℃): ')
outfile.write('-81 %s -76 %s \n' %(cmg_co, cmg_wa))

w_co = input('Import the RGB numbers of the coldest bound of W (-76℃): ')
w_wa = input('Import the RGB numbers of the warmest bound of W (-70℃): ')
outfile.write('-76 %s -70 %s \n' %(w_co, w_wa))

b_co = input('Import the RGB numbers of the coldest bound of B (-70℃): ')
b_wa = input('Import the RGB numbers of the warmest bound of B (-64℃): ')
outfile.write('-70 %s -64 %s \n' %(b_co, b_wa))

lg_co = input('Import the RGB numbers of the coldest bound of LG (-64℃): ')
lg_wa = input('Import the RGB numbers of the warmest bound of LG (-54℃): ')
outfile.write('-64 %s -54 %s \n' %(lg_co, lg_wa))

mg_co = input('Import the RGB numbers of the coldest bound of MG (-54℃): ')
mg_wa = input('Import the RGB numbers of the warmest bound of MG (-42℃): ')
outfile.write('-54 %s -42 %s \n' %(mg_co, mg_wa))

dg_co = input('Import the RGB numbers of the coldest bound of DG (-42℃): ')
dg_wa = input('Import the RGB numbers of the warmest bound of DG (-31℃): ')
outfile.write('-42 %s -31 %s \n' %(dg_co, dg_wa))

ow_co = input('Import the RGB numbers of the coldest bound of OW (-31℃): ')
ow_wa = input('Import the RGB numbers of the warmest bound of OW (+9℃): ')
outfile.write('-31 %s 9 %s \n' %(ow_co, ow_wa))

wmg_co = input('Import the RGB numbers of the coldest bound of WMG (+9℃): ')
wmg_wa = input('Import the RGB numbers of the warmest bound of WMG (+20℃): ')
outfile.write('-9 %s 20 %s \n' %(wmg_co, wmg_co))

wa_co = input('Import the RGB numbers of the coldest bound of Warm Area (+20℃): ')
wa_wa = input('Import the RGB numbers of the warmest bound of Warm Area (+50℃): ')
outfile.write('20 %s 50 %s \n' %(wa_co, wa_co))
