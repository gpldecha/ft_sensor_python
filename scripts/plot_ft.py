# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:21:01 2016

@author: guillaume
"""

import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def compute_sub_mean(X):
    mu = np.mean(X[1:100,:],axis=0)
    return X - np.tile(mu,(X.shape[0],1))
    
    
def plot_scatter_3(X):   
    plt.close('all')
    fig = plt.figure('Force/Torque',facecolor='white')
    ax1 = fig.add_subplot(121, projection='3d')    
    ax2 = fig.add_subplot(122, projection='3d')    
    ax1.scatter(X[:,0],X[:,1],X[:,2])
    ax2.scatter(X[:,3],X[:,4],X[:,5])
 
    ax1.set_title(r'Force',fontsize=20)
    ax1.set_xlabel(r"$F_{x}$",fontsize=20)  
    ax1.set_ylabel(r"$F_{y}$",fontsize=20)
    ax1.set_zlabel(r"$F_{z}$",fontsize=20)

    ax2.set_title(r'Torque',fontsize=20)
    ax2.set_xlabel(r"$T_{x}$",fontsize=20)  
    ax2.set_ylabel(r"$T_{y}$",fontsize=20)
    ax2.set_zlabel(r"$T_{z}$",fontsize=20) 
    

if __name__ == '__main__':
    
    X = np.loadtxt('/home/guillaume/roscode/catkin_ws3/src/ft_sensor_python/scripts/ft.txt')
    print "Loaded FT data"
    print "X: ", X.shape
    
    X_ = compute_sub_mean(X)
    plot_scatter_3(X_)
    
    np.savetxt('/home/guillaume/roscode/catkin_ws3/src/ft_sensor_python/scripts/data/X_sub_mean.txt',X_) 
    
    
    
    
