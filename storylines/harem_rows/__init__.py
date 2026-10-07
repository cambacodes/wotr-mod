"""Auto-discovered harem row modules; each exposes register(payload, scenes, refs)."""
import importlib
import pkgutil


def register_all(payload, scenes, refs):
    for info in sorted(pkgutil.iter_modules(__path__), key=lambda m: m.name):
        importlib.import_module(__name__ + "." + info.name).register(payload, scenes, refs)
