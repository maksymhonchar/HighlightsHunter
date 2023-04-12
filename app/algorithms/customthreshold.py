from typing import List, Tuple

import cv2
import numpy as np


class CustomThresholdAlgorithm:

    def find_pixels(self, img: np.ndarray, lower_threshold: int, upper_threshold: int, n: int = 1) -> List[Tuple[int, int]]:
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(
            src=img,
            code=cv2.COLOR_BGR2GRAY
        )
        # Apply a threshold to create a binary image
        _, binary_img = cv2.threshold(
            src=gray_img,
            thresh=lower_threshold,
            maxval=upper_threshold,
            type=cv2.THRESH_BINARY
        )
        # Find contours in the binary image
        contours, _ = cv2.findContours(
            image=binary_img,
            mode=cv2.RETR_LIST,
            method=cv2.CHAIN_APPROX_SIMPLE
        )
        # Get top N largest contours
        contours = sorted(
            contours,
            key=cv2.contourArea,
            reverse=True
        )[:n]
        # Create list of centroids
        centroids: List[Tuple[int, int]] = []
        for contour in contours:
            M = cv2.moments(contour)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                centroids.append((cx, cy))
        # Return results
        return centroids
