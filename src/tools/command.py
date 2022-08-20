from sys import stdout
import subprocess
from shlex import split


class run_command:
    def __init__(self, command: str, error=False):
        encoding = stdout.encoding
        try:
            result_object = subprocess.run(
                split(command),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            if (result_object.returncode == 0) is not error:
                self.result = result_object.stdout.decode(encoding)
            else:
                self.result = ""
        except (FileNotFoundError, AttributeError):
            self.result = ""

    def read(self):
        return self.result

    def readline(self):
        return self.result.split("\n", 1)[0]

    def readlines(self):
        return self.result.split("\n")
