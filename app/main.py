#!/usr/local/bin/python3

"""MODULE: Main application module."""

import sys

from app.args import parse_args
from app.print_table import print_table, generate_prefix_string
from app.query_normalisation import is_ip_address, resolve_domain_name
from app.ip_info import (  # pragma: no cover
    get_ip_information,
    get_autonomous_system_number,
    get_prefix_information,
)


HEADER = """-----------------------------------------------
| IP Address Information Lookup Tool (iPilot) |
|       By Luke Tainton (@luketainton)        |
-----------------------------------------------\n"""


def main():
    """Main function."""
    args = parse_args()
    if not args.noheader:
        print(HEADER)

    # Set IP to passed IP address, or resolve passed domain name to IPv4
    ip_address = (
        resolve_domain_name(args.query) if not is_ip_address(args.query) else args.query
    )

    # If not given an IPv4, and can't resolve to IPv4, then throw error and exit
    if not ip_address:
        print("ERROR: could not resolve query to IPv4 address.")
        sys.exit(1)

    # Get information from API
    ip_info = get_ip_information(ip_address)
    as_number = get_autonomous_system_number(ip_info.get("as"))

    # Assemble list for table generation
    table_data = [
        ["IP Address", ip_info.get("query")],
        ["Organization", ip_info.get("org")],
        [
            "Location",
            f"{ip_info.get('country')}/{ip_info.get('regionName')}/{ip_info.get('city')}",
        ],
        ["Timezone", ip_info.get("timezone")],
        ["Internet Service Provider", ip_info.get("isp")],
        ["Autonomous System", as_number],
    ]

    # If wanted, get prefix information
    if args.prefixes:
        prefix_info = get_prefix_information(as_number)
        table_data.append(["Prefixes", generate_prefix_string(prefix_info)])

    print_table(table_data)


if __name__ == "__main__":
    main()
