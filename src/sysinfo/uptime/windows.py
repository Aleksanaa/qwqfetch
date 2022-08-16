from ctypes.windll import kernel32 as lib  # type: ignore

uptime = lib.GetTickCount64()
uptime_seconds = int(str(uptime)[:-3])
