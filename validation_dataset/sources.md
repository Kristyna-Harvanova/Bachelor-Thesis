.jpg images from MZK https://www.digitalniknihovna.cz/mzk
.png images from IMSLP

#TODO

from MZK used these:
uuid,x,y,width,height
9e446997-58b4-4d6b-b9d8-34d184959afe,292,316,2806,3583
8b0bc152-b2af-4144-8a02-26ffea43e1f1,321,230,2168,2865
df035893-7ef1-4782-af6b-985fe74aa167,0,0,3870,3223

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
