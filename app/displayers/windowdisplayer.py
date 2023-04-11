import cv2
import numpy as np


class WindowDisplayer:

    def display_image(self, title: str, img: np.ndarray):
        cv2.imshow(
            winname=title,
            mat=img
        )

    def wait(self, exit_button: str = 'q') -> None:
        if cv2.waitKey(0) == ord(exit_button):
            cv2.destroyAllWindows()
