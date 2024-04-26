import json
from svgelements import *
from ...Annotation import Annotation

def process_bar_lines(
        bar_lines: list,
        annotation_bboxes: list,
        staves: list[Annotation]
):
    # method is the same as Kristynas, but! this filtration is added
    # keep in mind that this method modifies the existing bars!
    # using "bar_lines" outside of this method after this filtration may lead to inconsistent results
    bar_lines = filter_bars_in_staves(bar_lines, staves)

    # Sort the bar lines by their x and then y coordinate (final order from left to right and from top to bottom)
    bar_lines_sorted = sorted(bar_lines, key=lambda x: x.bbox()[0])
    bar_lines_sorted.sort(key=lambda x: x.bbox()[1])

    TWO_BARLINE_DIFF = 20  # There can be a measure, that ends with two bar lines, but the space between them is not another measure.
    NEW_STAFF_DIFF = 1.1 * staves[
        0].height  # The minimal space between the staves must be slightly greater than the height of the staff

    # Create a bounding box for each bar
    staff_index = 0
    for i in range(len(bar_lines_sorted)):
        annotation_class = Annotation.CLASSES[2]
        x, y, _, _ = bar_lines_sorted[i].bbox()
        x2, y2, _, _ = bar_lines_sorted[i + 1].bbox() if i + 1 < len(bar_lines_sorted) else (0, 0, 0, 0)

        if (y2 - y) > NEW_STAFF_DIFF:
            staff_index += 1
            continue  # This is not a measure, but a new line = new staff. (Or the end of the score.)
        if (x2 - x) < TWO_BARLINE_DIFF: continue  # This is not a measure, but a double bar line.

        width = x2 - x
        height = staves[staff_index].height
        annotation_bbox = Annotation(annotation_class, int(x), int(y), int(width), int(height))
        annotation_bboxes.append(annotation_bbox.to_json())


def filter_bars_in_staves(
        bar_lines: list,
        staves: list[Annotation],
        offset: int = 2
):
    """
    Given a list of bars and staves this method checks whether the bars belong to any staff (they intersect it),
    if so the bar is added to a list of valid bars. The bar is trimmed to fit exactly the staff it is associated with.
    """
    output = []
    # for every bar
    for bar_line in bar_lines:
        x, y, x1, y1 = bar_line.bbox()
        temp = False
        # check over all staves
        for staff in staves:
            # bar belongs to a staff if it has one endpoint above it and one below it
            if y <= staff.y + offset and staff.y + staff.height - offset <= y1:
                # trim the bar to fit the staff
                bar_line.points = [(x, staff.y), (x1, staff.y + staff.height)]
                output.append(bar_line)
                temp = True
                break
        # if not temp:
        #     print(f"Removing {bar_line.bbox()}")
    return output