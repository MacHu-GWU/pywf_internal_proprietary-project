# -*- coding: utf-8 -*-

import shutil
from pathlib import Path
from pathpick.api import PathPick

path_pick = PathPick.new(
    include=[],
    exclude=[
        ".git",
        ".idea",
        ".venv",
        ".github",
        ".poetry",
        ".pytest_cache",
        "docs/build",
        "build",
        "dist",
        "tmp",
        "htmlcov",
        "__pycache__",
        "genai",
        ".DS_Store",
        ".coverage",
        "index.md",
    ],
)

dir_project_root = Path(__file__).absolute().parent
repo_name = "cookiecutter_pywf_internal_proprietary_demo-project"
dir_src = dir_project_root.parent / repo_name
dir_dst = dir_project_root / repo_name

shutil.rmtree(dir_dst, ignore_errors=True)

for path_src in dir_src.rglob("*"):
    relpath = path_src.relative_to(dir_src)
    if path_src.is_file():
        if path_pick.is_match(str(relpath)):
            path_dst = dir_dst / relpath
            try:
                path_dst.write_bytes(path_src.read_bytes())
            except FileNotFoundError:
                path_dst.parent.mkdir(parents=True, exist_ok=True)
                path_dst.write_bytes(path_src.read_bytes())