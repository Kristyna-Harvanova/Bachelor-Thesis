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

def create_inkscape_svg(resized_png_path, width=210, height=297):
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

    # From images to annotations
        file.write("""
    </g>
    <g
        inkscape:groupmode="layer"
        id="layer2"
        inkscape:label="Annotations"
        style="display:inline">
    """)

    # Footer
        file.write("""
      </g>
    </svg>
    """)