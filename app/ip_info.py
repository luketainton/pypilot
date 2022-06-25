#!/usr/bin/env python3

import ipaddress
import requests


def get_ip_information(ipv4_address: ipaddress.IPv4Address) -> dict:
    """Retrieves information about a given IPv4 address from IP-API.com."""
    api_endpoint = "http://ip-api.com/json/{}".format(ipv4_address)
    resp = requests.get(api_endpoint).json()
    return resp


def get_autonomous_system_number(as_info: str) -> str:
    """Parses AS number from provided AS information."""
    as_number = as_info.split(" ")[0]
    return as_number


def get_prefix_information(autonomous_system: int) -> list:
    """Retrieves prefix information about a given autonomous system."""
    api_endpoint = "https://api.hackertarget.com/aslookup/?q={}".format(
        str(autonomous_system)
    )
    resp = requests.get(api_endpoint).text
    prefixes = resp.split("\n")
    prefixes.pop(0)
    return prefixes
