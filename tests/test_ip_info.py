#!/usr/bin/env python3

"""MODULE: Provides test cases for app/ip_info.py."""

from app.ip_info import (  # pragma: no cover
    get_ip_information,
    get_autonomous_system_number,
    get_prefix_information,
)


def test_get_ip_information() -> None:
    """TEST: ensure that the IP information API is working correctly."""
    test_query = "1.2.3.4"
    ip_info = get_ip_information(test_query)
    assert ip_info.get("status") == "success" and ip_info.get("query") == test_query


def test_get_autonomous_system_number() -> None:
    """TEST: ensure that AS information is parsed into AS number correctly."""
    as_info = "AS5089 Virgin Media Limited"
    as_number = get_autonomous_system_number(as_info)
    assert as_number == "AS5089"


def test_get_prefix_information() -> None:
    """TEST: ensure that advertised prefixes are retrieved correctly."""
    autonomous_system = "AS109"
    prefixes = get_prefix_information(autonomous_system)
    assert "144.254.0.0/16" in prefixes
