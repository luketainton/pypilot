#!/usr/bin/env python3

"""SETUP: Build application .whl file."""

from setuptools import setup

from pypilot._version import VERSION

dependencies: list = []
with open("requirements.txt", "r", encoding="ascii") as dep_file:
    for dep_line in dep_file.readlines():
        dependencies.append(dep_line.replace("\n", ""))


test_dependencies: list = []
with open("requirements-dev.txt", "r", encoding="ascii") as dep_file:
    for dep_line in dep_file.readlines():
        test_dependencies.append(dep_line.replace("\n", ""))


setup(
    name="ipilot",
    version=VERSION,
    description="IP Information Lookup Tool",
    long_description="IP Information Lookup Tool",
    long_description_content_type="text/x-rst",
    author="Luke Tainton",
    author_email="luke@tainton.uk",
    packages=["app"],
    install_requires=dependencies,
    tests_require=test_dependencies,
    entry_points={
        "console_scripts": [
            "ipilot = pypilot.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Framework :: Pytest",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: Freeware",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: System :: Networking",
    ],
)
