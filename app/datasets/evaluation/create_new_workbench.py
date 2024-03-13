from PIL import Image
from pathlib import Path

def create_new_workbench(
    from_image_path: str, 
    to_path_svg: str
):
    width, height = -1, -1
    with Image.open(from_image_path) as img:
        width, height = img.size

    if Path(to_path_svg).exists():
        print(f"Skipping {to_path_svg}...")
        return

    Path(to_path_svg).parent.mkdir(parents=True, exist_ok=True)

    # Create SVG to be annotated in Inkscape from the image 
    with open(to_path_svg, 'w') as file:
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
            xlink:href="{from_image_path}"/>
        """)

    # From images to annotations
        file.write("""
    </g>
    <g
        inkscape:groupmode="layer"
        id="layer2"
        inkscape:label="Note"
        style="display:inline">
    """)


    #TODO: add other classes as layers to the SVG file, specified in Annotation.CLASSES
    #     file.write("""
    # </g>
    # <g
    #     inkscape:groupmode="layer"
    #     id="layer3"
    #     inkscape:label="Annotation.CLASSES[1]"    #Bar
    #     style="display:inline">
    # """)
    
    #TODO: pak zaktualizovat i evaluation_dataset i validation_dataset

    # Footer
        file.write("""
      </g>
    </svg>
    """)