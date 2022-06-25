#!/usr/bin/env python3

"""SETUP: Build application .whl file."""

from setuptools import setup

from app._version import VERSION


dependencies = []
with open("requirements.txt", "r") as dep_file:
    for dep_line in dep_file.readlines():
        dependencies.append(dep_line.replace("\n", ""))


setup(
    name="ipilot",
    version=VERSION,
    description="IP Information Lookup Tool",
    author="Luke Tainton",
    author_email="luke@tainton.uk",
    packages=["app"],
    install_requires=dependencies,
    entry_points={
        "console_scripts": [
            "ipilot = app.main:main",
        ],
    },
)
