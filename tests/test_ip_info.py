#!/usr/bin/env python3

from app.ip_info import (
    get_ip_information,
    get_autonomous_system_number,
    get_prefix_information,
)


def test_get_ip_information() -> None:
    test_query = "1.2.3.4"
    ip_info = get_ip_information(test_query)
    assert ip_info.get("status") == "success" and ip_info.get("query") == test_query


def test_get_autonomous_system_number() -> None:
    as_info = "AS5089 Virgin Media Limited"
    as_number = get_autonomous_system_number(as_info)
    assert as_number == "AS5089"


def test_get_prefix_information() -> None:
    autonomous_system = "AS109"
    prefixes = get_prefix_information(autonomous_system)
    assert "144.254.0.0/16" in prefixes
