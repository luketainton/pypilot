#!/usr/bin/env python3

"""MODULE: Provides functions to call various APIs to retrieve IP/prefix information."""

import ipaddress

import requests


def get_ip_information(ipv4_address: ipaddress.IPv4Address) -> dict | None:
    """Retrieves information about a given IPv4 address from IP-API.com."""
    api_endpoint: str = f"http://ip-api.com/json/{ipv4_address}"
    try:
        resp: requests.Response = requests.get(api_endpoint, timeout=10)
        resp.raise_for_status()
        ret: dict | None = resp.json() if resp.json().get("status") == "success" else None
    except (requests.exceptions.JSONDecodeError, requests.exceptions.HTTPError):
        ret = None
    return ret


def get_autonomous_system_number(as_info: str) -> str:
    """Parses AS number from provided AS information."""
    as_number: str = as_info.split(" ")[0]
    return as_number


def get_prefix_information(autonomous_system: str) -> list | None:
    """Retrieves prefix information about a given autonomous system."""
    api_endpoint: str = f"https://api.hackertarget.com/aslookup/?q={str(autonomous_system)}"
    try:
        resp: requests.Response = requests.get(api_endpoint, timeout=10)
        resp.raise_for_status()
    except requests.exceptions.HTTPError:
        return None
    prefixes: list[str] = resp.text.split("\n")
    prefixes.pop(0)
    return prefixes
