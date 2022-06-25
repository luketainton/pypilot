#!/usr/bin/env python3

from app.query_normalisation import is_ip_address, resolve_domain_name, get_public_ip


def test_is_ip_address_true() -> None:
    test_query = "1.2.3.4"
    assert is_ip_address(test_query)


def test_is_ip_address_false_ip() -> None:
    test_query = "256.315.16.23"
    assert not is_ip_address(test_query)


def test_is_ip_address_false_fqdn() -> None:
    test_query = "google.com"
    assert not is_ip_address(test_query)


def test_resolve_domain_name_true() -> None:
    domain_name = "one.one.one.one"
    expected_results = ["1.1.1.1", "1.0.0.1"]  # Could resolve to either IP
    assert resolve_domain_name(domain_name) in expected_results


def test_resolve_domain_name_false() -> None:
    domain_name = "hrrijoresdo.com"
    assert not resolve_domain_name(domain_name)


def test_get_public_ip() -> None:
    public_ip = get_public_ip()
    assert is_ip_address(public_ip)
