from typing import List, Tuple

import cv2
import numpy as np


class AdaptiveThresholdAlgorithm:

    def find_pixels(self, img: np.ndarray, block_size: int, constant: int, n: int = 1) -> List[Tuple[int, int]]:
        """Perform adaptive thresholding

        Params:
            blockSize: The blockSize parameter should be chosen based on the size of the features in the image.
                Larger features require larger block sizes to capture their overall shape.
                Smaller features require smaller block sizes to capture their fine details.
                A good rule of thumb is to choose a blockSize that is roughly equal to the size of the smallest feature of interest.
            C: The C parameter controls the sensitivity of the thresholding.
                A higher C value will result in a more aggressive thresholding.
                A lower C value will result in a more lenient thresholding.
                A positive C value can be used to reduce noise in the resulting binary image.
                A negative C value can be used to highlight small features in the image.
        """
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(
            src=img,
            code=cv2.COLOR_BGR2GRAY
        )
        # Apply adaptive thresholding to create a binary image
        binary_img = cv2.adaptiveThreshold(
            src=gray_img,
            maxValue=255,
            adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # cv2.ADAPTIVE_THRESH_MEAN_C
            thresholdType=cv2.THRESH_BINARY,
            blockSize=block_size,
            C=constant
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
