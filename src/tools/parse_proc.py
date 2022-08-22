from __future__ import annotations

from pathlib import Path


def parse_proc_info(filepath: str | Path) -> list[dict[str, str]]:
    info_list = []
    for section in Path(filepath).read_text().split('\n\n'):
        info: list[list[str]] = [ln.split(':', 1) for ln in section.splitlines()]
        info: dict[str, str] = {s[0].strip('\t '): s[1].strip() for s in info if len(s) == 2}
        if info:
            info_list.append(info)
    return info_list
