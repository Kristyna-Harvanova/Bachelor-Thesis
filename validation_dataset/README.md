# Validation Dataset

This folder contains data used for the validation of the models in the Bachelor Thesis project.

## Structure

- `images/`: Contains source images in .png and .jpg formats.
- `workbenches/`: Contains .svg files which are work-in-progress annotations.
- `annotations/`: Contains final .json files with bounding box annotations.
- `sources.md`: Notes on the origin of the images.
- `README.md`: Documentation on the data structure and usage.

## Data Sources

- .jpg images are sourced from MZK (https://www.digitalniknihovna.cz/mzk).
- .png images are sourced from IMSLP.

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
