#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import freenect
import math
import numpy as np


class Kinect:

    @staticmethod
    def get_depth_distance():
        depth, timestamp = freenect.sync_get_depth()

        height, width = depth.shape

        x = int(math.floor(height / 2))
        y = int(math.floor(width / 2))

        depth_center = depth[x][y]

        distance = 0

        if depth_center <= 2047:
            distance = "{0:.2f}".format(
                0.1236 * math.tan(depth_center / 2842.5 + 1.1863))

        return distance

    @staticmethod
    def get_depth_frame():
        depth, timestamp = freenect.sync_get_depth()

        depth = depth.astype(np.uint8)

        return depth

    @staticmethod
    def get_video_frame():
        video, timestamp = freenect.sync_get_video()

        video = cv2.cvtColor(video, cv2.COLOR_RGB2BGR)

        return video
