# #import yaml
# import os
# import io
# import glob
# #import cv2
# from detect_systems_in_svg import detect_systems_in_svg


from PIL import Image
import os

def resize_and_save_png(original_png_path, resized_width=210, resized_height=297):
    resized_png_path = os.path.splitext(original_png_path)[0] + "_resized.png"

    # Check if the resized image already exists
    if not os.path.exists(resized_png_path):
        with Image.open(original_png_path) as img:
            resized_img = img.resize((resized_width, resized_height))
            resized_img.save(resized_png_path)
    
    return resized_png_path


def create_inkscape_svg_with_png(resized_png_path, width=210, height=297):
    png_base_name = os.path.basename(os.path.splitext(resized_png_path)[0])
    svg_file_path = os.path.join("data", "svg_files", png_base_name + ".svg")
    os.makedirs(os.path.dirname(svg_file_path), exist_ok=True)

    # Create Inkscape SVG with the resized PNG
    with open(svg_file_path, 'w') as file:
        file.write(f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <svg
       width="{width}"
        height="{height}"
        viewBox="0 0 {width} {height}"
        version="1.1"
        id="svg1"
        inkscape:version="1.3.2 (091e20e, 2023-11-25, custom)"
        sodipodi:docname="workbench.svg"
        xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
        xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:svg="http://www.w3.org/2000/svg">
        <sodipodi:namedview
            id="namedview1"
            pagecolor="#ffffff"
            bordercolor="#666666"
            borderopacity="1.0"
            inkscape:showpageshadow="2"
            inkscape:pageopacity="0.0"
            inkscape:pagecheckerboard="0"
            inkscape:deskcolor="#d1d1d1"
            inkscape:document-units="mm"
            showgrid="false"
            units="px"
            inkscape:zoom="1"
            inkscape:cx="500"
            inkscape:cy="500"
            inkscape:window-width="1920"
            inkscape:window-height="974"
            inkscape:window-x="-11"
            inkscape:window-y="-11"
            inkscape:window-maximized="1"
            inkscape:current-layer="layer2" />
        <defs
            id="defs1" />
        <g
            inkscape:label="Images"
            inkscape:groupmode="layer"
            id="layer1"
            sodipodi:insensitive="true">
        <image
            width="{width}"
            height="{height}"
            preserveAspectRatio="none"
            xlink:href="{resized_png_path}"/>
        """)

    # from images to annotations
        file.write("""
    </g>
    <g
        inkscape:groupmode="layer"
        id="layer2"
        inkscape:label="Annotations"
        style="display:inline">
    """)

    # footer
        file.write("""
      </g>
    </svg>
    """)









# def load_workbench(score_id: int):
#     # Get all the scores metadata.
#     with open(os.path.join("data", "scores.yaml")) as file:
#         all_scores = yaml.safe_load(file)
    
#     # Check if the workbench file does not already exists.
#     workbench_file = os.path.join("datasets", "workbench.svg")
#     if os.path.isfile(workbench_file):
#         print("[ERROR] Workbench file already exists.")
#         return

#     print("Loading score", score_id, ":")
#     for key, value in all_scores[score_id].items():
#         print(str(key) + ":", value)
#     print()

#     imslp_id = all_scores[score_id]["imslp"][1:]

#     open_imslp_pdf(imslp_id)
    
#     start_page = int(input("Enter the starting page: "))

#     musescore_corpus_conversion(
#         {score_id: all_scores[score_id]},
#         format="svg",
#         soft=True
#     )

#     svg_pages = detect_systems_in_svg(score_id)

#     with open(workbench_file, "w") as file:
#         create_inkscape_file(svg_pages, score_id, file)





# def load_workbench(score_id: int):
#     svg_page = detect_systems_in_svg(score_id)
#     workbench_file = os.path.join("datasets", "workbench.svg")
#     with open(workbench_file, "w") as file:
#         create_inkscape_file(svg_page, score_id, file)


# def create_inkscape_file(svg_pages, score_id, file: io.FileIO):
#     PAGE_HEIGHT = 297
#     SPACING = 10
#     CORPUS_X = 0

#     file.write(f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
#     <svg
#         score-id="{score_id}"
#         width="210"
#         height="297"
#         viewBox="0 0 210 297"
#         version="1.1"
#         id="svg1"
#         inkscape:version="1.3.2 (091e20e, 2023-11-25, custom)"
#         sodipodi:docname="workbench.svg"
#         xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
#         xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
#         xmlns:xlink="http://www.w3.org/1999/xlink"
#         xmlns="http://www.w3.org/2000/svg"
#         xmlns:svg="http://www.w3.org/2000/svg">
#         <sodipodi:namedview
#             id="namedview1"
#             pagecolor="#ffffff"
#             bordercolor="#666666"
#             borderopacity="1.0"
#             inkscape:showpageshadow="2"
#             inkscape:pageopacity="0.0"
#             inkscape:pagecheckerboard="0"
#             inkscape:deskcolor="#d1d1d1"
#             inkscape:document-units="mm"
#             showgrid="false"
#             units="px"
#             inkscape:zoom="1"
#             inkscape:cx="500"
#             inkscape:cy="500"
#             inkscape:window-width="1920"
#             inkscape:window-height="974"
#             inkscape:window-x="-11"
#             inkscape:window-y="-11"
#             inkscape:window-maximized="1"
#             inkscape:current-layer="layer2" />
#         <defs
#             id="defs1" />
#         <g
#             inkscape:label="Images"
#             inkscape:groupmode="layer"
#             id="layer1"
#             sodipodi:insensitive="true">
#     """)

