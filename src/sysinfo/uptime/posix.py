import psutil
import time

uptime_seconds = int(time.time() - psutil.boot_time())
