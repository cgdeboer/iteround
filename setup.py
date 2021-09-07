import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iteround",
    version="1.0.3",
    author="Calvin DeBoer",
    author_email="cgdeboer@gmail.com",
    description=("Rounds iterables (arrays, lists, sets, etc) "
                 "while maintaining the sum of the initial array."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cgdeboer/iteround",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
