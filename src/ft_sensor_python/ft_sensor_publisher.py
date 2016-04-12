import rospy
from std_msgs.msg import Float32MultiArray
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

class FTpublisher:

    def __init__(self, rospy):
        self.pub = rospy.Publisher('ft_classifier', Float32MultiArray,queue_size=10)
        self.y_msg = Float32MultiArray()

    def publish(self,Y):
        self.y_msg.data = Y
        self.pub.publish(self.y_msg)