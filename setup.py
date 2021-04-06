"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="dependency-extractor",
    version="1.0.0",
    description="A Python library which extracts library dependencies from source files written in most mainstream programming languages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexandrosraikos/dependency-extractor",
    author="Alexandros Raikos",
    author_email="alexandros@araikos.gr",
    classifiers=[  
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="dependencies, static code analysis, setuptools, development",
    # TODO: Decide single file or multifile approach. 
    package_dir={"": "src"},  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where="src"), 
    python_requires=">=3.6, <4",

    # TODO: Decide dependency approach.
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=["peppercorn"],
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    # extras_require={  # Optional
    #     "dev": ["check-manifest"],
    #     "test": ["coverage"],
    # },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    entry_points={
        "console_scripts": [
            "dextractor=dextractor:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/alexandrosraikos/dependency-extractor/issues",
        "Funding": "https://www.araikos.gr/",
        "Say Thanks!": "https://www.araikos.gr/contact",
        "Source": "https://github.com/alexandrosraikos/dependency-extractor/",
    },
)