import os
from svgelements import *
import json

def save2json(svg_path, cls = "Note"):
    
    # Load the SVG file
    svg_file_path = os.path.join("data", "svg_files", svg_path)

    with open(svg_file_path) as svg_file:
        svg_file: SVG = SVG.parse(svg_file, reify=True)
    
    svg_info = {}

    annotation_bboxes = []
    
    # Extract the information from the SVG file
    for element in svg_file.elements():
        if type(element) is Image:
            #page = imslp_pages.get(page_number, {})
            #page["image"] = element.values.get("{http://www.w3.org/1999/xlink}href")
            #x = float(element.values.get("x"))
            #y = float(element.values.get("y"))
            width = float(element.values.get("width"))
            height = float(element.values.get("height"))
            #page["bbox"] = (x, y, x + width, y + height)
            #page["width"] = int(element.values.get("imslp-width"))
            #page["height"] = int(element.values.get("imslp-height"))
            #imslp_pages[page_number] = page

            svg_info["width"] = width
            svg_info["height"] = height

        elif type(element) is Rect:
            x = float(element.values.get("x"))
            y = float(element.values.get("y"))
            width = float(element.values.get("width"))
            height = float(element.values.get("height"))
            annotation_bboxes.append((
                x, y, x + width, y + height
            ))
    
    svg_info["annotations"] = annotation_bboxes
    
    print("Parsed score:", svg_path)
    
    # Write the information to a JSON file
    json_path = svg_path.replace(".svg", ".json")
    json_path = "data\\json_files\\" + json_path
    #os.makedirs(os.path.dirname(json_path), exist_ok=True)

    with open(json_path, "w") as json_file:
        json.dump(svg_info, json_file, indent=4)
    