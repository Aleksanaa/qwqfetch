def parse_proc_info(filepath,needed=[]):
    info_list = []
    for raw_info_list in open(filepath).read().split("\n\n"):
        info_dict = {}
        for per_info in raw_info_list.split("\n"):
            pair = per_info.split(":", 1)
            if len(pair) == 2:
                info_dict[pair[0].strip("\t ")] = pair[1].strip()
        if info_dict != {}:
            info_list.append(info_dict)
    return info_list