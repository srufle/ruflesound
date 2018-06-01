import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ruflesound",
    version="0.0.3",
    author="Stephen Rufle",
    author_email="srufle@gmail.com",
    description="An example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/srufle/ruflesound",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)