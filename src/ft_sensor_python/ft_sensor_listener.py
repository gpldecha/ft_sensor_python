#!/usr/bin/env python

import rospy
from geometry_msgs.msg import WrenchStamped
import numpy as np


class FTlistener:

    def __init__(self, rospy):
        self.rospy = rospy
        self.rospy.Subscriber("/lwr/ee_ft", WrenchStamped, self.callback)
        self.ft_wrench = np.mat(6 * [0]).T

    def callback(self, ws):
        self.ft_wrench = np.mat([ws.wrench.force.x, ws.wrench.force.y, ws.wrench.force.z,
                                 ws.wrench.torque.x, ws.wrench.torque.y, ws.wrench.torque.z]).T

