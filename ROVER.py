#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def drive_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard ", data.data)

    if data.data[0] == "A" and data.data[-1] == "B":
        data = data.data[1:-1]
        data_list = [data[i:i + 4] for i in range(0, len(data), 4)]

        for i in data_list:
            value = int(i[1:4])
            if i[0] == '0':
                if i[1:4] < 255:
                    value = value
                else:
                    value = 255


            elif i[0] == '1':
                if i[1:4] < 255:
                    value = -value
                else:
                    value = -255

            drive_data = String()
            drive_data.data += str(value) + ' '
        drive_data.data = drive_data.data[:-1]
        drive_pub = rospy.Publisher('/position/drive', String, queue_size=10)
        drive_pub.publish(drive_data)



def arm_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard ", data.data)

    if data.data[0] == "A" and data.data[-1] == "B":
        data = data.data[1:-1]
        data_list = [data[i:i + 4] for i in range(0, len(data), 4)]

        for i in data_list:
            value = int(i[1:4])
            if i[0] == '0':
                if i[1:4] < 255:
                    value = value
                else:
                    value = 255


            elif i[0] == '1':
                if i[1:4] < 255:
                    value = -value
                else:
                    value = -255
            arm_data = String()
            arm_data.data += str(value) + ' '

        arm_data.data = arm_data.data[:-1]
        arm_pub = rospy.Publisher('/position/robotic_arm', String, queue_size=10)

        arm_pub.publish(arm_data)





def listener():
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber("/serial/drive", String, drive_callback)
    rospy.Subscriber("/serial/robotic_arm", String, arm_callback)

    while not rospy.is_shutdown():
        pass


if _name_ == '_main_':
    listener()