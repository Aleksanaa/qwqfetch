from ctypes import windll 

uptime = windll.kernel32.GetTickCount64()
uptime_seconds = int(str(uptime)[:-3])
