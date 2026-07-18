# test.py

import cv2
from camera import Camera
from hand import HandTracker
from gesture import Gesture

camera = Camera()
tracker = HandTracker()
gesture = Gesture()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    frame, landmarks = tracker.findHands(frame)

    if gesture.is_pinch(landmarks):
        cv2.putText(
            frame,
            "PINCH DETECTED",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Gesture Test", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

camera.release()
