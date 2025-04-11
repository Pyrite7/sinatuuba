import json
import config




def load_all_video_metadata() -> dict:
    with open(config.METADATA_PATH, "r") as file:
        return json.load(file)["video_data"]

def overwrite_all_video_metadata(metadata: dict):
    with open(config.METADATA_PATH, "r") as file:
        all_data = json.load(file)
    
    all_data["video_data"] = metadata

    with open(config.METADATA_PATH, "w") as file:
        json.dump(all_data, file, indent=4)





def load_video_metadata(video_id: str) -> dict:
    all_metadata = load_all_video_metadata()
    if video_id in all_metadata.keys():
        return load_all_video_metadata()[video_id]
    else:
        return {}


def write_video_metadata(video_id: str, metadata: str):
    data = load_all_video_metadata()
    
    data[video_id] = metadata

    overwrite_all_video_metadata(data)


def write_video_metadata_fields(video_id: str, metadata: dict):
    """
    Like write_video_metadata, mut adds/overwrites the only fields present in metadata.
    NOTE: this method is NOT recursive!!!
    """

    data = load_all_video_metadata()
    
    for key in metadata.keys():
        data[video_id][key] = metadata[key]
    
    overwrite_all_video_metadata(data)




