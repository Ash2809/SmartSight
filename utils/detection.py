import torch
from ultralytics import YOLO
import cv2
# from utils.detection import ObjectDetector

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        print(f"[INFO] Using device: {self.device}")
        
        # Load YOLOv8 model
        self.model = YOLO(model_path)
        self.model.to(self.device)
        print(f"[INFO] Model loaded from {model_path}")
    
    def detect(self, frame, conf=0.75):

        results = self.model(frame, conf=conf)
        
        detected_objects = [self.model.names[int(box.cls)] for box in results[0].boxes]
        annotated_frame = results[0].plot()
        
        return detected_objects, annotated_frame

if __name__ == "__main__":
    detector = ObjectDetector(model_path=r"C:\Advance_Projects\SmartSight\models\yolov8m.pt")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detected_objects, annotated_frame = detector.detect(frame)
        print("Detected:", detected_objects)

        cv2.imshow("VisionAI Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
