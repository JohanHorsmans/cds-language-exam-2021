#!/usr/bin/env bash

VENVNAME=lang_venv

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

pip install ipython
pip install jupyter

# Loading these here, since they are giving trouble in the requirements.txt
pip install matplotlib
pip install opencv-python
pip install pydot
pip install pydotplus
pip install graphviz

python -m ipykernel install --user --name=$VENVNAME

test -f requirements.txt && pip install -r requirements.txt

deactivate
echo "build $VENVNAME"
