#!/usr/bin/env python

import rospy
from geometry_msgs.msg import WrenchStamped
from std_msgs.msg import Float64MultiArray
import numpy as np


class FTlistener:

    def __init__(self, rospy):
        self.rospy = rospy
        self.rospy.Subscriber("/ft_sensor/netft_data", WrenchStamped, self.callback_ft)
        self.rospy.Subscriber("/belief_features", Float64MultiArray, self.callback_belief_feature)
        self.ft_wrench = np.mat(6 * [0]).T
        self.belief_f  = np.empty(shape=(0, 0) )

    def callback_ft(self, ws):
        self.ft_wrench = np.mat([ws.wrench.force.x, ws.wrench.force.y, ws.wrench.force.z,
                                 ws.wrench.torque.x, ws.wrench.torque.y, ws.wrench.torque.z]).T
                                 
    def callback_belief_feature(self,x):
        self.belief_f = np.array(x.data)
