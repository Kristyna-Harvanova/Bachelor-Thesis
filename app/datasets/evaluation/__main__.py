from .extract_annotations_from_workbench import extract_annotations_from_workbench
from .create_new_workbench import create_new_workbench
from pathlib import Path    #TODO: vsude opravit na cestu nezavislou na OS - hotovo skoro vsude
#TODO: predelat os.neco na Path.neco viz Discord - hotovo skoro vsude

def main():
    # Create new workbenches from the images
    path_images = Path("evaluation_dataset", "images")
    path_workbenches = Path("evaluation_dataset", "workbenches")
    for image_path in path_images.iterdir():
        create_new_workbench(
            str(image_path), 
            str(path_workbenches / (image_path.stem + ".svg"))
        )

    # Extract the annotations from the SVG files
    path_annotations = Path("evaluation_dataset", "annotations")
    for svg_path in path_workbenches.iterdir():
        extract_annotations_from_workbench(
            str(svg_path), 
            str(path_annotations / (svg_path.stem + ".json"))
        )

if __name__ == "__main__":
    main()