#!/usr/bin/env bash

pylint --recursive=yes --output-format=parseable --output=lintreport.txt . || pylint-exit $?
