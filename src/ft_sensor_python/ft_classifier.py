import numpy as np
from numpy import linalg as LA


def bel_function(x, var=1.0):
    return 1 - np.exp(-(1.0 / var) * (x * x))


class ThreasholdContact:

    def __init__(self):
        self.min_f = 3
        self.max_f = 5
        self.nat_noise = 1

    def classify(self,ft_wrench):
        norm_f = LA.norm(ft_wrench[0:3])
        print "norm(force) ", norm_f
        prob_contact = 0
        if norm_f >= self.nat_noise:
            prob_contact = bel_function(norm_f-self.nat_noise ,1.0/5.0)

        print "prob contact: ", prob_contact



class FTClassifier:
    def __init__(self, rospy):
        self.rospy = rospy
        self.threashold_c = ThreasholdContact()


    def classify(self, ft_wrench):
        """
        Given force and torque predict if a contact occured or not

        :param ft_wrench: 6 dim numpy matrix
        :return: void
        """


        return self.threashold_c.classify(ft_wrench)
