from typing import List, Tuple

import cv2
import numpy as np


class DOGBlobAlgorithm:  # Difference of Gaussians (DoG) method

    def find_pixels(self, img: np.ndarray, threshold: int, min_area: float, max_area: float) -> List[Tuple[int, int]]:
        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Apply Difference of Gaussians (DoG) filter
        blur1 = cv2.GaussianBlur(gray, (5, 5), 0)
        blur2 = cv2.GaussianBlur(gray, (9, 9), 0)
        dog = cv2.absdiff(blur1, blur2)
        # Threshold the resulting image
        _, thresh = cv2.threshold(
            src=dog,
            thresh=threshold,
            maxval=255,
            type=cv2.THRESH_BINARY
        )
        # Find contours in the binary image
        contours, _ = cv2.findContours(
            image=thresh,
            mode=cv2.RETR_LIST,
            method=cv2.CHAIN_APPROX_SIMPLE
        )
        # Filter the contours based on size and shape
        blobs: List[Tuple[int, int]] = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if min_area <= area <= max_area:
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = float(w) / h
                circularity = 4 * np.pi * area / (w ** 2 + h ** 2)
                if 0.5 <= aspect_ratio <= 2 and 0.5 <= circularity <= 1:
                    blobs.append((x + w // 2, y + h // 2))
        # Return the list of blob centroids
        return blobs
