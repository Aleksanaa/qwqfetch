from .command import run_command


def process(command):
    result = run_command("wmic %s" % command).read()
    for key, val in {"  ": " ", "\n ": "\n", " \n": "\n", "\n\n": "\n"}.items():
        while key in result:
            result = result.replace(key, val)
    return result.split("\n")[1]
