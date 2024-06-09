import cv2
from ultralytics import YOLO

# Load the custom-trained YOLOv8 model
model = YOLO("yolov8m_custom.pt")

# Initialize the webcam feed (use 0 for default webcam, or the appropriate index for external webcams)
camera_index = 0
cap = cv2.VideoCapture(camera_index)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print(f"Error: Could not open webcam {camera_index}")
    exit()

# Loop to capture frames from the webcam and perform detection
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # If the frame is read correctly, ret will be True
    if not ret:
        print("Error: Failed to capture image")
        break

    # Perform detection using the model
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the frame with detections
    cv2.imshow('YOLOv8 Live Detection', annotated_frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
