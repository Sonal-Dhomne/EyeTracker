import cv2

# Load pre-trained eye detection model
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Initialize object tracker for each eye
trackers = [cv2.legacy.TrackerMOSSE_create() for _ in range(2)]

# Open camera
cap = cv2.VideoCapture(0)

while True:
    # Read frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the frame
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Track the first detected eyes (up to two)
    for i, (x, y, w, h) in enumerate(eyes[:2]):
        bbox = (x, y, w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Change marker color to yellow
        cv2.putText(frame, f'Eye {i+1}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)  # Change text color to yellow
        success, bbox = trackers[i].update(frame)

        if success:
            # Tracking successful, draw bounding box
            x, y, w, h = [int(j) for j in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Change border color to yellow
            cv2.putText(frame, 'Tracked', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)  # Change text color to yellow
        
    # Display frame
    cv2.imshow("Eye Tracking", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
