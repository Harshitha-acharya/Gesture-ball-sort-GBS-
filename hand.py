import cv2
import mediapipe as mp

class HandTracker:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils

    def findHands(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        landmarks = []

        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

                self.drawer.draw_landmarks(
                    frame,
                    hand,
                    self.mpHands.HAND_CONNECTIONS
                )

                h, w, c = frame.shape

                for idx, lm in enumerate(hand.landmark):

                    x = int(lm.x * w)
                    y = int(lm.y * h)

                    landmarks.append((idx, x, y))

        return frame, landmarks

    def getFingerPosition(self, landmarks, finger_id=8):

        if len(landmarks) == 0:
            return None

        for point in landmarks:

            if point[0] == finger_id:
                return (point[1], point[2])

        return None