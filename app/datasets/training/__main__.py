import os
import glob
from .generate_images_for_oslic import convert_mscx2format
from .extract_annotations_from_mscore_svg import extract_annotations_from_mscore_svg

def main():
    # Convert the MSCX files to .svg
    #convert_mscx2format("datasets\\OpenScoreLieder\\scores", "svg")

    #TODO udelat i pro png, ale nefunguje pro vsechny u svg (viz convert_mscx2format)

    # Extract the annotations from the SVG 
    svg_files = glob.glob(r"datasets\OpenScoreLieder\scores\*\*\*\*.svg", recursive=True)

    for svg_file in svg_files:
        directory = os.path.dirname(svg_file.replace(".svg", ".json").replace("scores", "annotations"))
        os.makedirs(directory, exist_ok=True)
        extract_annotations_from_mscore_svg(svg_file, directory + "\\" + os.path.basename(svg_file).replace(".svg", ".json"))
    
    #TODO: nechat bezet a vytvorit vsecny jsony (trva to), az budu mit dostupne vsechny svg viz convert_mscx2format

if __name__ == "__main__":
    main()