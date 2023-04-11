from typing import List, Tuple

import cv2
import numpy as np


class Painter:

    def paint_centroids(self, img: np.ndarray, centroids: List[Tuple[int, int]]) -> np.ndarray:
        image_with_centroids = img.copy()
        for (cx, cy) in centroids:
            cv2.circle(
                img=image_with_centroids,
                center=(cx, cy),
                radius=5,
                color=(0, 0, 255),
                thickness=-1
            )
        return image_with_centroids
