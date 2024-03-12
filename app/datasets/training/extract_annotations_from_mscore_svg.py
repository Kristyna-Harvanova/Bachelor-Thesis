from svgelements import *
import json
from ...Annotation import Annotation

def extract_annotations_from_mscore_svg(
    from_path_svg: str, 
    to_path_json: str
):
    
    print(to_path_json)
    # Load the SVG file
    with open(from_path_svg) as svg_file:
        svg_file: SVG = SVG.parse(svg_file, reify=True)
    
    svg_info = {}
    annotation_bboxes = []
    
    wanted_classes = ["Note", "StaffLine", "BarLine"] #TODO: nejen Path, ale i PolyLine

    notes = []
    staff_lines = []
    bar_lines = []

    # Extract the information from the SVG file
    for element in svg_file.elements():
        if type(element) is SVG:
            width = round(float(element.values.get("width").replace("px", "")))
            height = round(float(element.values.get("height").replace("px", "")))

            svg_info["width"] = width
            svg_info["height"] = height
        
        elif type(element) is Path or type(element) is Polyline:
            cls = element.values.get('class', '')
            if cls not in wanted_classes: continue  

            # if cls = neco:
            #     notes.append(element)
            # elif 
            # elif
            #     #TODO

            # bbox = element.bbox()
            # #annotation_bbox = Annotation(cls, bbox.x, bbox.y, bbox.width, bbox.height)
            # x, y, width, height = bbox
            # annotation_bbox = Annotation(cls, int(x), int(y), int(width), int(height))
            # annotation_bboxes.append(annotation_bbox.to_json())
    
    #projit ty 3 pole a 
            # pro Notes udelat bbox viz vyse
            # pro staff_lines vytvorit funkci, ktera z 5 lines udaela jednu staff s info pro bbox
            # pro bar_lines vzit si staff a rozdelit ji barline a vutvorit bbox






    svg_info["annotations"] = annotation_bboxes
    
    print("Parsed score:", from_path_svg)

    # Save the information to a JSON file
    with open(to_path_json, "w") as json_file:
        json.dump(svg_info, json_file, indent=4)
    