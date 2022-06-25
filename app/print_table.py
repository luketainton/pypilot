#!/usr/bin/env python3

from tabulate import tabulate


def generate_prefix_string(prefixes: list) -> str:
    n = 4
    try:
        ret = ""
        for i in range(0, len(prefixes), n):
            ret += ", ".join(prefixes[i : i + n]) + "\n"
        return ret
    except AttributeError:
        return None


def print_table(table_data) -> None:
    print(tabulate(table_data))
