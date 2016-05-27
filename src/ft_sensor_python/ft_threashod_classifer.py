import numpy as np
from numpy import linalg as LA
from bar_plot import OneLineBarPlot
from circular_buffer import CircularBuffer
from scipy import stats
from copy import deepcopy

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
        self.F                   = np.zeros(3)
        self.max_N               = 6
        self.c_buffers           = [CircularBuffer(25) for i in range(3)]
        self.x                   = np.arange(25)
        self.slope_F0            = 0
        self.slope_F1            = 0
        self.slope_F2            = 0
        self.a                   = 8
        self.b                   = 1

        
    def get_num_classes(self):
        return 4
        
    def sigmf(self,x,a,c):
        return 1.0/(1.0 + np.exp(-a * (x - c)))
        
    def bound_value(self,x,min_v,max_v):
        if x > max_v:
            x = max_v
        elif x < min_v:
            x = min_v
            
        return x            
        
    def plot(self,probs):
        if self.bFirst:
            self.barp               = OneLineBarPlot('Features',['surf','edge','socket'])
            self.bFirst             = False
        self.barp.plot(np.array(probs))
        
    def classify(self, ft_wrench):
        
        self.F[2] = ft_wrench[0]        
        self.F[1] = ft_wrench[1] 
        self.F[0] = ft_wrench[2]
        self.F    = -self.F
        
        self.F[0] = self.bound_value(self.F[0],-self.max_N,self.max_N)        
        self.F[1] = self.bound_value(self.F[1],-self.max_N,self.max_N)
        self.F[2] = self.bound_value(self.F[2],-self.max_N,self.max_N)
        
        
        self.c_buffers[0].append(self.F[0])        
        self.c_buffers[1].append(self.F[1])        
        self.c_buffers[2].append(self.F[2])                         



        if  self.c_buffers[0].get()[0] != None:
            self.slope_F0, _, _,_,_ =  stats.linregress(self.x,self.c_buffers[0].get())
            self.slope_F1, _, _,_,_ =  stats.linregress(self.x,self.c_buffers[1].get())
            self.slope_F2, _, _,_,_ =  stats.linregress(self.x,self.c_buffers[2].get())

           
        #self.slope_F0 =  stats.linregress(self.x,self.c_buffers[0].get())
        #slope_F1 =  stats.linregress(self.x,self.c_buffers[1].get())
        #slope_F2 =  stats.linregress(self.x,self.c_buffers[2].get())

        # buffer data and compute gradient
        
        
        #print "wrench: ", ft_wrench[0], ft_wrench[1], ft_wrench[2], ft_wrench[3], ft_wrench[4], ft_wrench[5]
        #print "F: ", self.F[0], self.F[1], self.F[2], " slope: ",  self.slope_F0

       
        norm_f = LA.norm(ft_wrench[0:3])
        #norm_t = LA.norm(ft_wrench[3:6])
        #torque_xy = ft_wrench[3:5]        
        #norm_t_s = rescale(norm_t,0,0.2,0,2)
        
        #print " ", norm_f, norm_t
        
        prob_contact      = 0

        f_l = deepcopy(self.F[1])
        f_r = deepcopy(self.F[1])
        f_l = -f_l;        
        
        prob_left_edge      = self.sigmf(f_l,           self.a,self.b)
        prob_right_edge     = self.sigmf(f_r,           self.a,self.b)
        prob_up_edge        = self.sigmf(-self.F[2],    self.a,self.b)
        prob_down_edge      = self.sigmf(self.F[2],     self.a,self.b)
                
        
        if norm_f >= self.force_threashold:
            prob_contact = 1

        #print("p: [%f  %f]" % (prob_contact,prob_edge))
        return np.array([prob_contact,self.F[0],self.F[1],self.F[2],prob_right_edge,prob_left_edge,prob_up_edge,prob_down_edge])
        
        
        
        