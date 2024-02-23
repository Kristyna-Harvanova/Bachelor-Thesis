import os
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
