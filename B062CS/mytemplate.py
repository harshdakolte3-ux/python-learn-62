import os
from pathlib import Path
project_name = 'temp'
list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/input/data.csv",
    f"{project_name}/source/__train__.py",
    f"{project_name}/source/__predict__.py",
    f"{project_name}/source/__modelselection__.py",
    f"{project_name}/source/tunemodel.py",
    f"{project_name}/source/__utlis__.py",
    f"{project_name}/models/model1.pkl",
    f"{project_name}/models/model2.pkl",
    f"{project_name}/notebook/exploratoion.ipynb",
    f"{project_name}/Readme.md",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",

]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

        if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w")as f:
                pass
        
