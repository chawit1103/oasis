import importlib.util
from pathlib import Path


def test_examples_import_successfully():
    for path in Path("examples").glob("socialsense_*_demo.py"):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        assert hasattr(module, "main")
