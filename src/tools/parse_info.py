from __future__ import annotations

# It is used to deal with this kind of strings:

# Name: Arch Linux
# Arch: x86_64
# Version:  Rolling

# or

# Name=Arch Linux
# Arch=x86_64
# Version=Rolling

# And if you need Name and Arch:
# needs = {"Name":"name","Arch":"arch"}
# It will output {"name":"Arch Linux","arch":"x86_64"}


def parser(inputs: str, needs: dict[str, str], separator: str) -> dict[str, str]:
    satisfied = {key: "" for key in needs.values()}
    for line in inputs.split("\n"):
        for key, val in needs.items():
            if line.strip().startswith(key):
                line_list = line.split(separator, 1)
                if line_list[0].strip() == key:
                    satisfied[val] = line_list[1].strip()
                    needs.pop(key)
                    break
    return satisfied