#     # print OS lieder corpus SVGs
#     for pi, svg_page in enumerate(svg_pages):
#         path = svg_page["path"]
#         score_id = svg_page["score_id"]
#         page_number = svg_page["page_number"]
#         ratio = PAGE_HEIGHT / svg_page["page_height"]
#         height = svg_page["page_height"] * ratio
#         width = svg_page["page_width"] * ratio
#         px = CORPUS_X
#         py = pi * (PAGE_HEIGHT + SPACING)
#         file.write(f"""
#         <rect
#             style="fill:#ffffff;fill-opacity:1.0;"
#             id="paper-white-lc{score_id}-p{page_number}"
#             width="{width}"
#             height="{height}"
#             x="{px}"
#             y="{py}" />
#         """)
#         file.write(f"""
#         <image
#             width="{width}"
#             height="{height}"
#             preserveAspectRatio="none"
#             xlink:href="{path}"
#             id="{score_id}"
#             x="{px}"
#             y="{py}" />
#         """)

#     # from images to annotations
#     file.write("""
#     </g>
#     <g
#         inkscape:groupmode="layer"
#         id="layer2"
#         inkscape:label="Annotations"
#         style="display:inline">
#     """)

#     # print OS lieder system bounding boxes
#     for pi, svg_page in enumerate(svg_pages):
#         path = svg_page["path"]
#         score_id = svg_page["score_id"]
#         page_number = svg_page["page_number"]
#         ratio = PAGE_HEIGHT / svg_page["page_height"]
#         height = svg_page["page_height"] * ratio
#         width = svg_page["page_width"] * ratio
#         px = CORPUS_X
#         py = pi * (PAGE_HEIGHT + SPACING)
#         for si, system in enumerate(svg_page["systems"]):
#             sx = system["left"] * ratio
#             sy = system["top"] * ratio
#             sw = (system["right"] - system["left"]) * ratio
#             sh = (system["bottom"] - system["top"]) * ratio
#             file.write(f"""
#             <rect
#                 style="fill:{WORKBENCH_RECT_COLOR};fill-opacity:0.366049;stroke-width:0.1"
#                 id="rect{score_id}-s{si + 1}"
#                 width="{sw}"
#                 height="{sh}"
#                 x="{px + sx}"
#                 y="{py + sy}" />
#             """)

#     # footer
#     file.write("""
#       </g>
#     </svg>
#     """)