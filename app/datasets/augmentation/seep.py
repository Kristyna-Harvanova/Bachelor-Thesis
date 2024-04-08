import cv2 as cv2
import numpy as np

def prepare_back_side(
        image: np.ndarray
) -> np.ndarray:
    """Blurs the image and rotates it along the y axis."""
    # Bluring the image.
    image = cv2.blur(image, (10, 10))

    # Rotation along the y axis => parameter 1, along the x axis => parameter 0
    image = cv2.flip(image, 1)

    return image

def layer_images(
        background: np.ndarray,
        foreground: np.ndarray,
        alpha: float = 0.2
) -> np.ndarray:
    """Layers two images on top of each other with a given alpha value for the foreground image."""

    # Cut the images to the same size.
    x_shape = min(background.shape[0], foreground.shape[0])
    y_shape = min(background.shape[1], foreground.shape[1])

    background = background[0:x_shape, 0:y_shape]
    foreground = foreground[0:x_shape, 0:y_shape]

    # Layer the images.
    beta = ( 1.0 - alpha )
    result = cv2.addWeighted(background, beta, foreground, alpha, 0.0)

    return result

def seep_image(
        seep_image: np.ndarray,
        background_image: np.ndarray,
        seep_level: float
) -> np.ndarray:
    """Seeps the backside into the background of the main image and returns one complete image."""  

    seep_image = prepare_back_side(seep_image)
    background = layer_images(background_image, seep_image, seep_level/3)

    return background
