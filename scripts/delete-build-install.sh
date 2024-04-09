rm -rf build
rm -rf dist
rm -rf src/pinjet_common.egg-info

which python

python setup.py sdist bdist_wheel

pip install --force-reinstall dist/*.whl
