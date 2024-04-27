#!/usr/local/bin/python3

"""MODULE: Main application module."""

import sys

from ipilot.args import parse_args
from ipilot.ip_info import (
    get_autonomous_system_number,
    get_ip_information,
    get_prefix_information,
)
from ipilot.print_table import generate_prefix_string, print_table
from ipilot.query_normalisation import is_ip_address, resolve_domain_name

HEADER = """-----------------------------------------------
| IP Address Information Lookup Tool (iPilot) |
|       By Luke Tainton (@luketainton)        |
-----------------------------------------------\n"""


def main() -> None:
    """Main function.
    
    Args:
        None
    
    Returns:
        None
    """
    args = parse_args()
    if not args.noheader:
        print(HEADER)

    # Set IP to passed IP address, or resolve passed domain name to IPv4
    ip_address = resolve_domain_name(args.query) if not is_ip_address(args.query) else args.query

    # If not given an IPv4, and can't resolve to IPv4, then throw error and exit
    if not ip_address:
        print("ERROR: could not resolve query to IPv4 address.")
        sys.exit(1)

    # Get information from API
    ip_info: dict | None = get_ip_information(ip_address)
    if not ip_info:
        print("ERROR: could not retrieve IP information from API.")
        sys.exit(1)
    as_number: str = get_autonomous_system_number(ip_info["as"])

    # Assemble list for table generation
    country: str = ip_info["country"]
    region: str = ip_info["regionName"]
    city: str = ip_info["city"]
    table_data: list = [
        ["IP Address", ip_info["query"]],
        ["Organization", ip_info["org"]],
        ["Location", f"{country}/{region}/{city}"],
        ["Timezone", ip_info["timezone"]],
        ["Internet Service Provider", ip_info["isp"]],
        ["Autonomous System", as_number],
    ]

    # If wanted, get prefix information
    if args.prefixes:
        prefix_info = get_prefix_information(as_number)
        if not prefix_info:
            print("ERROR: could not retrieve prefix information from API.")
            sys.exit(1)
        else:
            table_data.append(["Prefixes", generate_prefix_string(prefix_info)])

    print_table(table_data)


if __name__ == "__main__":
    main()
