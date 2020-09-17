#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys

from components.Kinect import Kinect

from time import sleep


def main(args):
    while True:
        depth_distance = Kinect.get_depth_distance()

        video = Kinect.get_video_frame()

        cv2.putText(
            video,
            "The current distance is: " + str(depth_distance) + " mts",
            (video.shape[1] - video.shape[1] + 10, video.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow('Video', video)

        # depth = Kinect.get_depth_frame()
        # cv2.imshow('Depth', depth)

        if cv2.waitKey(5) & 0xFF == 27:
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
