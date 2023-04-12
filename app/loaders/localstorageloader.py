import os

import cv2
import numpy as np

from app.loaders.exceptions import InvalidFileFormatError


class LocalStorageLoader:

    def load_img(self, path: str) -> np.ndarray:
        if not os.path.exists(path):
            error_msg = f"File {path=} does not exist."
            raise FileNotFoundError(error_msg)

        valid_formats = ('.jpg', '.jpeg', '.png')
        if not path.lower().endswith(valid_formats):
            error_msg = f"Invalid file format for {path=}. Only JPG, JPEG, PNG files are allowed."
            raise InvalidFileFormatError(error_msg)

        img = cv2.imread(
            filename=path,
            flags=cv2.IMREAD_COLOR
        )
        return img
