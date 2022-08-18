# __init__ file
from .parse_proc import parse_proc_info as parse_proc
from .get_parents import get as get_parents
from .get_wmic_value import process as get_wmic

__all__ = [parse_proc, get_parents, get_wmic]
