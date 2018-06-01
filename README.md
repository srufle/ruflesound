# Rufle Sound

An example package to use for 
[Packaging Tutorial](https://packaging.python.org/tutorials/packaging-projects/)


```
python -m pip install --user --upgrade setuptools wheel
python -m pip install --user --upgrade twine
```

```
python setup.py sdist bdist_wheel

set TWINE_USERNAME=srufle
set TWINE_PASSWORD=[secret]
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```