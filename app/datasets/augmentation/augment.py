from pathlib import Path
import cv2
from PIL import Image
import numpy as np
from .seep import seep_image
from .handwriting_augmentation import augment
from .noise import kanungo

def alpha2white(
    png_file: Path,
    output_image_path: Path,
    transparency_treshold: int
):
    img = Image.open(str(png_file)).convert("RGBA")  # Ensure the image is in RGBA mode
    data = np.array(img)  

    # Binary mask where true indicates pixels that should turn black
    black_mask = data[..., 3] >= transparency_treshold

    binarized_data = np.ones_like(data) * 255  # Make everything white
    binarized_data[black_mask, :3] = 0  # Set RGB to black, alpha stays 255 (fully opaque)

    # Create a new image from the binarized data
    Image.fromarray(binarized_data[..., :3], mode="RGB").save(str(output_image_path))


def augment_with(
    png_file: Path,
    output_image_path: Path,
    backgrounds: list[Path],
    seep_images: list[Path],
    take: int,
    handwriting=True,
    noise=True,
    seep=True,
    pattern=True
):
    # Load the image
    image = cv2.imread(str(png_file))
    height, width = image.shape[:2]

    ## Add handwritten style
    if handwriting:
        image = augment(image, np.random.choice([-1, 1]))

    ## Add kanungo noise
    if noise:
        image = kanungo(image)

    ## Prepare background
    if pattern:
        # Chose the background image
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
    else:
        background_cropped = np.full((height, width, 3), 255, dtype=np.uint8)

    ## Add seep
    if seep:
        # Chose image to seep
        seep_height, seep_width, tried = 0, 0, 0
        while (seep_height != height or seep_width != width):
            seeped_image = cv2.imread(str(seep_images[np.random.randint(0, len(seep_images))]))
            seep_height, seep_width = seeped_image.shape[:2]
            tried += 1
            if tried > 10:
                seeped_image = image
                seep_height, seep_width = seeped_image.shape[:2]
                break

        # Chose intensity of a seep
        seep_level = np.random.random_sample() # Return float in the interval 0.0, 1.0, the smaller number, the less seep
        background_cropped = seep_image(seeped_image, background_cropped, seep_level)#, image)

    ## Add image to the seeped background
    if seep or pattern:
        # Mask for white pixels (the image is purely black (0) and white (255))
        mask = image[:, :, 0] == 255 

        # Create a 3-channel mask for color image replacement
        mask_3d = np.stack([mask]*3, axis=-1)

        # Use the mask to replace white pixels in the existing image with pixels from the background image
        image = np.where(mask_3d, background_cropped, image)

    # Resizing image to similar proportions
    if take is None:
        target_width = 1000
        target_height = int(height * target_width / width)
        image = cv2.resize(image, (target_width, target_height))

    # Save the merged image
    cv2.imwrite(str(output_image_path), image)
    print(f"Done: {output_image_path}")