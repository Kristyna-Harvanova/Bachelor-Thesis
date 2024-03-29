from pathlib import Path
from .download_datasets import download_oslic
from .generate_images_for_oslic import convert_mscx2format
from .extract_annotations_from_mscore_svg import extract_annotations_from_mscore_svg
from .format_data_for_yolo import json_to_yolo_format

def main():
    # Download the OpenScore Lieder dataset
    #download_oslic()    

    # Convert the MSCX files to .png
    path_mscxs = Path("datasets", "Lieder-main", "scores")
    #convert_mscx2format(str(path_mscxs), "png")    #NOTE: info trva cca 66 minut. 

    # Convert the MSCX files to .svg
    #convert_mscx2format(str(path_mscxs), "svg")    #NOTE: info trva cca 10 minut.  

    # Extract the annotations from the SVG 
    path_svgs = Path("datasets", "Lieder-main", "scores")
    svg_files = list(path_svgs.glob("**/*.svg"))
    svg_files.sort() # Sort files if not in the same directory

    # for i, svg_file in enumerate(svg_files):
    #     print(i)
    #     extract_annotations_from_mscore_svg(      #NOTE: info trva cca 4 hodiny na aic. Vytvoreno 5174 souboru.
    #         str(svg_file),
    #         str(svg_file.with_suffix(".json")) 
    #     )

    # Convert the annotations to YOLO format
    path_jsons = Path("datasets", "Lieder-main", "scores")
    json_files = list(path_jsons.glob("**/*.json"))
    json_files.sort()

    # for i, json_file in enumerate(json_files):
    #     print(f"{i}: {json_file}")
    #     json_to_yolo_format(                        #NOTE: info trva cca 30 sekund na aic. Vytvoreno 5165 souboru.
    #         json_file,
    #         Path("yolo", "dataset", "labels", "train")
    #     )


    # Copy images into directory for Yolo training
    # import shutil

    # path_pngs = Path("datasets", "Lieder-main", "scores")
    # png_files = list(path_pngs.glob("**/*.png"))
    # png_files.sort()

    # dest_dir = Path("yolo", "dataset", "images", "train")

    # from datetime import datetime
    # start = datetime.now()

    # for i, png_file in enumerate(png_files):
    #     print(f"{i}: {png_file}")
    #     shutil.copy(png_file, dest_dir / png_file.name) #NOTE: info trva cca 6 minut na aic. Vytvoreno 5174 souboru.

    # print(datetime.now() - start)


    png_files = list(Path("yolo", "dataset", "images", "train").glob("*.png"))
    
    # # TODO: from alpha and black pistures to white and black pictures
    # import cv2
    # for i, png_file in enumerate(png_files):
    #     print(f"{i}: {png_file}")
    #     img = cv2.imread(str(png_file), cv2.IMREAD_UNCHANGED)
    #     img[img == 0] = 255
    #     cv2.imwrite(str(png_file), img)
    
    # TODO: using numpy: from alpha and black pistures to white and black pictures
    import numpy as np
    for i, png_file in enumerate(png_files):
        print(f"{i}: {png_file}")
        img = np.array(Image.open(str(png_file)))
        img[img == 0] = 255
        Image.fromarray(img).save(str(png_file))
        
    


   


if __name__ == "__main__":
    main()