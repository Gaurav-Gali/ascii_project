# Imports
from ascii_magic import AsciiArt
import cv2
import os

# Ascii Conversions


class ASCII:
    ascii_art = None

    def __init__(self, src_img):
        self.ascii_art = AsciiArt.from_image(src_img)

    def show_img(self, columns=50):
        self.ascii_art.to_terminal(columns=columns)
        print()


class Capture:
    capture = None

    def __init__(self, cam_no=0):
        self.capture = cv2.VideoCapture(cam_no)

    def show_feed(self):
        while True:
            ret, frame = self.capture.read()

            if not ret:
                continue

            if not os.path.exists("frames"):
                os.makedirs("frames")
            frame_path = "frames/frame.png"

            cv2.imwrite(frame_path, frame)
            ASCII(frame_path).show_img(150)

            if cv2.waitKey(1) == ord("q"):
                break

        self.capture.release()
        cv2.destroyAllWindows()


c = Capture()
c.show_feed()
