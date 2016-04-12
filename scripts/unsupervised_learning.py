# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:14:10 2016

@author: guillaume
"""


import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn.mixture import GMM
from sklearn import datasets

import pickle

def train_gmm(X,k):
    print "Training GMM"
    bic = np.zeros(shape=(k.size))
    aic = np.zeros(shape=(k.size))
    
    for i in xrange(0,k.size):
        K   = int(k[i])
        print "K: ", K
        gmm = GMM(covariance_type='full',min_covar=0.001, n_components=K,n_init=5,n_iter=100, params='wmc', random_state=None, tol=0.001, verbose=0)
        gmm.fit(X)
        bic[i] = gmm.bic(X)
        aic[i] = gmm.aic(X)
        
    return (gmm,bic,aic)        


            
    
if __name__ == '__main__':
    
    data_name = 'X_sub_mean'
    X = np.loadtxt('/home/guillaume/roscode/catkin_ws3/src/ft_sensor_python/scripts/data/' + data_name +  '.txt')
    print "Loaded FT data"
    print "X: ", X.shape
    
    np.random.seed(5)
    model_name   = 'gmm'
    path_to_save = '/home/guillaume/roscode/catkin_ws3/src/ft_sensor_python/scripts/models/'
    
    k = np.array(range(3,10))
    gmm, bic, aic = train_gmm(X,k)

        
    plt.close('all')
    fig = plt.figure('BIC and AIC',facecolor='white')
    plt.plot(bic,'r')
    plt.plot(aic,'b')
    ax = fig.gca()
    ax.set_xticks(k)
    ax.set_xticklabels(map(str,k))

   
    bSave = True
    if bSave:
        print "Saving model..."
        pickle.dump(gmm, open(path_to_save + model_name + '.p', "wb" ),protocol=2)
    
    
    
    