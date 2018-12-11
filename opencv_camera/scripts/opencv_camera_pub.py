import rospy
import numpy
import cv2 as cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

##Create publisher of data type Image
image_publisher = rospy.Publisher("OpenCV_Camera_Pub", Image,queue_size=10)
rospy.init_node("OpenCV_Camera_Pub_node", anonymous=True)
##Initialize cv_bridge
bridge = CvBridge()

########CODE FOR RECORDING ########
cap = cv2.VideoCapture(0)

#Sets the width capture resolution
cap.set(3,320)
#Sets the height capture resolution
cap.set(4,240)

speed = 0
altitude = 0
font = cv2.FONT_HERSHEY_SIMPLEX
#[Testing]

###########User Settings############
SpeedOnOff = False
AltitudeOnOff = False
while(True):
	speed+=1;
	altitude+=1;
	if(speed > 25):
		speed = 0
        if(altitude > 200):
        	altitude = 50
	ret, frame = cap.read()

############Toggles###############################
	if AltitudeOnOff:
		cv2.putText(frame,'alt  '+str(altitude)+" ft",(10,30), font, 1,(66,244,72),2)
	if SpeedOnOff:
		cv2.putText(frame,'spd '+ str(speed)+" mph",(10,60), font, 1,(66,244,72),2)
#####################Display Frame###############

	cv2.imshow('Publisher Frame',frame)
	check = cv2.waitKey(1)
####################Toggle Speed #################
	if check == ord('s'):
			SpeedOnOff = not SpeedOnOff
#############Toggle Altitude#######################
	if check== ord('a'):
		AltitudeOnOff = not AltitudeOnOff
###################QUIT##########################
	if check == ord('q'):
		break
###################################
	try:
		image_publisher.publish(bridge.cv2_to_imgmsg(frame,"bgr8"))
	except CvBridgeError as e:
		print(e)
cap.release()
cv2.destroyAllWindows()






##EditFrame perorms all the alterations to the original image
def EditFrame(frame):
        cv2.putText(frame,'alt  '+str(altitude)+" ft",(10,30), font, 1,(66,244,72),2)
        if SpeedOnOff:
                cv2.putText(frame,'spd '+ str(speed)+" mph",(10,60), font, 1,(66,244,72),2)
        if cv2.waitKey(10) & 0xFF == ord('s'):
                if not SpeedOnOff:
			SpeedOnOff = True
		else:
			SpeedOnOff = False
