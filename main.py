import os
from download_scores import download
from load import resize_and_save_png, create_inkscape_svg
from save import save2json

def main():

    # # Download scores from kramerius.mzk.cz
    # scores_paths = download("data\\scores.csv")

    # # Create Inkscape SVG from MZK images
    # for score_path in scores_paths:
    #     #resized_png_path = resize_and_save_png(score_path)
    #     create_inkscape_svg(score_path)


    # # Create Inkscape SVG from binarized IMSLP images
    # imslp_paths = ["./data/scores/" + path for path in os.listdir("data\\scores") if path.startswith("IMSLP")]
    # for imslp_path in imslp_paths:
    #     create_inkscape_svg(imslp_path)


    # Save the annoted SVG files to JSON
    for svg_path in os.listdir("data\\svg_files"):
        save2json(svg_path)


if __name__ == "__main__":
    main()