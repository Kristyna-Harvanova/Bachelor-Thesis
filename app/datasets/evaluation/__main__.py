from .extract_annotations_from_workbench import extract_annotations_from_workbench
from .create_new_workbench import create_new_workbench

def main():
    # Create new workbenches from the images
    create_new_workbench("evaluation_dataset\\images\\70fac7dd-90e8-4e7b-b12f-0b0c1ccbca00_130_287_1890_2571.jpg", "evaluation_dataset\\70fac7dd-90e8-4e7b-b12f-0b0c1ccbca00_130_287_1890_2571.svg")

    # Extract the annotations from the SVG files
    extract_annotations_from_workbench("evaluation_dataset\\70fac7dd-90e8-4e7b-b12f-0b0c1ccbca00_130_287_1890_2571.svg", "evaluation_dataset\\70fac7dd-90e8-4e7b-b12f-0b0c1ccbca00_130_287_1890_2571.json")
    
if __name__ == "__main__":
    main()