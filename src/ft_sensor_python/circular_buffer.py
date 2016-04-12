# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:44:19 2016

@author: guillaume
"""
import collections

class CircularBuffer:
    
    def __init__(self,size):
        self.data = [None for i in xrange(size)]
        
    def append(self,x):
        self.data.pop(0)
        self.data.append(x) 
        
    def get_most_common(self):
        val = collections.Counter(self.data).most_common()[0][0]
        if val is not None:
            return val
        else:
            return 0
        
    def get(self):
        return self.data
        
    def print_data(self):
        print "".join([str(x) for x in self.data])