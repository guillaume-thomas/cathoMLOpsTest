python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel

pip install -e packages/inference

cd packages/inference/
python setup.py sdist bdist_wheel
cd dist
cp *.whl ../../../cats_and_dogs/train/packages
cp *.whl ../../../cats_and_dogs/api/packages
cd ../../../

pip install -e packages/extraction

cd packages/extraction/
python setup.py sdist bdist_wheel
cd dist
cp *.whl ../../../cats_and_dogs/label/packages
cp *.whl ../../../cats_and_dogs/api/packages
cd ../../../

pip install -r cats_and_dogs/api/requirements.txt