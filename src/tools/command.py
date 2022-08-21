from locale import getpreferredencoding
import subprocess
from shlex import split


class RunCommand:
    def __init__(self, command: str, error=False) -> None:
        encoding = getpreferredencoding()
        try:
            result_object = subprocess.run(
                split(command),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            if (result_object.returncode == 0) is not error:
                self.result = result_object.stdout.decode(encoding).strip()
            else:
                self.result = ""
        except (FileNotFoundError, AttributeError):
            self.result = ""

    def read(self) -> str:
        return self.result

    def readline(self) -> str:
        return self.result.split("\n", 1)[0]

    def readlines(self) -> list[str]:
        return self.result.split("\n")
