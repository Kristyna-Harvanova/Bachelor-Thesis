from tqdm import tqdm
import requests
import zipfile

def download_oslic():
    download_dataset(
        "https://github.com/apacha/OMR-Datasets/releases/download/datasets/OpenScore-Lieder-Snapshot-2023-10-30.zip",
        "OpenScore-Lieder-Snapshot-2023-10-30.zip"
    )

def download_dataset(
        url: str,
        zip_file_name: str,
):
    response = requests.get(url, stream=True)

    with open(zip_file_name, "wb") as file:
        for data in tqdm(response.iter_content()):
            file.write(data)
    
    with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
        zip_ref.extractall("datasets")
