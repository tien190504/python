from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator

model = YOLO("yolov8s.pt")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


while True:
    _, img = cap.read()
    
    result = model.predict(img)
    
    for r in result:
        annotator = Annotator(img)
        
        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]
            c = box.cls
            annotator.box_label(b, model.names[int(c)])
            
    img = annotator.result()
    img_resized = cv2.resize(img, (960, 540))
    cv2.imshow('YOLO V8 Detection', img_resized)



    if cv2.waitKey(1) & 0xFF == ord(' ') or cv2.getWindowProperty('YOLO V8 Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
