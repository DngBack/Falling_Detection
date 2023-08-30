# import cv2
# cap = cv2.VideoCapture("http://28.63.96.104:8080/video")

# # Check if the camera is opened successfully
# if not cap.isOpened():
#     print("Cannot open camera")


# # Read the video frame by frame
# while True:
#     ret, frame = cap.read()
#     cv2.imshow("Frame", frame)

#     # Press 'q' to quit
#     if cv2.waitKey(1) == ord('q'):
#         break

# # Release the resources
# cap.release()
# cv2.destroyAllWindows()
import cv2

def process_video():
    # Create a video capture object
    cap = cv2.VideoCapture("http://28.63.96.104:8080/video")

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Cannot open camera")
        return

    # Read the video frame by frame
    while True:
        ret, frame = cap.read()
        if frame is None:
            print("Can not open camera")
        # Display the frame
        cv2.imshow("Frame", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the resources
    cap.release()

if __name__ == "__main__":
    process_video()