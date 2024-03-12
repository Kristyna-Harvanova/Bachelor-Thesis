import os
import json
from pathlib import Path

def convert_mscx2format(
    dataset_dir_path: str, 
    format: str = "png"
):
    """ Convert all .mscx files in the dataset directory to the specified format. """

    # Create a JSON file for the conversion
    json_path = create_json_for_conversion(dataset_dir_path, format)

    # Run the conversion
    os.system(f"\"C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe\" -j {json_path}")    #TODO: zmenit cestu na univerzalni ?? jde to nejak nezavisle na OS?

    # Remove the JSON file
    #os.remove(json_path)   #TODO: remove????, pokud ano, tak pouzit Path.unlink()???????

def create_json_for_conversion(
    dataset_dir_path: str,
    format="png",
) -> str:
    """ Create a JSON file for the conversion of all .mscx files in the dataset directory to the specified format. """
    conversion_list = []

    # Walk through the directory
    for root, dirs, files in os.walk(dataset_dir_path):
        for file in files:
            # Check for .mscx files
            if file.endswith('.mscx'):
                # Construct the full paths for input and output files
                in_path = Path(root, file)              #in_path = os.path.join(root, file) #TODO stejne jako Path.join()?????
                out_path = in_path.with_suffix(f".{format}") #out_path = in_path.replace(".mscx", ("." + format))#.replace("mscx_scores", format + "_files")

                # TODO: ASK, je to v pohode, kdyz nebudou vsechny stranky z .mscx souboru?
                # # Skip already made .format files (there will be maybe some missing pages. xxx-1.format, xxx-2.format, ...)
                # if os.path.exists(out_path) or os.path.exists(out_path.replace(f".{format}", f"-1.{format}")):
                #     continue

                # Add to conversion list
                conversion_list.append({
                    "in": str(in_path),
                    "out": str(out_path)
                })
    
    output_json_path = Path(dataset_dir_path, f"tmp_{format}.json") #output_json_path = os.path.join(dataset_dir_path, "tmp_" + format + ".json")

    with open(output_json_path, 'w') as json_file:
        json.dump(conversion_list, json_file, indent=4)
    
    return output_json_path
