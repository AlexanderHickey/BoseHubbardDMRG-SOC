'''
This module is used to iterate through available simulation results
and generate corresponding correlation and distribution function plots.
'''

import pyalps
import numpy as np
import plot

#Enumerate indices corresponding to data files
indx_list = ['{}'.format(j) for j in range(800,852)]

#List measurements performed on the ground state
meas_list = ['Energy','Truncation error',
             'One-body Correlation UP','One-body Correlation DO',
             'Two-body Correlation UP','Two-body Correlation DO',
             'nUP','nDO',
             'One-body Correlation UPDO','Two-body Correlation UPDO']

for j in indx_list:
        
    fname = '{}'.format(j)

    try:
    
        #Load all measurements on ground state
        data = pyalps.loadEigenstateMeasurements(pyalps.getResultFiles(prefix=fname), what = meas_list)
        
        #Save eigenstate properties as a dictionary
        prop = data[0][0].props
        Nmax, L = prop['NMax'], prop['L']
        
        #Extrach properties
        E0     = data[0][0].y[0]
        trunc  = data[0][1].y[0]
        obUP   = data[0][2].y[0]
        obDO   = data[0][3].y[0]
        tbUP   = data[0][4].y[0]
        tbDO   = data[0][5].y[0]
        nUP    = data[0][6].y[0]
        nDO    = data[0][7].y[0]
        obUPDO = data[0][8].y[0]
        tbUPDO = data[0][9].y[0]
        
        #Plot title
        cor_title = 'Correlations for $L$ = {}, Nmax = {} \n $t$ = {:.3f}, $\mu$ = {:.3f}, $V$ = {:.3f}, $U_s$ = {:.3f}, $h_z$ = {:.3f}, $\gamma$ = {:.3f} \n Truncation error = {:.4E}'.format(int(L),int(Nmax),prop['t'],prop['mu'],prop['V'],prop['Uud'],prop['hz'],np.arcsin(prop['sg']),trunc)
        
        #Generate plots
        plot.plot_momentum(obUP, obDO, tbUP, tbDO, j)
        plot.plot_correlations(obUP, obDO, tbUP, tbDO, obUPDO, tbUPDO, cor_title, j)
    
    
    except:
    
        print('Failed to process {}'.format(fname))

