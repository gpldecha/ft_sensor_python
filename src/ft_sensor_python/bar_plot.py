# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:15:04 2016

@author: guillaume
"""
import matplotlib.pylab as plt
from matplotlib.pyplot import plot, ion, show, draw
import numpy as np

class OneLineBarPlot:

    def __init__(self,name='my bar plot',xticklabels=None):        
        ion()
        self.bFirst = True        
        self.fig = plt.figure(name,facecolor='white') 
        self.xticklabels = xticklabels
                
    def plot(self,prob):    
        x = np.arange(prob.size)
        y = prob.reshape(x.shape)
        if self.bFirst:
            self.hl  = plt.bar(x,y,align='center')
            self.ax = self.fig.gca()
            self.ax.set_xticks(x)
            if self.xticklabels != None:
                self.ax.set_xticklabels(self.xticklabels) 
            else:
                self.ax.set_xticklabels(map(str,range(x.size)))
            self.ax.set_xlabel('K')
            self.ax.set_ylabel('Prob')
            draw()
            self.bFirst = False
        else:
           self.ax.clear()
           self.ax.bar(x,y,align='center')
           self.ax.set_xticks(x)
           if self.xticklabels != None:
               self.ax.set_xticklabels(self.xticklabels) 
           else:
                self.ax.set_xticklabels(map(str,range(x.size)))
           self.ax.set_xlabel('K')
           self.ax.set_ylabel('Prob')
           draw()   
