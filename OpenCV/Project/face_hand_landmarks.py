import cv2
import time
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
face_detection = mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.5)
hands = mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
while cap.isOpened():
    success,image = cap.read()
    if not success:
        print('Ignore empty camera')
    image.flags.writeable = False
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)
    results_hands = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image,detection)
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image,
                                      hand_landmarks,
                                      mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())


    cv2.imshow('MediaPipe Face Detection', cv2.flip(image,1))
    if cv2.waitKey(5) & 0XFF == ord('q'):
        break
cap.release()