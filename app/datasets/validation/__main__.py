# TODO: Uses same interface as `evaluation_dataset`. Code for this is in `app/datasets/evaluation`. 
# Udelat to takto - mit modul na validation a volat kod z evaluation modulu?

from pathlib import Path 
from ..evaluation.extract_annotations_from_workbench import extract_annotations_from_workbench
from ..evaluation.create_new_workbench import create_new_workbench  
# TODO: dotaz - jaka je konvence, nejdrim import cizich modulu, potom mych? nebo naopak?

def main():
    # Create new workbenches from the images
    path_images = Path("validation_dataset", "images")
    path_workbenches = Path("validation_dataset", "workbenches")
    for image_path in path_images.iterdir():
        create_new_workbench(
            str(image_path), 
            str(path_workbenches / (image_path.stem + ".svg"))
        )

    # Extract the annotations from the SVG files
    path_annotations = Path("validation_dataset", "annotations")
    for svg_path in path_workbenches.iterdir():
        extract_annotations_from_workbench(
            str(svg_path), 
            str(path_annotations / (svg_path.stem + ".json"))
        )

if __name__ == "__main__":
    main()