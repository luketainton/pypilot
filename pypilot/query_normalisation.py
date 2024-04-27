#!/usr/bin/env python3

"""MODULE: Provides functions that ensure an IP address is
available to query the APIs for."""

import ipaddress
import socket

import requests


def is_ip_address(query: str) -> bool:
    """Verifies if a given query is a valid IPv4 address."""
    try:
        ipaddress.ip_address(query)
        return True
    except ValueError:
        return False


def resolve_domain_name(domain_name: str) -> ipaddress.IPv4Address | None:
    """Resolve a domain name via DNS or return None."""
    try:
        result: str = socket.gethostbyname(domain_name)
        ip_address: ipaddress.IPv4Address = ipaddress.IPv4Address(result)
        return ip_address
    except (socket.gaierror, ipaddress.AddressValueError):
        return None


def get_public_ip() -> ipaddress.IPv4Address:
    """Get the user's current public IPv4 address."""
    ip_address: str = requests.get("https://api.ipify.org", timeout=10).text
    return ipaddress.IPv4Address(ip_address)
