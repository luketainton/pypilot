#!/usr/local/env python3

"""MODULE: Provides CLI arguments to the application."""

import argparse

from ipilot.query_normalisation import get_public_ip


def parse_args() -> argparse.Namespace:  # pragma: no cover
    """Get arguments from user via the command line.
    
    Args:
        None
    
    Returns:
        argparse.Namespace: parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Query information about an IP address or domain name."
    )
    parser.add_argument(
        "-q",
        "--query",
        help="IP/domain name to query (default: current public IP)",
        default=get_public_ip(),
    )
    parser.add_argument(
        "-p",
        "--prefixes",
        help="show advertised prefixes",
        action="store_true",
    )
    parser.add_argument(
        "-n",
        "--noheader",
        help="do not print header",
        action="store_true",
    )
    return parser.parse_args()
