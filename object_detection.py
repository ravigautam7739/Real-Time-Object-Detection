import cv2
from ultralytics import YOLO

# Load YOLOv8 model (nano = fast, you can use 'yolov8s.pt' for better accuracy)
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame, conf=0.5)  # confidence threshold

    # Draw results
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()