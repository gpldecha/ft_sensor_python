import numpy as np
from numpy import linalg as LA
from bar_plot import OneLineBarPlot

def bel_function(x, var=1.0):
    return 1 - np.exp(-(1.0 / var) * (x * x))

def rescale(x,oldMin,oldMax,newmin,newMax):
    return (((x - oldMin) * (newMax - newmin)) / (oldMax - oldMin)) + newmin


class ThreasholdContact:
    def __init__(self):
        self.min_f               = 3
        self.max_f               = 5
        self.force_threashold    = 1.0
        self.torque_threashold   = 0.1
        self.bFirst              = True
        
    def get_num_classes(self):
        return 3
        
    def plot(self,probs):
        if self.bFirst:
            self.barp               = OneLineBarPlot('Features',['surf','edge','socket'])
            self.bFirst             = False
        self.barp.plot(np.array(probs))
        
    def classify(self, ft_wrench):
        norm_f = LA.norm(ft_wrench[0:3])
        norm_t = LA.norm(ft_wrench[3:6])
        torque_xy = ft_wrench[3:5]        
        norm_t_s = rescale(norm_t,0,0.2,0,2)
        
        #print "torque: ", norm_t
        
        prob_contact = 0
        prob_edge = 0
        prob_socket = 0
        if norm_f >= self.force_threashold:
            prob_contact = 1
        if norm_t >= self.torque_threashold:
            prob_edge = 1

        #print("p: [%f  %f]" % (prob_contact,prob_edge))
        return np.array([prob_contact,prob_edge,prob_socket])