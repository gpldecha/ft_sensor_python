import numpy as np
from ft_sensor_python.ft_model_classifier import *
from ft_sensor_python.ft_threashod_classifer import *
from circular_buffer import CircularBuffer
from collections import Counter

class FTClassifier:
    def __init__(self, rospy,classifier_type):
        self.rospy              = rospy
        self.classifier_type    = classifier_type

        self.threashold_c       = ThreasholdContact()
        self.gmm_c              = FTGMMClassifier('/home/guillaume/PythonWorkSpace/Peg_sensor_model/models/gmm/gmm.p')
        self.dgmm_c             = FTGMMClassifier('/home/guillaume/PythonWorkSpace/Peg_sensor_model/models/gmm/dgmm.p')
        
        if self.classifier_type == 'gmm':
            self.c_buffers          = [CircularBuffer(25) for i in range(self.gmm_c.get_num_classes())]
        elif self.classifier_type == 'threashold':
            self.c_buffers          = [CircularBuffer(25) for i in range(self.threashold_c.get_num_classes())]

        
    def buffer_reguliser(self,probs):  
        props = probs.tolist()
        for i, x in enumerate(props): 
            self.c_buffers[i].append(x)
            probs[i] = self.c_buffers[i].get_most_common()    
        return np.array(probs)            


    def classify(self, ft_wrench,belief_f,T):
        """
        Given force and torque predict if a contact occured or not

        :param ft_wrench: 6 dim numpy matrix
               belief_f: 4 dim belief feature vector
               T: position of the socket  
        :return: void
        """
        
        if self.classifier_type == 'gmm':
            probs = self.gmm_c.classify(ft_wrench)
            self.gmm_c.plot(probs)
        elif self.classifier_type == 'threashold':
            probs = self.threashold_c.classify(ft_wrench);
            probs = self.buffer_reguliser(probs)
            #self.threashold_c.plot(probs)
        else:
            print "no such classifier: ", self.classifier_type          
                  
        return probs.tolist()
