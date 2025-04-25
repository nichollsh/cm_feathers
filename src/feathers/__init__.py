from __future__ import annotations

from .feathers import _register_all, get_cmap, list_cmaps

__version__ = "25.04.30"

__all__ = ["get_cmap", "list_cmaps"]

_register_all()
