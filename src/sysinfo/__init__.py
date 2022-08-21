import os
from multiprocessing.pool import ThreadPool

from .board_name import get_host
from .cpu_info import get_cpu
from .desktop_environment import get_de
from .gpu_info import get_gpu
from .kernel import get_kernel
from .memory import get_ram
from .os_info import get_os
from .package_count import get_pkg
from .resolution import get_res
from .shell import get_shell
from .system_theme import get_theme
from .terminal import get_term
from .uptime import get_uptime
from .username import get_username

use_threading = True

functions_list = [get_username, get_os, get_host, get_kernel, get_uptime, get_pkg, get_shell,
                  get_res, get_de, get_theme, get_term, get_cpu, get_gpu, get_ram]


def run() -> dict[str, str]:
    with ThreadPool(os.cpu_count()) as p:
        return {k: v for d in p.map(lambda f: f(), functions_list) for k, v in d.items()}
