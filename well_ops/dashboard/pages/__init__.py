from .about import about
from .index import index
from .settings.profile import profile
from .settings.settings import settings
from .tools.index import index as tools_index
from .tools.stamp import stamp as tools_stamp
from .table import table

__all__ = [
    "about",
    "index",
    "profile",
    "settings",
    "table",
    "tools_index",
    "tools_stamp",
]