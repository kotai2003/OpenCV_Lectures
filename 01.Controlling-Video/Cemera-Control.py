import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)

#frame rate
fps = cap.get(cv2.CAP_PROP_FPS)
print('fps value:', fps)

# width and heigt
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('(width, height)', w, h)

# Setting width and height (640, 480) -> (320,320)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

#time
prev_time = 0
current_time = 0

while True:
    ret, img = cap.read()

    #Measure FPS
    current_time = time.time()
    fps_m = 1 /(current_time - prev_time)
    prev_time = current_time
    print('fps measured', fps_m)


    cv2.imshow('Frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


