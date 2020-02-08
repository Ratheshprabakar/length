import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="length",
    version="1.0.1",
    author="Rathesh Prabakar",
    author_email="ratheshprabakar@gmail.com",
    description="A package to count the number of digits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ratheshprabakar/length",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.2',
)
