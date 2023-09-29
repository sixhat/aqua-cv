# Decided to ask chatGPT how to do it...
# This is a simple color-based segmentation to identify possible obstacles. 

import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Use 0 for the default camera (usually the webcam)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Obstacle detection here
    # Define lower and upper bounds for the orange color
    lower_orange = np.array([0, 100, 100])
    upper_orange = np.array([20, 255, 255])
    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Create a mask for the orange color
    mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw bounding boxes around detected obstacles
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if (w * h > 1000):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame,  (x + w//2, y + h//2), 10, (255, 255, 0), 2)
    # End of obstacle detection
    
    
    cv2.imshow('Obstacle Avoidance', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
