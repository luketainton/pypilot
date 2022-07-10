#!/usr/bin/env python3

"""MODULE: Provides test cases for app/print_table.py."""

from app.print_table import generate_prefix_string  # pragma: no cover


def test_generate_prefix_string_small() -> None:
    """TEST: Verifies if a small prefix list results in one line."""
    test_query = ["abc", "def"]
    result = generate_prefix_string(prefixes=test_query)
    assert result == "abc, def\n"


def test_generate_prefix_string_large() -> None:
    """TEST: Verifies if a large prefix list results in multiple lines."""
    test_query = ["abc", "def", "ghi", "jkl", "mno", "pqr"]
    result = generate_prefix_string(prefixes=test_query)
    assert result == "abc, def, ghi, jkl\nmno, pqr\n"
