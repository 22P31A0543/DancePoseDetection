import cv2 as cv
import mediapipe as mp
import time
import numpy as np


class PoseDetectori:
    def __init__(self, mode=False, smooth=True, detectionCon=0.7, trackCon=0.5):
        self.mode = mode
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode,
                                     smooth_landmarks=self.smooth,
                                     min_detection_confidence=self.detectionCon,
                                     min_tracking_confidence=self.trackCon)

    def findPose(self, img,img1, draw=True):
        imgRGB = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks and draw:
            landmark_spec = mp.solutions.drawing_utils.DrawingSpec(color=(255,0,0), thickness=1, circle_radius=0)
            connection_spec = mp.solutions.drawing_utils.DrawingSpec(color=(255,0,0), thickness=10)
            self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS,landmark_spec,connection_spec)
        return img

    def findPosition(self, img, draw=True):
        lmlist = []
        if self.results.pose_landmarks:
            h, w, _ = img.shape
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append((cx, cy))
                # if draw:
                #     cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED)
        return lmlist


    def create_pose_mask(img, landmarks, radius=30):
        mask = np.zeros(img[:2], dtype=np.uint8)
        for (x, y) in landmarks:
            cv.circle(mask, (x, y), radius, 255, -1)
        return mask














    

        
    
