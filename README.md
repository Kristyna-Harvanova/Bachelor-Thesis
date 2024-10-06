﻿# Postprocessing of Synthetic Sheet Music in the Context of Optical Music Recognition.

This repository contains the code and datasets for the Bachelor Thesis project on Postprocessing of Synthetic Sheet Music in the Context of Optical Music Recognition.

## Abstract

### English version:

This work focuses on improving training data synthesis methods for the Optical Music Recognition (OMR) task. The study concentrates on creating realistic, colored, and degraded images of musical scores (postprocessing). These degraded data are generated from synthetic, purely black-and-white images. After applying postprocessing methods, the musical scores closely mimic physical documents, thereby enhancing the quality of training data for OMR models. The proposed postprocessing methods were tested on object detection tasks, specifically recognizing various types of musical symbols. Experiments demonstrated that all proposed methods positively impact the resulting OMR model, with the greatest benefit coming from the generation of synthetic backgrounds for musical scores.

### Czech version:

Tato práce se zaměřuje na vylepšení metod syntézy trénovacích dat pro úlohu Optical Music Recognition (OMR). Práce se soustředí na vytváření realistických barevných a degradovaných obrázků not (postprocessing). Tato degradovaná data vznikají ze syntetických čistě černo-bílých obrázků. Po aplikaci postprocessingových metod notopisy věrně napodobují fyzické dokumenty, čímž zlepšují kvalitu trénovacích dat pro OMR modely. Navržené postprocessingové metody byly testovány na úloze object detection, neboli na rozpoznávání jednotlivých typů různých hudebních symbolů. Experimenty prokázaly, že všechny navržené metody pozitivně ovlivňují výsledný OMR model, přičemž největší přínos má generování syntetického pozadí notopisů.

## Thesis

[Link to the text of the Bachelor Thesis](https://dspace.cuni.cz/handle/20.500.11956/192815)

## Poster 

![Poster](Poster_Harvanova.jpg)

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
