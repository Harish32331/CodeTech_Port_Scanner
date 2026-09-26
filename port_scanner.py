
#!/usr/bin/env python3

import argparse
import socket
from datetime import datetime


def scan_port(target, port, timeout):
    """Attempt a TCP connection to a single port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((target, port))
        return result == 0
    except socket.error:
        return False
    finally:
        sock.close()


def scan_ports(target, start_port, end_port, timeout):
    """Scan a range of TCP ports."""
    print("\n" + "=" * 55)
    print("          CodeTech TCP Port Scanner")
    print("=" * 55)
    print(f"Target : {target}")
    print(f"Ports  : {start_port}-{end_port}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 55)

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port, timeout):
            print(f"[OPEN]   TCP/{port}")
            open_ports.append(port)

    print("-" * 55)

    if open_ports:
        print(f"Open ports found: {len(open_ports)}")
    else:
        print("No open TCP ports found in the selected range.")

    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)

    return open_ports


def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP port scanner for authorized security testing."
    )

    parser.add_argument(
        "target",
        help="Hostname or IP address to scan"
    )

    parser.add_argument(
        "-s",
        "--start",
        type=int,
        default=1,
        help="Starting port (default: 1)"
    )

    parser.add_argument(
        "-e",
        "--end",
        type=int,
        default=1024,
        help="Ending port (default: 1024)"
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=0.5,
        help="Connection timeout in seconds (default: 0.5)"
    )

    args = parser.parse_args()

    if not 1 <= args.start <= 65535:
        parser.error("Starting port must be between 1 and 65535.")

    if not 1 <= args.end <= 65535:
        parser.error("Ending port must be between 1 and 65535.")

    if args.start > args.end:
        parser.error("Starting port cannot be greater than ending port.")

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"[ERROR] Unable to resolve target: {args.target}")
        return

    print(f"\nResolved target: {args.target} -> {target_ip}")

    scan_ports(
        target_ip,
        args.start,
        args.end,
        args.timeout
    )


if __name__ == "__main__":
    main()
