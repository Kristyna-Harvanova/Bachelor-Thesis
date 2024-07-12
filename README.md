# Bachelor Thesis Project

This repository contains the code and datasets for the Bachelor Thesis project on Postprocessing of Synthetic Sheet Music in the Context of Optical Music Recognition.

## Structure

- `app/`: Application code.
  - `Annotation.py`: Dataclass for annotations.
  - `datasets/`: Scripts for dataset management.
    - `__init__.py`: Module initializer.
    - `augmentation/`: Scripts for data augmentation.
    - `evaluation/`: Scripts for evaluation dataset.
    - `training/`: Scripts for training dataset.
    - `validation/`: Scripts for validation dataset.
- `datasets/`: Data folder, not included in the repository. Data will be automatically downloaded.
  - `OpenScore-Lieder/`: Contains OpenScore Lieder dataset.
- `evaluation-dataset/`: Contains evaluation data.
- `validation_dataset/`: Contains validation data.
- `requirements.txt`: Python dependencies.
- `README.md`: Main documentation.

## Usage

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the desired script as
    ```
    python -m app.datasets.module_name
    ```
    from the root directory.


## Example of Annotation JSON Structure

```json
{
    "width": 1890,
    "height": 2571,
    "annotations": [
        {
            "class": "StaffMeasure",
            "x": 1434,
            "y": 2329,
            "width": 455,
            "height": 107
        },
        {
            "class": "Notehead",
            "x": 351,
            "y": 170,
            "width": 32,
            "height": 29
        }
    ]
}
```

# YOLO V8
## Structure of dataset

The dataset is divided into three parts: training, validation, and testing. Each part contains two folders: images and labels. The images folder contains the images in .jpg format, and the labels folder contains the labels in .txt format.

- `dataset/`
  - `images/`
    - `train/`
      - `image_name.jpg`
      - ...
    - `val/`
      - `image_name.jpg`
      - ...
    - `test/`
      - `image_name.jpg`
      - ...
  - `labels/`
    - `train/`
      - `image_name.txt`
      - ...
    - `val/`
      - `image_name.txt`
      - ...
    - `test/`
      - `image_name.txt`
      - ...


## Format of labels
```txt
<class> <x_center> <y_center> <width> <height>
<class> <x_center> <y_center> <width> <height>
...
```

### Explanation
- `<class>` - Integer representing the class of the object. Values:
    - `0` for Notehead
    - `1` for Staff
    - `2` for StaffMeasure
- `<x_center>` - Float representing the x coordinate of the center of the bounding box relative to the image size.
- `<y_center>` - Float representing the y coordinate of the center of the bounding box relative to the image size.
- `<width>` - Float representing the width of the bounding box relative to the image size.
- `<height>` - Float representing the height of the bounding box relative to the image size.
