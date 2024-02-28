import os
from .extract_annotations_from_workbench import extract_annotations_from_workbench
from .create_new_workbench import create_new_workbench

def main():
    # Create new workbenches from the images
    for image_path in os.listdir("evaluation_dataset\\images"):
        create_new_workbench("evaluation_dataset\\images\\" + image_path, "evaluation_dataset\\workbenches\\" + image_path.replace(".png", ".svg").replace(".jpg", ".svg"))

    # Extract the annotations from the SVG files
    for svg_path in os.listdir("evaluation_dataset\\workbenches"):
        extract_annotations_from_workbench("evaluation_dataset\\workbenches\\" + svg_path, "evaluation_dataset\\annotations\\" + svg_path.replace(".svg", ".json"))
    
if __name__ == "__main__":
    main()