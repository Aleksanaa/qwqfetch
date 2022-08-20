from .command import RunCommand


def process(command):
    result = RunCommand(f"wmic {command}").read()
    for key, val in {"  ": " ", "\n ": "\n", " \n": "\n", "\n\n": "\n"}.items():
        while key in result:
            result = result.replace(key, val)
    return result.split("\n")[1]
