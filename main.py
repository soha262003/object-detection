import cv2
import numpy as np
import cvlib

cap = cv2.VideoCapture(0) 
while True:
    ret, frame = cap.read()  

    if not ret:
        print("Error: Could not read a frame from the webcam.")
        break

 
    bbox, label, conf = cvlib.detect_common_objects(frame)

    for i in range(len(bbox)):
        x, y, w, h = bbox[i]
        text = f"{label[i]}: {conf[i]:.2f}"
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
