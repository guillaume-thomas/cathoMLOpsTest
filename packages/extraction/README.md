Module d'extraction des images depuis des pdfs. Utilsé notamment pour le labelling.

cd packages

pip install --upgrade pip
pip install --upgrade setuptools wheel

pip install -e extraction

cd extraction
python setup.py sdist bdist_wheel
cd dist