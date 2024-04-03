from pathlib import Path
import cv2
from .BackgroundGenerator import BackgroundGenerator
from .seep import seep_image, layer_images, prepare_back_side
from .handwriting_augmentation import augment
from PIL import Image
import numpy as np

def main():
    ### From alpha and black pictures to white and black pictures
    png_files = list(Path("yolo", "dataset", "images", "train_20_back").glob("*.png"))
    #png_files = list(Path("yolo", "dataset", "images", "val").glob("*.png"))
    
    TRANSPARENCY_THRESHOLD = 50  # For example, consider alpha values <= 10 as "transparent enough"

    # for i, png_file in enumerate(png_files):        
    #     print(f"{i}: {png_file}")
    #     img = Image.open(str(png_file)).convert("RGBA")  # Ensure the image is in RGBA mode
    #     data = np.array(img)  

    #     # Binary mask where true indicates pixels that should turn black
    #     black_mask = data[..., 3] >= TRANSPARENCY_THRESHOLD

    #     binarized_data = np.ones_like(data) * 255  # Make everything white
    #     binarized_data[black_mask, :3] = 0  # Set RGB to black, alpha stays 255 (fully opaque)

    #     # Create a new image from the binarized data
    #     Image.fromarray(binarized_data[..., :3], mode="RGB").save(str(png_file))


    ### Generate all possible backgrounds for MuseScore sheet size
    path_to_download = Path("app", "datasets", "augmentation", "backgrounds", "samples.csv")
    generator = BackgroundGenerator(path_to_download)

    path_to_background_dir = Path("app", "datasets", "augmentation", "backgrounds", "generated")
    #TODO: Common je docela i 3060, 3960. Predgenerovat taky?? - udelat velike, pak vyriznout pro dany rozmer - pro kazdy vzorek vice vygenerovanych nebo z 5000x5000 rezat nahodne
    COMMON_WIDTH, COMMON_HEIGHT = 2977, 4208
    # generator.generate_all(COMMON_WIDTH, COMMON_HEIGHT, path_to_background_dir)



    ### Merge background with sheet
    backgrounds = [background for background in path_to_background_dir.iterdir() if background.is_file()]

    # for i, existing_image_path in enumerate(png_files):        
    #     print(f"{i}: {existing_image_path}")

    #     # Load the existing images
    #     existing_image = cv2.imread(str(existing_image_path))
    #     height, width = existing_image.shape[:2]
    #     print(width, height)    # TODO: remove after deciding if predgenerovat or not

    #     if width == COMMON_WIDTH and height == COMMON_HEIGHT:
    #         back_img = cv2.imread(str(backgrounds[np.random.randint(0, len(backgrounds))]))
    #     else:
    #         back_img = generator.generate(width, height)

    #     # Mask for white pixels (the image is purely black (0) and white (255))
    #     mask = existing_image[:, :, 0] == 255 

    #     # Create a 3-channel mask for color image replacement
    #     mask_3d = np.stack([mask]*3, axis=-1)

    #     # Use the mask to replace white pixels in the existing image with pixels from the background image
    #     merged_image = np.where(mask_3d, back_img, existing_image)

    #     # Save the merged image
    #     merged_image_path = existing_image_path.parent / "with_back2" / (existing_image_path.stem + "_with_back2.png")
    #     cv2.imwrite(str(merged_image_path), merged_image)
    #     print(f"Merged into: {merged_image_path}")

    

    ### Launching the seep:
    # test_path_from = Path("yolo", "dataset", "images", "train_20_back", "lc4919673-4.png")
    # test_path_to = test_path_from.parent / "with_seep" / (test_path_from.stem + "_with_seep.png")

    # back_side = cv2.imread(str(test_path_from))
    # #TODO: Udelat tedy i bez pridaneho pozadi jen ciste prosak na bile.
    # height, width = back_side.shape[:2]
    # if width == COMMON_WIDTH and height == COMMON_HEIGHT:
    #     backgroung_from_quilt = cv2.imread(str(backgrounds[np.random.randint(0, len(backgrounds))]))
    # else:
    #     backgroung_from_quilt = generator.generate(width, height)

    # front_side = cv2.imread(str(test_path_from))
    #TODO: mira prosaku - 0-1
    # seeped_image = seep_image(back_side, backgroung_from_quilt, front_side)
    # cv2.imwrite(str(test_path_to), seeped_image)
    # print(f"Seeped: {test_path_to}")




    ### Launching the augmentation of handwritting:
    # # test_path_from = Path("yolo", "dataset", "images", "train_20_back", "with_seep", "lc4919673-4_with_seep.png")   #NOTE: 
    # # test_path_to = test_path_from.parent.parent / "with_handwriting" / (test_path_from.stem + "_with_handwriting.png")
    # test_path_from = Path("yolo", "dataset", "images", "train_20_back", "lc4919673-4.png")
    # test_path_to = test_path_from.parent / "with_handwriting" / (test_path_from.stem + "_with_handwriting.png")

    # image = cv2.imread(str(test_path_from))
    # image = augment(image, -1)    # TODO: random vybirat (-pi; pi)
    # cv2.imwrite(str(test_path_to), image)
    # print(f"Handwritten: {test_path_to}")


    ### Kanungo: TODO

if __name__ == "__main__":
    main()