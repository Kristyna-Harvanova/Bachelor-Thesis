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
    
    # path = Path("datasets", "Lieder-main", "scores", "Satie,_Erik", "Socrate")
    # convert_mscx2format(str(path), "svg")    

    # Extract the annotations from the SVG 
    path_svgs = Path("datasets", "Lieder-main", "scores")
    #path_svgs = Path("D:", "Lieder-main", "scores")
    svg_files = list(path_svgs.glob("**/*.svg"))
    svg_files.sort() # Sort files if not in the same directory

    for i, svg_file in enumerate(svg_files):
        if i < 4109: continue
        print(i)
        extract_annotations_from_mscore_svg(      #NOTE: info trva cca 4 hodiny na aic.
            str(svg_file),
            str(svg_file.with_suffix(".json")) 
        )

if __name__ == "__main__":
    main()