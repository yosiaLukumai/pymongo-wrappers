from setuptools import setup, find_packages
import codecs
import os

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


# Setting up
setup(
    name = 'PyDbSchema',
    version = "0.0.5",
    author = "Yosia Lukumai",
    author_email = "yosialukumai@gmail.com",
    url ='https://github.com/yosiaLukumai/pymongo-wrappers',
    description ="PyMongoose enable you to validate your SChema and setting them default values it Give you Schema Object that give you easier accesbility of pymongo collection ",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license = "MIT",
    install_requires = ['pymongo >= 3.0'],
    packages=find_packages(),
    keywords=['pythonmongodb', 'py_mongoose', 'Py_Mongoose', 'mongoosepy', 'pymongo', 'Schemavalidator', 'ShemaChecker'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)