#!/usr/bin/env python3

"""MODULE: Provides functions that ensure an IP address is available to query the APIs for."""

import socket
import ipaddress
import requests


def is_ip_address(query: str) -> bool:
    """Verifies if a given query is a valid IPv4 address."""
    try:
        ipaddress.ip_address(query)
        return True
    except ValueError:
        return False


def resolve_domain_name(domain_name: str) -> ipaddress.IPv4Address:
    """Resolve a domain name via DNS or return None."""
    try:
        ip_address = socket.gethostbyname(domain_name)
    except socket.gaierror:
        ip_address = None
    return ip_address


def get_public_ip() -> ipaddress.IPv4Address:
    """Get the user's current public IPv4 address."""
    ip_address = requests.get("https://api.ipify.org").text
    return ip_address
