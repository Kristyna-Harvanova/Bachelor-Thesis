import requests
import zipfile
from pathlib import Path
from tqdm import tqdm

def download_oslic(dataset_dir: Path = Path("datasets")):
    download_dataset(
        "https://github.com/apacha/OMR-Datasets/releases/download/datasets/OpenScore-Lieder-Snapshot-2023-10-30.zip",
        "OpenScore-Lieder-Snapshot-2023-10-30.zip",
        dataset_dir
    )

def download_dataset(
        url: str,
        zip_file_name: str,
        dataset_dir: Path = Path("datasets")
):
    dataset_dir.mkdir(parents=True, exist_ok=True)

    file_path = dataset_dir / zip_file_name
    
    response = requests.get(url, stream=True)

    with open(file_path, "wb") as file:
        for data in tqdm(response.iter_content()):
            file.write(data)
    
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(dataset_dir)
