import cv2
import numpy as np


class LocalStorageWriter:

    def save_img(self, path: str, img: np.ndarray) -> None:
        cv2.imwrite(
            filename=path,
            img=img
        )
