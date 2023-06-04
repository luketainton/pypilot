#!/usr/bin/env python3

"""MODULE: Provides test cases for app/query_normalisation.py."""

from app.query_normalisation import (  # pragma: no cover
    get_public_ip,
    is_ip_address,
    resolve_domain_name,
)


def test_is_ip_address_true() -> None:
    """TEST: Verifies if a given query is a valid IPv4 address."""
    test_query = "1.2.3.4"
    assert is_ip_address(test_query)


def test_is_ip_address_false_ip() -> None:
    """TEST: Verifies that None is returned if an invalid IP is given."""
    test_query = "256.315.16.23"
    assert not is_ip_address(test_query)


def test_is_ip_address_false_fqdn() -> None:
    """TEST: Verifies that None is returned if a domain name is given."""
    test_query = "google.com"
    assert not is_ip_address(test_query)


def test_resolve_domain_name_true() -> None:
    """TEST: Verifies that DNS resolution is working correctly."""
    domain_name = "one.one.one.one"
    expected_results: list[str] = ["1.1.1.1", "1.0.0.1"]  # Could resolve to either IP
    assert str(resolve_domain_name(domain_name)) in expected_results


def test_resolve_domain_name_false() -> None:
    """TEST: Verifiees that a non-existent domain is not resolved."""
    domain_name = "hrrijoresdo.com"
    assert not resolve_domain_name(domain_name)


def test_get_public_ip() -> None:
    """TEST: Verifies that the current public IP is retrieved correctly."""
    public_ip = get_public_ip()
    assert is_ip_address(public_ip)
