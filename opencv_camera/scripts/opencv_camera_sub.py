import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
def img_decode(data):
	try:
		cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
	except CvBridgeError as e:
		print(e)
	cv2.imshow("Subscriber Frame", cv_image)
	cv2.waitKey(3)
def main():
	rospy.init_node("OpenCV_Camera_Sub_node", anonymous=True)
	rospy.Subscriber("OpenCV_Camera_Pub",Image, img_decode)
	rospy.spin()
main()
