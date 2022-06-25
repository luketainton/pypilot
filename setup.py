#!/usr/bin/env python3

"""SETUP: Build application .whl file."""

from setuptools import setup

from app._version import VERSION

setup(
    name="ipilot",
    version=VERSION,
    description="IP Information Lookup Tool",
    author="Luke Tainton",
    author_email="luke@tainton.uk",
    packages=["ipilot"],
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "ipilot = app.main:main",
        ],
    },
)
