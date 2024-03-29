import requests
from pathlib import Path

def download(
        images_csv_path: Path,
    ) -> list:
    """
    Downloads images from kramerius.mzk.cz
    """
    images = []

    with images_csv_path.open("r") as csv_file:
        skipped_first_line = csv_file.readline()
        for line in csv_file:
            info = line.split(",")
            uuid = info[0]
            x = info[1]
            y = info[2]
            width = info[3]
            height = info[4]
            dpi = info[5][:-1]  # removing last character "\n"

            url = f"https://kramerius.mzk.cz/search/iiif/uuid:{uuid}/{x},{y},{width},{height}/max/0/default.jpg"
            image_name = f"{uuid}_{x}_{y}_{width}_{height}_{dpi}.jpg"
            image_path = images_csv_path.parent / "images" / image_name
            #image_path = f"./backgrounds/images/{uuid}_{x}_{y}_{width}_{height}_{dpi}.jpg"

            #if not os.path.exists(image_path):
            if not image_path.exists():
                print(f"Downloading {image_name}...")
                r = requests.get(url, allow_redirects=True)
                #open(image_path, "wb").write(r.content)
                image_path.write_bytes(r.content)
            else:
                print(f"Skipping {image_name}...")
            
            images.append(str(image_path))
    
    return images
