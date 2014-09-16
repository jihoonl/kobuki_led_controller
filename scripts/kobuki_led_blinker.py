#!/usr/bin/env python

import rospy
import kobuki_utils

if __name__ == '__main__':
    blinker = kobuki_utils.LedBlinker()
    blinker.loginfo('Initialized')
    blinker.spin()
    blinker.loginfo('Bye Bye')
