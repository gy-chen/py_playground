import cv2

def capture_video():
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def capture_frame():
    cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cap.read()
    except KeyboardInterrupt:
        return ret, frame
    finally:
        cap.release()

if __name__ == '__main__':
    #capture_video()
    ret, frame = capture_frame()
