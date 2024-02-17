from load import resize_and_save_png, create_inkscape_svg
from download_scores import download

def main():
    scores_paths = download("data\\scores.csv")

    for score_path in scores_paths:
        #resized_png_path = resize_and_save_png(score_path)
        create_inkscape_svg(score_path)

if __name__ == "__main__":
    main()