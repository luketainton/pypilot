#!/usr/bin/env python3

import ipaddress
import requests
import socket


def is_ip_address(query: str) -> bool:
    try:
        ipaddress.ip_address(query)
        return True
    except ValueError:
        return False


def resolve_domain_name(domain_name: str) -> ipaddress.IPv4Address:
    try:
        ip = socket.gethostbyname(domain_name)
    except socket.gaierror:
        ip = None
    return ip


def get_public_ip() -> ipaddress.IPv4Address:
    ip = requests.get("https://api.ipify.org").text
    return ip
