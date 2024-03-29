# Bachelor-Thesis

```
.venv/                    # virtuální prostředí pythonu
evaluation-dataset/       # bude na githubu, bude to relativně málo dat
    images/               # dříve "scores" - obsahují zdrojové png a jpg
        libovolne-jmeno.png
    workbenches/          # .svg soubory (work in progress)
        libovolne-jmeno.svg
    annotations/          # finlání .json soubory s bounding boxy
        libovolne-jmeno.json
    sources.md            # jen textové poznámky - odkud se vzal libovolne-jmeno.png
    README.md             # tady můžu zdokumentovat strukturu dat a kde co je a jak dataset použít
app/
    Annotation.py
    datasets/
        __init__.py
        evaluation/
            __init__.py
            __main__.py       # tohle jde spustit přes `python3 -m app.datasets.evaluation`
            extract_annotations_from_workbench.py # bývalé save.py
            create_new_workbench.py # bývalé create.py
        training/
            __init__.py
            download_oslic.py
            generate_images_for_oslic.py # může mít více funkcí - vytvoreni docasneho json souboru na convert do svg, png.
            extact_annotations_from_mscore_svg.py - do jsonu
    __init__.py           # prázdný, udělá ze složky python modul
datasets/                 # nebude na githubu, tady jsou DATA
    OpenScore-Lieder/
README.md                 # hlavní vstup do dokumentace - tady můžeš odkázat na jiná readme v podsložkách
```




Relativní importy - z extract_annotations_from_workbench.py importuju Annotation.py

    from ...Annotaion import Annotation

viz: https://github.com/ufal/olimpic-icdar24/blob/master/app/datasets/scanned/__main__.py


Struktura anotačního JSON souboru
```json
{
    "width": 1080,       # rozměry PNG/JPG obrázku v images/ složce v pixelech
    "height": 1920,
    "annotations": [
        { # tohle může být data class "Annotation" třeba s funkcí .to_json() -> dict
            "class": "Note",  # napiš si někde seznam možných hodnot - nějaké "README.md"
            "x": 1,
            "y", 2,
            "width": 3,
            "height": 4
        },
        ...
    ]
}
```

TODO: podivat se na NOTE a zjistit, jestli je treba jeste nevo predelat.
TODO: zkontrolovat komentare, pripadne prelozit do Aj, pripadne dookomentovat


# YOLO V8
## Structure of dataset
```
dataset/
    images/
        train/
            image_name.jpg
            ...
        val/
            image_name.jpg
            ...
        test/
            image_name.jpg
            ...
    labels/
        train/
            image_name.txt
            ...
        val/
            image_name.txt
            ...
        test/
            image_name.txt
            ...
```

## Format of labels
```txt
<class> <x_center> <y_center> <width> <height>
<class> <x_center> <y_center> <width> <height>
...
```
Where: 
- <class> - integer representing the class of the object. Acquires values 0 for Notehead, 1 for Staff and 2 for StaffMeasure.
- <x_center> - float representing the x coordinate of the center of the bounding box relative to the image size
- <y_center> - float representing the y coordinate of the center of the bounding box relative to the image size
- <width> - float representing the width of the bounding box relative to the image size
- <height> - float representing the height of the bounding box relative to the image size
  