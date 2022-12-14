def get_from_lspci():
    try:
        from ...tools import RunCommand

        lspci = RunCommand("lspci -mm").readlines()
        for line in lspci:
            if '"VGA compatible controller"' in line:
                line_list = line.split('" "')
                if "[" and "]" in line_list[1]:
                    manufacturer = (
                        line_list[1].strip('"').split("[", 1)[1].split("]")[0]
                    )
                    manufacturer = manufacturer.replace("/", " ")
                else:
                    manufacturer = line_list[1]
                name = line_list[2].split('"')[0]
                return f"{manufacturer} {name}".strip()
        return ""
    except IndexError:
        return ""


def get_from_glxinfo():
    try:
        from ...tools.command import RunCommand

        glxinfo = RunCommand("glxinfo -B").readlines()
        for line in glxinfo:
            if "Device: " in line:
                name = line.split(": ", 1)[1].split(" (", 1)[0]
                return name
        return ""
    except IndexError:
        return ""


gpu_info = ""
for method in [get_from_lspci, get_from_glxinfo]:
    result = method()
    if result:
        gpu_info = result
        break
