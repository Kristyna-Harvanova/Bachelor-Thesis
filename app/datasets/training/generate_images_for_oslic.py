import os
import json

def convert_mscx2format(
    dataset_dir_path: str, 
    format: str = "png"):
    """ Convert all .mscx files in the dataset directory to the specified format. """

    # Create a JSON file for the conversion
    json_path = create_json_for_conversion(dataset_dir_path, format)

    # Run the conversion
    os.system(f"\"C:\\Program Files\\MuseScore 3\\bin\\MuseScore3.exe\" -j {json_path}")

    # Remove the JSON file
    #os.remove(json_path)   #TODO: remove

    #TODO: od Kinkel, 2. jsou svg prazdne
    #TODO: vytvorilo se pouze do G. Mahler, 5. dalsi uz ne

def create_json_for_conversion(
    dataset_dir_path: str,
    format="png",
):
    """ Create a JSON file for the conversion of all .mscx files in the dataset directory to the specified format. """
    conversion_list = []

    # Walk through the directory
    for root, dirs, files in os.walk(dataset_dir_path):
        for file in files:
            # Check for .mscx files
            if file.endswith('.mscx'):
                # Construct the full paths for input and output files
                in_path = os.path.join(root, file)
                out_path = in_path.replace(".mscx", ("." + format))#.replace("mscx_scores", format + "_files")

                # Add to conversion list
                conversion_list.append({
                    "in": in_path,
                    "out": out_path
                })
    
    output_json_path = os.path.join(dataset_dir_path + "\\tmp_" + format + ".json")

    with open(output_json_path, 'w') as json_file:
        json.dump(conversion_list, json_file, indent=4)
    
    return output_json_path
