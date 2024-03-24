import json
from svgelements import *
from ...Annotation import Annotation

def extract_annotations_from_workbench(
    from_path_svg: str, 
    to_path_json: str
):
    # Load the SVG file
    with open(from_path_svg) as svg_file:
        svg_file: SVG = SVG.parse(svg_file, reify=True)
    
    svg_info = {}
    annotation_bboxes = []
    
    # Extract the information from the SVG file
    for element in svg_file.elements():
        if type(element) is Image:
            width = round(float(element.values.get("width")))
            height = round(float(element.values.get("height")))

            svg_info["width"] = width
            svg_info["height"] = height
        
        elif type(element) is Group:
            cls = element.values.get("{http://www.inkscape.org/namespaces/inkscape}label")
            if cls not in Annotation.CLASSES: continue

            for child in element:
                if type(child) is not Rect: continue

                x = int(float(child.values.get("x")))
                y = int(float(child.values.get("y")))
                width = int(float(child.values.get("width")))
                height = int(float(child.values.get("height")))
                annotation_bbox = Annotation(cls, x, y, width, height)
                annotation_bboxes.append(annotation_bbox.to_json())
    
    svg_info["annotations"] = annotation_bboxes
    
    print("Parsed score:", from_path_svg)

    # Save the information to a JSON file
    with open(to_path_json, "w") as json_file:
        json.dump(svg_info, json_file, indent=4)
    