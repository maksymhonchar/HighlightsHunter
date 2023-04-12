import os

from app.algorithms import AdaptiveThresholdAlgorithm
from app.displayers import CentroidsPainter, WindowDisplayer
from app.loaders import LocalStorageLoader
from app.writers import LocalStorageWriter


class AdaptiveThresholdCaseRunner:

    def __init__(self) -> None:
        self.loader = LocalStorageLoader()
        self.writer = LocalStorageWriter()
        self.algorithm = AdaptiveThresholdAlgorithm()
        self.painter = CentroidsPainter()
        self.displayer = WindowDisplayer()

    def run(self, data_dir_path: str, output_dir_path: str, n_pixels: int = 10) -> None:
        for img_name in os.listdir(data_dir_path):
            # load
            img_path = os.path.join(data_dir_path, img_name)
            img = self.loader.load_img(img_path)
            # find
            n_brightest_pixels = self.algorithm.find_pixels(
                img=img,
                block_size=5,
                constant=5,
                n=n_pixels
            )
            # paint
            img_with_circles_and_text = self.painter.paint(
                img=img,
                centroids=n_brightest_pixels
            )
            # write
            output_img_path = os.path.join(
                f'{img_name}_{type(self.algorithm).__name__}',
                output_dir_path
            )
            self.writer.save_img(output_img_path, img_with_circles_and_text)
            # display
            img_title = f"Image {img_path}"
            self.displayer.display_image(img_title, img_with_circles_and_text)
        # wait for user input
        self.displayer.wait()
