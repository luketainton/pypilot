#!/usr/bin/env python3

import ipaddress
import requests
import socket


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
        ip = socket.gethostbyname(domain_name)
    except socket.gaierror:
        ip = None
    return ip


def get_public_ip() -> ipaddress.IPv4Address:
    """Get the user's current public IPv4 address."""
    ip = requests.get("https://api.ipify.org").text
    return ip
