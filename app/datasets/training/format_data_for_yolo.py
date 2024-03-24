import json
from pathlib import Path
from ...Annotation import Annotation

def compute_bbox(
    x_left: int, 
    y_up: int, 
    width: int, 
    height: int,
    img_width: int,
    img_height: int
) -> tuple[float, float, float, float]:
    """
    Compute the bounding box coordinates for YOLO format.
    """
    x_center = x_left + width // 2
    y_center = y_up + height // 2

    # Normalize the coordinates
    x_center = x_center / img_width
    y_center = y_center / img_height
    width = width / img_width
    height = height / img_height

    return x_center, y_center, width, height

def json_to_yolo_format(
    json_path: Path,
    output_dir: Path,
):
    """
    Convert the JSON annotations to YOLO format.
    """
    # Read the JSON file
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Extract the image dimensions
    img_width = data['width']
    img_height = data['height']

    # Create the output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create the output file
    output_path = output_dir / f"{json_path.stem}.txt"
    with open(output_path, 'w') as file:
        # Extract the information for each annotation
        for annotation in data['annotations']:
            cls = annotation['class']
            x_left = annotation['x']
            y_up = annotation['y']
            width = annotation['width']
            height = annotation['height']

            # Convert the data to YOLO format
            cls = Annotation.CLASSES.index(cls)
            x_center, y_center, width, height = compute_bbox(
                x_left, y_up, width, height, img_width, img_height
            )

            file.write(f"{cls} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
