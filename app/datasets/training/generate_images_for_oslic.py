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
    os.system(f"\"C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe\" -j {json_path}")    #NOTE: nezmenit cestu na univerzalni. proste takhle ted. jde to nejak nezavisle na OS?

def create_json_for_conversion(
    dataset_dir_path: str,
    format="png",
) -> str:
    """ Create a JSON file for the conversion of all .mscx files in the dataset directory to the specified format. """
    conversion_list = []

    mscx_files = list(Path(dataset_dir_path).glob("**/*.mscx"))    
    mscx_files.sort() # Sort files if not in the same directory

    for in_path in mscx_files:
        # Construct the full paths for input and output files
        out_path = in_path.with_suffix(f".{format}") 

        # Add to conversion list
        conversion_list.append({
            "in": str(in_path),
            "out": str(out_path)
        })
    
    output_json_path = Path(dataset_dir_path, f"tmp_{format}.json")

    with open(output_json_path, 'w') as json_file:
        json.dump(conversion_list, json_file, indent=4)
    
    return output_json_path
