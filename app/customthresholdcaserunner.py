import os

from app.algorithms import CustomThresholdAlgorithm
from app.displayers import Painter, WindowDisplayer
from app.loaders import LocalStorageLoader
from app.writers import LocalStorageWriter


class CustomThresholdCaseRunner:

    def __init__(self) -> None:
        self.loader = LocalStorageLoader()
        self.writer = LocalStorageWriter()
        self.algorithm = CustomThresholdAlgorithm()
        self.painter = Painter()
        self.displayer = WindowDisplayer()

    def run(self, data_dir_path: str, output_dir_path: str, n_pixels: int = 10) -> None:
        for img_name in os.listdir(data_dir_path):
            # load
            img_path = os.path.join(data_dir_path, img_name)
            img = self.loader.load_img(img_path)
            # find
            n_brightest_pixels = self.algorithm.find_pixels(
                img=img,
                lower_threshold=240,
                upper_threshold=255,
                n=n_pixels
            )
            # paint
            img_with_circles = self.painter.paint_centroids(
                img=img,
                centroids=n_brightest_pixels
            )
            # write
            output_img_path = os.path.join(output_dir_path, img_name)
            self.writer.save_img(output_img_path, img_with_circles)
            # display
            img_title = f"Image {img_path}"
            self.displayer.display_image(img_title, img_with_circles)
        # wait for user input
        self.displayer.wait()
