# Real-time Object Detection with OpenCV and CVlib

This Python script performs real-time object detection using your webcam. It leverages the OpenCV (cv2) library for video capture and image processing, and the CVlib library for object detection.

## Prerequisites

Before running the script, ensure you have the following libraries installed:

* **OpenCV (cv2):**  Install using: `pip install opencv-python`
* **NumPy:** Install using: `pip install numpy` (likely already installed with OpenCV)
* **CVlib:** Install using: `pip install cvlib`

You may also need to install TensorFlow or other deep learning frameworks that CVlib depends on.  If you encounter errors related to missing dependencies, install them as needed.  A common issue is the `object_detection` package.  Try: `pip install object_detection`

## How to Run

1.  **Clone or download the repository:** If you have this code in a repository, clone it. Otherwise, save the Python code as a `.py` file (e.g., `object_detection.py`).
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute the script using: `python object_detection.py`

## Usage

Once the script is running, it will:

1.  **Capture video from your webcam:** The script will open a window displaying the feed from your default webcam.
2.  **Detect objects:** CVlib will detect common objects in each frame of the video.
3.  **Draw bounding boxes and labels:**  The detected objects will be highlighted with green bounding boxes.  Each box will include a label (e.g., "person", "car", "dog") and a confidence score (a number between 0 and 1 indicating how sure the model is about its prediction).
4.  **Display the results:** The processed frames with bounding boxes and labels will be shown in the "Object Detection" window.
5.  **Exit:** Press the 'q' key on your keyboard to close the window and stop the script.

## Code Explanation

*   `cv2.VideoCapture(0)`: Opens the default webcam (usually index 0).  Change the index if you have multiple cameras.
*   `cvlib.detect_common_objects(frame)`: This function performs the object detection.  It returns bounding boxes (`bbox`), labels (`label`), and confidence scores (`conf`).
*   The loop iterates through the detected objects, draws rectangles around them using `cv2.rectangle`, and adds text labels using `cv2.putText`.
*   `cv2.imshow("Object Detection", frame)`: Displays the processed frame in a window.
*   `cv2.waitKey(1) & 0xFF == ord('q')`: Checks for the 'q' key press to exit the loop.

## Troubleshooting

*   **Webcam issues:** If you encounter problems with the webcam, ensure it's properly connected and that you have the necessary drivers.  Try changing the `VideoCapture` index.
*   **Missing libraries:** Double-check that all required libraries are installed.  Refer to the installation instructions above.
*   **Performance:** Real-time object detection can be computationally intensive.  If you experience slow performance, try reducing the video resolution or using a more powerful computer.
*   **CUDA errors:** If you have a compatible NVIDIA GPU and CUDA installed, CVlib might try to use it. If you don't have CUDA set up correctly, you might get errors.  Try uninstalling TensorFlow and reinstalling it *without* GPU support to force CPU usage.  You can also try setting the `CUDA_VISIBLE_DEVICES` environment variable to an empty string.

## Further Development

*   **Custom object detection:** Train your own models to detect specific objects that are not included in the pre-trained CVlib model.
*   **Performance optimization:** Explore techniques to improve the speed of object detection.
*   **Integration with other applications:** Use the object detection results to trigger other actions or integrate with other systems.
