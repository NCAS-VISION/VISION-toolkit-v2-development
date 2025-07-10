"""Python packaging setup for the VISION TOOLKIT package."""

from setuptools import find_packages, setup


def get_dependencies():
    """Get dependencies for the package, listed in 'requirements.txt'."""
    requirements = open("requirements.txt", "r")
    return requirements.read().splitlines()


long_description = (
    "End-to-end model-to-observational field co-location for flight, "
    "satellite and other observational data using cf-python and cf-plot, "
    "for the TWINE-funded (NCAS-)VISION project."
)


tests_require = ()
extras_require = {
    "plotting": [
        "cf-plot>=3.4.0",
    ],
    "documentation": [
        "sphinx",
        "shibuya",  # chosen and configured docs theme
    ],
    "pre_commit_hooks": [
        "pre-commit",
        "black",
        "flake8",
    ],
}


# TODO: flesh out author details including emails, etc.
setup(
    name="vision-toolkit",
    description=(
        "Virtual Integration of Satellite and In-Situ "
        "Observation Networks (VISION) toolkit simulator"
    ),
    url="https://github.com/NCAS-VISION/VISION-toolkit-v2-development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="National Centre for Atmospheric Science",
    version="2.0.0.dev1",
    python_requires=">=3.10",
    install_requires=get_dependencies(),
    # tests_require=tests_require,  # TODO add when add tests
    extras_require=extras_require,
    packages=[
        "visiontoolkit",
        "visiontoolkit.plugins",
    ],
    entry_points={
        "console_scripts": ["visiontoolkit = visiontoolkit.visiontoolkit:main"]
    },
    keywords=[
        "modelling",
        "modeling",
        "observations",
        "data",
        "science",
        "oceanography",
        "meteorology",
        "climate",
        "weather",
        "space",
        "cf",
        "netcdf",
        "UM",
    ],
    classifiers=[
        # For lits of possibilities, see: https://pypi.org/classifiers/
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        # "License :: ???",  # TODO: add when add license
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Hydrology",
        "Topic :: Scientific/Engineering :: Oceanography",
        "Topic :: Utilities",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
