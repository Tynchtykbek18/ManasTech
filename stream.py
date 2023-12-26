import cv2

rtmp_url = 'rtmp://10.42.0.1:1935/live/1'

cap = cv2.VideoCapture(rtmp_url)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Ваш код обработки кадра, если необходимо

    cv2.imshow('RTMP Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
