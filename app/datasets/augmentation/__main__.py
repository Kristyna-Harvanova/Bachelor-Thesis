from pathlib import Path
import cv2
from PIL import Image
import numpy as np
from .BackgroundGenerator import BackgroundGenerator
from .seep import seep_image, layer_images, prepare_back_side
from .handwriting_augmentation import augment
from .noise import kanungo

def main():
    ### From alpha and black pictures to white and black pictures   # NOTE: 5174 trva cca 2,5 hodiny na aic
    # png_alpha_files = list(Path("yolo", "dataset", "images", "train_alpha").glob("*.png"))
    
    # TRANSPARENCY_THRESHOLD = 50  # For example, considering alpha values <= 10 as "transparent enough"

    # for i, png_file in enumerate(png_alpha_files):        
    #     print(f"{i}: {png_file}")
    #     img = Image.open(str(png_file)).convert("RGBA")  # Ensure the image is in RGBA mode
    #     data = np.array(img)  

    #     # Binary mask where true indicates pixels that should turn black
    #     black_mask = data[..., 3] >= TRANSPARENCY_THRESHOLD

    #     binarized_data = np.ones_like(data) * 255  # Make everything white
    #     binarized_data[black_mask, :3] = 0  # Set RGB to black, alpha stays 255 (fully opaque)

    #     # Create a new image from the binarized data
    #     dest_path = png_file.parent.parent / "train_white" / (png_file.stem + ".png")
    #     Image.fromarray(binarized_data[..., :3], mode="RGB").save(str(dest_path))


    ### Generate all possible backgrounds for MuseScore sheet size
    # path_to_download = Path("app", "datasets", "augmentation", "backgrounds", "samples.csv")
    # generator = BackgroundGenerator(path_to_download)

    path_to_background_dir = Path("app", "datasets", "augmentation", "backgrounds", "generated")
    # generator.generate_all(path_to_background_dir)



    # 1767: yolo/dataset/images/train_white/lc6023075-6.png
    # Done: yolo/dataset/images/train_augm_all/lc6023075-6.png
    # 1768: yolo/dataset/images/train_white/lc5866060-05.png
    # Done: yolo/dataset/images/train_augm_all/lc5866060-05.png
    # 1769: yolo/dataset/images/train_white/lc6249298-2.png
    # Done: yolo/dataset/images/train_augm_all/lc6249298-2.png
    # 1770: yolo/dataset/images/train_white/lc6993176-6.png
    # Done: yolo/dataset/images/train_augm_all/lc6993176-6.png
    # 1771: yolo/dataset/images/train_white/lc5725144-1.png
    # libpng error: Write Error


    png_white_files = list(Path("yolo", "dataset", "images", "train_white").glob("*.png"))

    ### Augment everything          # NOTE: 5174 trva cca xx hodiny na aic
    backgrounds = [background for background in path_to_background_dir.iterdir() if background.is_file()]

    for i, png_file in enumerate(png_white_files[1770:]):        
        print(f"{i}: {png_file}")

        # Load the image
        image = cv2.imread(str(png_file))
        height, width = image.shape[:2]

        ## Add handwritten style
        image = augment(image, np.random.choice([-1, 1]))

        ## Add kanungo noise
        image = kanungo(image)
        
        background = cv2.imread(str(backgrounds[np.random.randint(0, len(backgrounds))]))
        back_height, back_width = background.shape[:2]

        # Ensure the background is larger than the crop size
        if back_width >= width and back_height >= height:
            # Randomly choose the top-left corner of the cropping area
            x_start = np.random.randint(0, back_width - width + 1)
            y_start = np.random.randint(0, back_height - height + 1)
            # Crop the background
            background_cropped = background[y_start:y_start+height, x_start:x_start+width]
        else:
            raise ValueError(f"Background image is smaller than the desired crop size. Image size is {width} and {height}.")

        ## Add seep to background
        # Chose image to seep
        seep_height, seep_width, tried = 0, 0, 0
        while (seep_height != height or seep_width != width):
            seeped_image = cv2.imread(str(png_white_files[np.random.randint(0, len(png_white_files))]))
            seep_height, seep_width = seeped_image.shape[:2]
            tried += 1
            if tried > 10:
                seeped_image = image
                seep_height, seep_width = seeped_image.shape[:2]
                break

        # Chose intensity of a seep
        seep_level = np.random.random_sample() # Return float in the interval 0.0, 1.0, the smaller number, the less seep
        background_cropped = seep_image(seeped_image, background_cropped, seep_level)#, image)

        ## Add background
        # Mask for white pixels (the image is purely black (0) and white (255))
        mask = image[:, :, 0] == 255 

        # Create a 3-channel mask for color image replacement
        mask_3d = np.stack([mask]*3, axis=-1)

        # Use the mask to replace white pixels in the existing image with pixels from the background image
        merged_image = np.where(mask_3d, background_cropped, image)

        # Save the merged image
        merged_image_path = png_file.parent.parent / "train_augm_all" / (png_file.stem + ".png")
        cv2.imwrite(str(merged_image_path), merged_image)
        print(f"Done: {merged_image_path}")





    ### Merge background with sheet
    # backgrounds = [background for background in path_to_background_dir.iterdir() if background.is_file()]

    # for i, existing_image_path in enumerate(png_white_files):        
    #     print(f"{i}: {existing_image_path}")

    #     # Load the existing images
    #     existing_image = cv2.imread(str(existing_image_path))
    #     height, width = existing_image.shape[:2]
        
    #     back_img = cv2.imread(str(backgrounds[np.random.randint(0, len(backgrounds))]))
    #     back_height, back_width = back_img.shape[:2]

    #     # Ensure the background is larger than the crop size
    #     if back_width >= width and back_height >= height:
    #         # Randomly choose the top-left corner of the cropping area
    #         x_start = np.random.randint(0, back_width - width + 1)
    #         y_start = np.random.randint(0, back_height - height + 1)
    #         # Crop the background
    #         back_img_cropped = back_img[y_start:y_start+height, x_start:x_start+width]
    #     else:
    #         raise ValueError(f"Background image is smaller than the desired crop size. Image size is {width} and {height}.")

    #     # Mask for white pixels (the image is purely black (0) and white (255))
    #     mask = existing_image[:, :, 0] == 255 

    #     # Create a 3-channel mask for color image replacement
    #     mask_3d = np.stack([mask]*3, axis=-1)

    #     # Use the mask to replace white pixels in the existing image with pixels from the background image
    #     merged_image = np.where(mask_3d, back_img_cropped, existing_image)

    #     # Save the merged image
    #     merged_image_path = existing_image_path.parent / "with_back_final" / (existing_image_path.stem + "_with_back_final.png")
    #     cv2.imwrite(str(merged_image_path), merged_image)
    #     print(f"Merged into: {merged_image_path}")

    

    ### Launching the seep:
    # test_path_from = Path("yolo", "dataset", "images", "train_20_back", "lc4919673-4.png")
    # test_path_to = test_path_from.parent / "with_seep" / (test_path_from.stem + "_with_seep.png")

    # back_side = cv2.imread(str(test_path_from))
    # height, width = back_side.shape[:2]
    # if width == COMMON_WIDTH and height == COMMON_HEIGHT:
    #     backgroung_from_quilt = cv2.imread(str(backgrounds[np.random.randint(0, len(backgrounds))]))
    # else:
    #     backgroung_from_quilt = generator.generate(width, height)

    # front_side = cv2.imread(str(test_path_from))
    # seeped_image = seep_image(back_side, backgroung_from_quilt, front_side)
    # cv2.imwrite(str(test_path_to), seeped_image)
    # print(f"Seeped: {test_path_to}")




    ### Launching the augmentation of handwritting:
    # # test_path_from = Path("yolo", "dataset", "images", "train_20_back", "with_seep", "lc4919673-4_with_seep.png")   #NOTE: 
    # # test_path_to = test_path_from.parent.parent / "with_handwriting" / (test_path_from.stem + "_with_handwriting.png")
    # test_path_from = Path("yolo", "dataset", "images", "train_20_back", "lc4919673-4.png")
    # test_path_to = test_path_from.parent / "with_handwriting" / (test_path_from.stem + "_with_handwriting.png")

    # image = cv2.imread(str(test_path_from))
    # image = augment(image, -1) 
    # cv2.imwrite(str(test_path_to), image)
    # print(f"Handwritten: {test_path_to}")


    ### Launching the noise operations:
    # test_path_from = Path("yolo", "dataset", "images", "train_20_back", "lc4919673-4.png")
    # test_path_to = test_path_from.parent / "with_kanungo" / (test_path_from.stem + "_with_kanungo.png")

    # image = cv2.imread(str(test_path_from))
    # image = kanungo(image)
    # cv2.imwrite(str(test_path_to), image)
    # print(f"Kanungo: {test_path_to}")



if __name__ == "__main__":
    main()