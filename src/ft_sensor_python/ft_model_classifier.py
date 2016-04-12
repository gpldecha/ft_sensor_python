import numpy as np
from sklearn.mixture import GMM
from bar_plot import OneLineBarPlot
import pickle

class FTGMMClassifier:
    def __init__(self,model_filename):
        self.gmm        = pickle.load(open(model_filename,'rb'))
        self.bFirst     = True

    def get_num_classes(self):     
        return self.gmm.weights_.size
    
    def plot(self,prob):
        if self.bFirst:
            self.bFirst = False
            self.barp = OneLineBarPlot()
        self.barp.plot(prob)
      
    def classify(self, ft_wrench):  
        ft_wrench = ft_wrench.reshape((1,6))
        prob      = self.gmm.predict_proba(ft_wrench)  
        return prob