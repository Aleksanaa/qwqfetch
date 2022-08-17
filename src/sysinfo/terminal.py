from psutil import Process

terminal = ""

for parents in Process().parents():
    name = parents.name()
    if not (
        name.endswith("sh")
        or name.endswith("shell")
        or name.startswith("python")
        or name in ["nu", "su", "sudo", "doas", "screen", "hyfetch", "tmux"]
    ):
        terminal = name
        break
