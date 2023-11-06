# Decided to ask chatGPT how to do it...
# This is a simple color-based segmentation to identify possible obstacles. 

import cv2 as cv
import numpy as np

# cap = cv.VideoCapture(0)  # Use 0 for the default camera (usually the webcam)
cap = cv.VideoCapture("../media/2023-10-14 at 11.53.02.mp4")  # Use 0 for the default camera (usually the webcam)

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv.CAP_PROP_POS_MSEC, 0.0)
        continue
    
    # 0x87D1FF  - 135, 209, 255
    lower_aqua_blue = np.array([55,109,155])
    upper_aqua_blue = np.array([155,255, 255])
    # Convert the frame to the HSV color space
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # Create a mask for the orange color
    mask = cv.inRange(hsv_frame, lower_aqua_blue, upper_aqua_blue)
    # Find contours in the mask
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    cv.drawContours(frame, contours, -1, (0,255,0), 3)
    
    # Draw bounding boxes around detected obstacles
    # for contour in contours:
    #     x, y, w, h = cv.boundingRect(contour)
    #     if (w * h > 10_000):
    #         cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #         cv.circle(frame,  (x + w//2, y + h//2), 10, (255, 255, 0), 2)
    # # End of obstacle detection
    
    
    cv.imshow('Obstacle Avoidance', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
