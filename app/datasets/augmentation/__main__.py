import argparse
from pathlib import Path
import cv2
from PIL import Image
import numpy as np
from .BackgroundGenerator import BackgroundGenerator
from .augment import alpha2white, augment_with

from .seep import seep_image, layer_images, prepare_back_side   #TODO: smazat nepotrebne importy, udelat komentare 
from .handwriting_augmentation import augment
from .noise import kanungo

def main(take=None):
    # ### From alpha-black pictures to white-black pictures   # NOTE: 5174 trva cca 2,5 hodiny na aic
    # png_alpha_files = list(Path("yolo", "dataset", "images", "train_alpha").glob("*.png"))
    # TRANSPARENCY_THRESHOLD = 50  # For example, considering alpha values <= 10 as "transparent enough"
    # for i, png_file in enumerate(png_alpha_files):        
    #     print(f"{i}: {png_file}")
    #     output_image_path = png_file.parent.parent / "train_white" / (png_file.stem + ".png")   #TODO: regenerate to jpg?? ovlivni to datasety vzgenervane z train_white, ktere se delali z png?
    #     alpha2white(png_file, output_image_path, TRANSPARENCY_THRESHOLD)

    # ### Generate all possible backgrounds for MuseScore sheet size
    # path_to_download = Path("app", "datasets", "augmentation", "backgrounds", "samples.csv")
    # generator = BackgroundGenerator(path_to_download)
    path_to_background_dir = Path("app", "datasets", "augmentation", "backgrounds", "generated")
    # generator.generate_all(path_to_background_dir)

    ### File praparation for all types of augmentation.
    png_white_files = list(Path("yolo", "dataset", "images", "train_white").glob("*.png"))
    backgrounds = [background for background in path_to_background_dir.iterdir() if background.is_file()]
    # Randomly select 'take' files to make them in high quality
    if take is not None:
        png_white_files_array = np.array(png_white_files)
        chosen_indices = np.random.choice(len(png_white_files_array), take, replace=False)
        png_white_files = png_white_files_array[chosen_indices].tolist()

    # ### Augment adding everything                   # NOTE: 5175 trva cca 3,5 hodiny na aic
    # for i, png_file in enumerate(png_white_files):        
    #     print(f"{i}: {png_file}")
    #     output_image_path = png_file.parent.parent / "train_augm_all" / (png_file.stem + ".jpg")  #NOTE: saving as a .jpg file to save disk storage
    #     augment_with(png_file, output_image_path, backgrounds, png_white_files, take, handwriting=True, noise=True, seep=True, pattern=True)

    # ### Augment without pattern (background)      # NOTE: 5175 trva cca 3,2 hodiny na aic
    # for i, png_file in enumerate(png_white_files):        
    #     print(f"{i}: {png_file}")
    #     output_image_path = png_file.parent.parent / "train_without_back" / (png_file.stem + ".jpg")
    #     augment_with(png_file, output_image_path, backgrounds, png_white_files, take, handwriting=True, noise=True, seep=True, pattern=False)

    # ### Augment without kanungo noise             # NOTE: 5175 trva cca 2,2 hodiny na aic
    # for i, png_file in enumerate(png_white_files):        
    #     print(f"{i}: {png_file}")
    #     output_image_path = png_file.parent.parent / "train_without_kanungo" / (png_file.stem + ".jpg")
    #     augment_with(png_file, output_image_path, backgrounds, png_white_files, take, handwriting=True, noise=False, seep=True, pattern=True)

    # ### Augment without seep                      # NOTE: 5175 trva cca 2,5 hodiny na aic
    # for i, png_file in enumerate(png_white_files):        
    #     print(f"{i}: {png_file}")
    #     output_image_path = png_file.parent.parent / "train_without_seep" / (png_file.stem + ".jpg")
    #     augment_with(png_file, output_image_path, backgrounds, png_white_files, take, handwriting=True, noise=True, seep=False, pattern=True)

    # ### Augment without caligraphic handwriting   # NOTE: 5175 trva cca 2,85 hodiny na aic
    # for i, png_file in enumerate(png_white_files):        
    #     print(f"{i}: {png_file}")
    #     output_image_path = png_file.parent.parent / "train_without_caligraph" / (png_file.stem + ".jpg")
    #     augment_with(png_file, output_image_path, backgrounds, png_white_files, take, handwriting=False, noise=True, seep=True, pattern=True)
    

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('--take', type=int, help='Number of images to process in original quality.')

    # Parse arguments
    args = parser.parse_args()

    # Call your main function with the parsed arguments
    main(take=args.take)