import playlists
import metadata
from cli import get_current_video_id


def get_query(query: str) -> list[str]:
    
    components = list(map(lambda part: part.split(":"), query.split(",")))

    match components:
        case [["current"]]:
            return [get_current_video_id()]

        case [["parse", link]]:
            pass

        case [["id", video_id]]:
            return [video_id]

        case _:
            all_metadata = metadata.load_all_video_metadata()

            set = []
            
            # Filter by playlists
            playlist_filters = list(filter(lambda component: component[0] == "in", components))
            if len(playlist_filters) == 0:
                set = list(all_metadata.keys())
            else:
                initial_filter = playlist_filters[0]
                other_filters = playlist_filters[1:]
                set = playlists.load_playlist(initial_filter[1])
                for other_filter in other_filters:
                    set = filter(lambda video_id: video_id in playlists.load_playlist(other_filter[1]), set)
                set = list(set)
            

            def matches_metadata(video_id: str, attribute_name: str, attribute_value: str) -> bool:
                md: dict = all_metadata[video_id]
                key_exists = attribute_name in md.keys()
                if key_exists:
                    if md[attribute_name] == None:
                        return False
                    matches = attribute_value.lower() in md[attribute_name].lower()
                    return matches
                else:
                    return False

            # Filter by artist
            artist_filters = filter(lambda component: component[0] == "by", components)
            for artist_filter in artist_filters:
                matches_title = lambda video_id: matches_metadata(video_id, "title", artist_filter[1])
                matches_channel = lambda video_id: matches_metadata(video_id, "channel", artist_filter[1])
                set = filter(lambda video_id: matches_channel(video_id) or matches_title(video_id), set)
            set = list(set)

            # Filter by other metadata
            SPECIAL_KEYS = [
                "in",
                "by",
                "parse",
                "id",
                "auto",
                "all",
            ]
            metadata_filters = filter(lambda component: component[0] not in SPECIAL_KEYS, components)
            for metadata_filter in metadata_filters:
                set = filter(lambda video_id: matches_metadata(video_id, metadata_filter[0], metadata_filter[1]), set)
            set = list(set)

            return set




