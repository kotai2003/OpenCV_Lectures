import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)

# frame rate
fps = cap.get(cv2.CAP_PROP_FPS)
print('fps value:', fps)

# width and height
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('(width, height)', w, h)

# setting width and height
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(0.5 * h))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(0.5 * w))
# cap.set(cv2.CAP_PROP_FPS, 30)

# time
prev_time = 0
current_time = 0

while True:
    ret, img = cap.read()

    #frame rate
    current_time = time.time()
    fps_meas = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(img, str(int(fps_meas)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)


    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
