import cv2

hand_cascade = cv2.CascadeClassifier('hand.xml')

def detect(gray, frame):
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    return frame

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()