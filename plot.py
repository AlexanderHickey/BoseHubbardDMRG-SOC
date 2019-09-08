'''
Plot the correlations, momentum distributions and structure
factors for a given set of ground state measurements.
'''

import numpy as np
import matplotlib.pyplot as plt

#Figure size and resolution
figsize = (10,8)
DPI = 300


def occ(corr1UP, corr1DO, corr2UP, corr2DO):
    '''
    Compute the momentum distributions and structure factors
    '''
    
    #Change type to numpy array
    corr1UP = np.array(corr1UP)
    corr1DO = np.array(corr1DO)
    corr2UP = np.array(corr2UP)
    corr2DO = np.array(corr2DO)
    
    #Lattice length
    L = corr1UP.shape[0]
    
    #Enumerate crystal momentum in the 1st Brillouin zone
    klist = [2*np.pi/L*(j-0.5*L) for j in range(L)]
    dist = np.arange(L)
    
    nkUP, skUP = [], []
    nkDO, skDO = [], []
    
    #Compute momentum distribution functions and structure factors
    for j in range(L):
        
        fourier_phases = np.exp(1.0j*klist[j]*dist)
        
        nkUP.append( np.sum(fourier_phases*corr1UP) )
        nkDO.append( np.sum(fourier_phases*corr1DO) )
        skUP.append( np.sum(fourier_phases*corr2UP) )
        skDO.append( np.sum(fourier_phases*corr2DO) )


    return np.array(klist), np.abs(nkUP), np.abs(nkDO), np.abs(skUP)/L, np.abs(skDO)/L
    
    
def plot_momentum(corr1UP, corr1DO, corr2UP, corr2DO, indx):
    '''
    Plot the momentum distributions and structure factors
    ''' 
     
    #Compute distributions and structure factors
    klist, nkUP, nkDO, skUP, skDO = occ(corr1UP, corr1DO, corr2UP, corr2DO)
    
    #Plot on 2x2 grid
    fig, ax = plt.subplots(2,2,figsize = figsize,sharex=True)
    fig.suptitle(title)

    ax[0][0].plot(klist,nkUP,marker = 'o',color = 'black')
    ax[1][0].plot(klist,nkDO,marker = 's',color = 'black')
    ax[0][1].plot(klist,skUP,marker = '*',color = 'black')
    ax[1][1].plot(klist,skDO,marker = 'P',color = 'black')
    
    ax[0][0].set_title(r'$n_{k,\uparrow}$',fontsize = 14)
    ax[1][0].set_title(r'$n_{k,\downarrow}$',fontsize = 14)
    ax[0][1].set_title(r'$S_{k,\uparrow}$',fontsize = 14)
    ax[1][1].set_title(r'$S_{k,\downarrow}$',fontsize = 14)
    
    ax[1][0].set_xlabel('$k$',fontsize = 18)
    ax[1][1].set_xlabel('$k$',fontsize = 18)
    
    plt.xlim(-np.pi-.1,np.pi)
    plt.xlabel('k',fontsize = 18)
    
    plt.savefig('momentum_fig{}.png'.format(indx), dpi = DPI)
    
    plt.close()
    
    
    
def plot_correlations(corr1UP, corr1DO, corr2UP, corr2DO, corr1UD, corr2UD, title, indx):
    '''
    Plot the measured correlations
    ''' 
    
    #Length of lattice
    L = len(corr1UP)
    
    #Plot on 3x2 grid
    fig, ax = plt.subplots(3,2,figsize = figsize,sharex=True)
    fig.suptitle(title)

    ax[0][0].plot(np.arange(L),corr1UP,marker = 'o',color = 'black')
    ax[1][0].plot(np.arange(L),corr1DO,marker = 's',color = 'black')
    ax[0][1].plot(np.arange(L),corr2UP,marker = '*',color = 'black')
    ax[1][1].plot(np.arange(L),corr2DO,marker = 'P',color = 'black')
    ax[2][0].plot(np.arange(L),corr1UD,marker = 'P',color = 'black')
    ax[2][1].plot(np.arange(L),corr2UD,marker = 'P',color = 'black')
    
    ax[0][0].set_title(r'$\langle b_{0\uparrow}^\dagger b_{j\uparrow} \rangle$',fontsize = 14)
    ax[1][0].set_title(r'$\langle b_{0\downarrow}^\dagger b_{j\downarrow} \rangle$',fontsize = 14)
    ax[0][1].set_title(r'$\langle n_{0\uparrow} n_{j\uparrow} \rangle$',fontsize = 14)
    ax[1][1].set_title(r'$\langle n_{0\downarrow} n_{j\downarrow} \rangle$',fontsize = 14)
    ax[2][0].set_title(r'$\langle b_{0\uparrow}^\dagger b_{j\downarrow} \rangle$',fontsize = 14)
    ax[2][1].set_title(r'$\langle n_{0\uparrow} n_{j\downarrow} \rangle$',fontsize = 14)
    
    ax[2][0].set_xlabel('$j$',fontsize = 18)
    ax[2][1].set_xlabel('$j$',fontsize = 18)
    
    plt.xlim(-.1,L+0.1)
    plt.xlabel('j',fontsize = 18)
    
    plt.savefig('correlation_fig{}.png'.format(indx), dpi = DPI)
    
    plt.close()