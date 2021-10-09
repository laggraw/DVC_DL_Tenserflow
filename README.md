# DVC - DL - TF - AIOPS - Demo

### commands

### Create a new env
``` bash
conda create --prefix ./env python=3.7 -y
```

## Activate a new env
``` bash
source activate ./env
```

### init DVC
``` bash
git init
dvc init
```

### Create Empty files -
``` bash
mkdir -p src/utils config
touch src/__init__.py src/utils/__init__.py param.yaml dvc.yaml config/config.yaml src/stage_01_load_save.py src/utils/all_utils.py setup.py .gitignore
```
### install src
``` bash
pip install -e .
```
