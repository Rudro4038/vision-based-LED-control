import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Finger tip landmark IDs
TIP_IDS = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    # Mirror the image
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    finger_count = 0

    if results.multi_hand_landmarks:

        hand_landmarks = results.multi_hand_landmarks[0]
        handedness = results.multi_handedness[0].classification[0].label

        mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )

        landmarks = hand_landmarks.landmark

        fingers = []

        # Thumb
        if handedness == "Right":
            fingers.append(
                landmarks[TIP_IDS[0]].x < landmarks[TIP_IDS[0]-1].x
            )
        else:
            fingers.append(
                landmarks[TIP_IDS[0]].x > landmarks[TIP_IDS[0]-1].x
            )

        # Other four fingers
        for tip in TIP_IDS[1:]:
            fingers.append(
                landmarks[tip].y < landmarks[tip-2].y
            )

        finger_count = sum(fingers)

        cv2.putText(
            frame,
            f"Hand: {handedness}",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2,
        )

    cv2.putText(
        frame,
        f"Fingers: {finger_count}",
        (10, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 0),
        3,
    )

    cv2.imshow("Vision-Based Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()