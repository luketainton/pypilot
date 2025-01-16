#!/usr/bin/env python3

"""MODULE: Provides test cases for app/ip_info.py."""

import requests_mock

from app.ip_info import (  # pragma: no cover
    get_autonomous_system_number,
    get_ip_information,
    get_prefix_information,
)


def test_get_ip_information() -> None:
    """TEST: ensure that the IP information API is working correctly."""
    test_query: str = "1.2.3.4"
    ip_info = get_ip_information(test_query)
    assert ip_info.get("status") == "success" and ip_info.get("query") == test_query


def test_get_ip_information_broken_api_response() -> None:
    """TEST: ensure that None is returned if the IP API response is broken."""
    test_query = "1.2.3.4"
    with requests_mock.Mocker() as mocker:
        mocker.get(f"http://ip-api.com/json/{test_query}", text="error")
        resp = get_ip_information(test_query)
        assert not resp


def test_get_ip_information_bad_response() -> None:
    """TEST: ensure that None is returned if the IP API returns code 404."""
    test_query = "1.2.3.4"
    with requests_mock.Mocker() as mocker:
        mocker.get(f"http://ip-api.com/json/{test_query}", status_code=404)
        resp = get_ip_information(test_query)
        assert not resp


def test_get_autonomous_system_number() -> None:
    """TEST: ensure that AS information is parsed into AS number correctly."""
    as_info = "AS5089 Virgin Media Limited"
    as_number: str = get_autonomous_system_number(as_info)
    assert as_number == "AS5089"


def test_get_prefix_information() -> None:
    """TEST: ensure that advertised prefixes are retrieved correctly."""
    autonomous_system = "AS109"
    prefixes = get_prefix_information(autonomous_system)
    assert "144.254.0.0/16" in prefixes


def test_get_prefix_information_broken_api_response() -> None:
    """TEST: ensure that None is returned if the prefix API response is broken."""
    autonomous_system = "AS109"
    with requests_mock.Mocker() as mocker:
        mocker.get(
            f"https://api.hackertarget.com/aslookup/?q={str(autonomous_system)}",
            text="error",
        )
        resp = get_prefix_information(autonomous_system)
        assert not resp


def test_get_prefix_information_bad_response() -> None:
    """TEST: ensure that None is returned if the prefix API returns code 404."""
    autonomous_system = "AS109"
    with requests_mock.Mocker() as mocker:
        mocker.get(
            f"https://api.hackertarget.com/aslookup/?q={str(autonomous_system)}",
            status_code=404,
        )
        resp = get_prefix_information(autonomous_system)
        assert not resp
