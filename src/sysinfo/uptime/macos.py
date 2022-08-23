from ...tools.command import RunCommand
from time import time

uptime_seconds = int(time()) - int(
    RunCommand("/usr/sbin/sysctl -n kern.boottime").readline().split()[3].strip(",")
)
