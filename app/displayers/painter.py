from typing import List, Tuple

import cv2
import numpy as np


class CentroidsPainter:

    def paint(self, img: np.ndarray, centroids: List[Tuple[int, int]]) -> np.ndarray:
        img_with_circles = self._paint_circles(img, centroids)
        img_with_circles_and_text = self._paint_coords(img_with_circles, centroids)
        return img_with_circles_and_text

    def _paint_circles(self, img: np.ndarray, centroids: List[Tuple[int, int]]) -> np.ndarray:
        image_with_centroids = img.copy()
        for (cx, cy) in centroids:
            cv2.circle(
                img=image_with_centroids,
                center=(cx, cy),
                radius=3,
                color=(0, 0, 255),  # red
                thickness=-1
            )
        return image_with_centroids

    def _paint_coords(self, img: np.ndarray, centroids: List[Tuple[int, int]]) -> np.ndarray:
        image_with_centroids = img.copy()
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.25
        font_thickness = 1

        for (cx, cy) in centroids:
            text = f"({cx}, {cy})"
            text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
            text_x = cx - text_size[0] // 2
            text_y = cy - 5
            cv2.putText(
                img=image_with_centroids,
                text=text,
                org=(text_x, text_y),
                fontFace=font,
                fontScale=font_scale,
                color=(0, 0, 0),  # black
                thickness=font_thickness,
                lineType=cv2.LINE_AA
            )
        return image_with_centroids
