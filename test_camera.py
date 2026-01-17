import cv2
from picamera2 import Picamera2

# Initialize Picamera2
picam2 = Picamera2()

# Configure for OpenCV
config = picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
picam2.configure(config)

picam2.start()

print("Press 'q' to quit, 's' to save image")

while True:
    frame = picam2.capture_array()

    cv2.imshow("Camera Test", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if key == ord('s'):
        cv2.imwrite("capture.jpg", frame)
        print("Image saved as capture.jpg")

picam2.stop()
cv2.destroyAllWindows()
