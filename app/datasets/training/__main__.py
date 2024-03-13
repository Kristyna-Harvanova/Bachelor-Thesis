from pathlib import Path
from .generate_images_for_oslic import convert_mscx2format
from .extract_annotations_from_mscore_svg import extract_annotations_from_mscore_svg
from .download_datasets import download_oslic

def main():
    # Download the OpenScore Lieder dataset
    #download_oslic()    
    #download_oslic(Path("D:"))   

    path_mscxs = Path("datasets", "Lieder-main", "scores")
    #path_mscxs = Path("D:", "Lieder-main", "scores")

    # Convert the MSCX files to .png
    #convert_mscx2format(str(path_mscxs), "png")    #NOTE: info trva cca 66 minut. 

    # Convert the MSCX files to .svg
    #convert_mscx2format(str(path_mscxs), "svg")    #NOTE: info trva cca 10 minut.

    # Extract the annotations from the SVG 
    path_svgs = Path("datasets", "Lieder-main", "scores")
    #path_svgs = Path("D:", "Lieder-main", "scores")
    svg_files = list(path_svgs.glob("**/*.svg"))
    svg_files.sort() # Sort files if not in the same directory

    # for svg_file in svg_files[:5]:
    #     extract_annotations_from_mscore_svg(      #NOTE: info trva cca XX minut.
    #         str(svg_file),
    #         str(svg_file.with_suffix(".json")) 
    #     )
    
    #TODO: nechat bezet a vytvorit vsecny jsony (trva to), az budu mit dostupne vsechny svg viz convert_mscx2format a hotovy kod extract_annotations_from_mscore_svg

if __name__ == "__main__":
    main()