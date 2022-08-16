def _init():
    global _global_dict
    _global_dict = {}


def set(new_dict: dict) -> None:
    merge(new_dict, _global_dict)


def merge(new_dict: dict, old_dict: dict):
    for key in new_dict.keys():
        if isinstance(key, str):
            if (
                isinstance(new_dict[key], dict)
                and key in old_dict.keys()
                and isinstance(old_dict[key], dict)
            ):
                merge(new_dict[key], old_dict[key])
            elif new_dict[key] != ("" or None):
                old_dict[key] = new_dict[key]


def get(keys: list):
    result = []
    for key in keys:
        if isinstance(key, str):
            result.append(_global_dict[key])
    return result


def delete(keys: list):
    for key in keys:
        if isinstance(key, str):
            del _global_dict[key]
