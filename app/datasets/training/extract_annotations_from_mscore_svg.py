from svgelements import *
import json
from statistics import median
from ...Annotation import Annotation

def extract_annotations_from_mscore_svg(
    from_path_svg: str, 
    to_path_json: str
):
    # Load the SVG file
    with open(from_path_svg) as svg_file:
        svg_file: SVG = SVG.parse(svg_file, reify=True)
    
    svg_info = {}
    annotation_bboxes = []
    
    wanted_classes = ["Note", "StaffLines", "BarLine"]

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

            if cls == wanted_classes[0]:
                notes.append(element)
            elif cls == wanted_classes[1]:
                staff_lines.append(element)
            elif cls == wanted_classes[2]:
                bar_lines.append(element)
    
    # Process the notes
    if len(notes) > 0: process_notes(notes, annotation_bboxes)

    # Process the staff lines
    if len(staff_lines) > 0: staves = process_staff_lines(staff_lines, annotation_bboxes)

    # Process the bar lines
    if len(bar_lines) > 0: process_bar_lines(bar_lines, annotation_bboxes, staves)

    # Add the annotations to the SVG info
    svg_info["annotations"] = annotation_bboxes

    print("Parsed score:", from_path_svg)

    # Save the information to a JSON file
    with open(to_path_json, "w") as json_file:
        json.dump(svg_info, json_file, indent=4)
    

def process_notes(
    notes: list, 
    annotation_bboxes: list    
):
    for note in notes:
        annotation_class = Annotation.CLASSES[0]
        x, y, x_and_width, y_and_height = note.bbox()
        width = x_and_width - x
        height = y_and_height - y
        annotation_bbox = Annotation(annotation_class, int(x), int(y), int(width), int(height))
        annotation_bboxes.append(annotation_bbox.to_json())

def process_staff_lines(
    staff_lines: list,
    annotation_bboxes: list
) -> list[Annotation]:
    
    # Sort the staff lines by their x and then y coordinate (final order from left to right and from top to bottom).
    staff_lines_sorted = sorted(staff_lines, key=lambda x: x.bbox()[0])
    staff_lines_sorted.sort(key=lambda x: x.bbox()[1]) 

    # Merge staff lines that consist of multiple objects.
    staff_lines_final = []
    current_staff_line = staff_lines_sorted[0]
    i = 1
    while (i < len(staff_lines_sorted)):
        y_diff = staff_lines_sorted[i].bbox()[1] - current_staff_line.bbox()[1]

        # The staff line is the same as the previous, just divided into multiple objects.
        if (y_diff > -1 and y_diff < 1):    
            merged_bbox = (
                current_staff_line.bbox()[0],
                current_staff_line.bbox()[1], 
                staff_lines_sorted[i].bbox()[2], 
                staff_lines_sorted[i].bbox()[3]    
            )
            current_staff_line = Polyline(merged_bbox)
        else:
            staff_lines_final.append(current_staff_line)
            current_staff_line = staff_lines_sorted[i]
        i += 1
    staff_lines_final.append(current_staff_line)

    # Calculate the differences between the staff lines and find the average
    differences = [staff_lines_final[i+1].bbox()[1] - staff_lines_final[i].bbox()[1] for i in range(len(staff_lines_final)-1)]
    average_diff = median(differences) 
    possible_shift = 8

    # Cluster staff lines into staves.
    staves = []
    staff = []
    for staff_line in staff_lines_final:
        # If the staff is empty, add the first staff line
        if (len(staff) == 0): 
            staff.append(staff_line)

        # Add the next staff lines to the staff
        elif (len(staff) < 5):
            y_diff = staff_line.bbox()[1] - staff[-1].bbox()[1]
            if (y_diff > average_diff - possible_shift and y_diff < average_diff + possible_shift): 
                staff.append(staff_line)
            else: print("Incomplete staff")     # NOTE: This should not happen.

        # If the staff is complete, create a bounding box and reset the staff
        if (len(staff) == 5):
            annotation_class = Annotation.CLASSES[1]
            x, y, x_and_width, _ = staff[0].bbox()  # Get the bounding box of the first staff line
            width = x_and_width - x
            height = staff[-1].bbox()[3] - y        # Get the height of the staff = whole 5 lines
            annotation_bbox = Annotation(annotation_class, int(x), int(y), int(width), int(height))
            annotation_bboxes.append(annotation_bbox.to_json())
            staves.append(annotation_bbox)
            staff = []
    
    return staves

def process_bar_lines(
    bar_lines: list,
    annotation_bboxes: list,
    staves: list[Annotation]
):
    # Sort the bar lines by their x and then y coordinate (final order from left to right and from top to bottom)
    bar_lines_sorted = sorted(bar_lines, key=lambda x: x.bbox()[0])
    bar_lines_sorted.sort(key=lambda x: x.bbox()[1])
    
    two_barline_diff = 20   # There can be a measure, that ends with two bar lines, but the space between them is not another measure.
    new_staff_diff = 1.1 * staves[0].height     # The minimal space between the staves must be slightly greater than the height of the staff

    # Create a bounding box for each bar
    staff_index = 0
    for i in range(len(bar_lines_sorted)):
        annotation_class = Annotation.CLASSES[2]
        x, y, _, _ = bar_lines_sorted[i].bbox()
        x2, y2, _, _ = bar_lines_sorted[i+1].bbox() if i+1 < len(bar_lines_sorted) else (0, 0, 0, 0)

        if (y2 - y) > new_staff_diff: 
            staff_index += 1
            continue   # This is not a measure, but a new line = new staff. (Or the end of the score.)
        if (x2 - x) < two_barline_diff: continue    # This is not a measure, but a double bar line.

        width = x2 - x
        height = staves[staff_index].height
        annotation_bbox = Annotation(annotation_class, int(x), int(y), int(width), int(height))
        annotation_bboxes.append(annotation_bbox.to_json())