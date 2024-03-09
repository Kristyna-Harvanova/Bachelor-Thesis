.jpg images from MZK https://www.digitalniknihovna.cz/mzk
.png images from IMSLP

#TODO

from MZK used these:
uuid,x,y,width,height
3997e154-a7bc-41d8-9bf2-089c50187b10,131,112,2925,3804
70fac7dd-90e8-4e7b-b12f-0b0c1ccbca00,130,287,1890,2571
cc8bc884-ae43-4a26-8914-4f988bec7bb6,63,168,2543,3142

downloading via Python: 

import os
import requests

def download(
        images_csv_path: str,
    ) -> list:
    """
    Downloads scores from kramerius.mzk.cz
    """
    images = []

    with open(images_csv_path, "r") as csv_file:
        skipped_first_line = csv_file.readline()
        for line in csv_file:
            info = line.split(",")
            uuid = info[0]
            x = info[1]
            y = info[2]
            width = info[3]
            height = info[4][:-1]  # removing last character "\n"

            url = f"https://kramerius.mzk.cz/search/iiif/uuid:{uuid}/{x},{y},{width},{height}/max/0/default.jpg"
            image_path = f"./data/scores/{uuid}_{x}_{y}_{width}_{height}.jpg"

            if not os.path.exists(image_path):
                print(f"Downloading {uuid}_{x}_{y}_{width}_{height}...")
                r = requests.get(url, allow_redirects=True)
                open(image_path, "wb").write(r.content)
            else:
                print(f"Skipping {uuid}_{x}_{y}_{width}_{height}...")
            
            images.append(image_path)
    
    return images
