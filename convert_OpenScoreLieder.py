from typing import Dict, Any
import os
import tempfile
import json

def create_json_for_conversion(
    dataset_dir_path: str,
    format="png",
):
    """Executes the conversion of the OpenScore-Lieder corpus for scores from .mscx format."""

    conversion_list = []

    # Walk through the directory
    for root, dirs, files in os.walk(dataset_dir_path):
        for file in files:
            # Check for .mscx files
            if file.endswith('.mscx'):
                # Construct the full paths for input and output files
                in_path = os.path.join(root, file)
                out_path = in_path.replace(".mscx", ("." + format)).replace("mscx_scores", format + "_files")

                
                # Add to conversion list
                conversion_list.append({
                    "in": in_path,
                    "out": out_path
                })
    
    output_json_path = os.path.join(dataset_dir_path + "\\..", "corpus_conversion2" + format + ".json")

    with open(output_json_path, 'w') as json_file:
        json.dump(conversion_list, json_file, indent=4)

    return

    # create the conversion json file
    conversion = []
    for score_id, score in scores.items():
        score_folder = os.path.join(
            LIEDER_CORPUS_PATH, "scores", score["path"]
        )
        out_path = os.path.join(score_folder, f"lc{score_id}.{format}")

        # skip already exported files
        if soft:
            if os.path.isfile(out_path):
                continue
            if os.path.isfile(out_path.replace(f".{format}", f"-1.{format}")):
                continue
            if os.path.isfile(out_path.replace(f".{format}", f"-01.{format}")):
                continue

        conversion.append({
            "in": os.path.join(score_folder, f"lc{score_id}.mscx"),
            "out": out_path
        })
    
    if len(conversion) == 0:
        return
    
    # run musescore conversion
    tmp = tempfile.NamedTemporaryFile(mode="w", delete=False)
    try:
        json.dump(conversion, tmp)
        tmp.close()

        # clear musescore settings, since it may remember not to print
        # page and system breaks, but we do want those to be printed
        assert os.system(
            f"rm -f ~/.config/MuseScore/MuseScore3.ini"
        ) == 0

        assert os.system(
            f"{MSCORE} -j \"{tmp.name}\""
        ) == 0
    finally:
        tmp.close()
        os.unlink(tmp.name)
