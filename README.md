# Eye Tracker using OpenCV

This project is an eye tracker application that uses OpenCV to detect and track eyes in real-time from a webcam feed.

## Features

- Real-time eye detection using Haar cascades.
- Eye tracking using the MOSSE tracker.
- Visual feedback with bounding boxes and labels for detected and tracked eyes.

## Requirements

- Python 3.x
- OpenCV 4.x

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Sonal-Dhomne/EyeTracker.git
    cd EyeTracker
    ```

2. **Install the required Python packages:**

    ```bash
    pip install opencv-python opencv-contrib-python
    ```

3. **Download the Haar cascade for eye detection:**

    Download the `haarcascade_eye.xml` file from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the project directory.

## Usage

1. **Run the eye tracker script:**

    ```bash
    python eye_tracker.py
    ```

2. **Controls:**

    - The application will start the webcam feed and begin detecting and tracking eyes.
    - Press `q` to exit the application.

## Code Explanation

The main parts of the script are:

1. **Loading the Haar Cascade for Eye Detection:**

    ```python
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    ```

2. **Initializing Object Trackers:**

    ```python
    trackers = [cv2.legacy.TrackerMOSSE_create() for _ in range(2)]
    ```

3. **Capturing Frames from the Webcam:**

    ```python
    cap = cv2.VideoCapture(0)
    ```

4. **Processing Each Frame:**

    - Converting to grayscale for eye detection.
    - Detecting eyes using the Haar cascade.
    - Tracking the first two detected eyes using the MOSSE tracker.
    - Drawing bounding boxes and labels on the frame for visual feedback.

5. **Displaying the Frame:**

    ```python
    cv2.imshow("Eye Tracking", frame)
    ```

6. **Releasing Resources on Exit:**

    ```python
    cap.release()
    cv2.destroyAllWindows()
    ```

## Acknowledgements

- [OpenCV](https://opencv.org/) for providing the computer vision library.
- [OpenCV GitHub repository](https://github.com/opencv/opencv) for the Haar cascades.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any inquiries or issues, please contact [Sonal Dhomne](mailto:sonaldhomne04work@gmail.com).
