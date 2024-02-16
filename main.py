from load import resize_and_save_png, create_inkscape_svg_with_png

def main():
    #resized_png_path = resize_and_save_png("data\\scores\\3997e154-a7bc-41d8-9bf2-089c50187b10_131_112_2925_3804.jpg", 210, 297)
    original_png_path = "data\\scores\\3997e154-a7bc-41d8-9bf2-089c50187b10_131_112_2925_3804.jpg"
    create_inkscape_svg_with_png(original_png_path)

if __name__ == "__main__":
    main()