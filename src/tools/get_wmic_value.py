from .command import RunCommand


def process(command: str) -> str:
    result_raw = RunCommand(f"wmic {command}").read()
    result = "\n".join(
        [line.rstrip() for line in result_raw.splitlines() if line.strip()]
    )
    return result.splitlines()[1]