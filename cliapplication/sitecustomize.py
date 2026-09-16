import sys
from pathlib import Path

modules_dir = Path(__file__).resolve().parent / "modules"
modules_dir_str = str(modules_dir)

if modules_dir_str not in sys.path:
    sys.path.insert(0, modules_dir_str)
