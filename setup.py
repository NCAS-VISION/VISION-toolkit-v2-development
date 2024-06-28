"""Python packaging setup for the VISION TOOLKIT package."""
import io
import os
from setuptools import find_packages, setup


# TODO 1: add further information typical for a setup.py, esp. dependency
# requirements and package data, but also extras such as keywords,
# platforms, etc.
# TODO 2: flesh out author details including emails, etc.
setup(
    name="vision-toolkit",
    description=(
        "Virtual Integration of Satellite and In-Situ "
        "Observation Networks (VISION) toolkit flight simulator"
    ),
    url="TODO",
    long_description="TODO",
    long_description_content_type="text/markdown",
    author="NCAS, TODO",
    version="0.1",  # TODO 3: set this when ready, currently pre-release/beta
    python_requires=">=3.10",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "visiontoolkit = visiontoolkit.__main__:main"
        ]
    },
)
