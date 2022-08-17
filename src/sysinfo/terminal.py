from ..tools import get_parents

terminal = ""

for name in get_parents():
    if not (
        name.endswith("sh")
        or name.endswith("shell")
        or name.startswith("python")
        or name in ["nu", "su", "sudo", "doas", "screen", "hyfetch", "tmux"]
    ):
        terminal = name
        break