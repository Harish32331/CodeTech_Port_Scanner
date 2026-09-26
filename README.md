# CodeTech Port Scanner

A Python-based TCP port scanner developed as part of the CodeTech Cybersecurity & Ethical Hacking Internship.

## Project Overview

The CodeTech Port Scanner is a command-line cybersecurity utility that checks a specified range of TCP ports on a hostname or IP address and identifies ports that accept TCP connections.

The project demonstrates basic concepts of:

- Network reconnaissance
- TCP/IP communication
- Socket programming
- Port enumeration
- Hostname and IP resolution
- Command-line argument handling

## Features

- TCP connect-based port scanning
- Custom starting and ending ports
- Configurable connection timeout
- Hostname and IPv4 address support
- Open-port identification
- Input validation
- Clear terminal output
- No external Python dependencies

## Technologies Used

- Python 3
- Python socket module
- Python argparse module
- TCP/IP networking

## Project Structure

CodeTech_Port_Scanner/
├── port_scanner.py
├── README.md
└── requirements.txt

## Usage

python3 port_scanner.py <target>

Example:

python3 port_scanner.py localhost -s 7995 -e 8005

## Testing

The scanner was tested against the local machine using a TCP service running on port 8000.

Test range: 7995-8005

Result: TCP/8000 - OPEN

## Security Notice

This tool is intended for educational purposes and authorized security testing only. Scan only systems and networks for which you have permission.

## Conclusion

The project demonstrates how Python socket programming can be used to establish TCP connections and identify accessible ports. It provides a simple foundation for understanding network reconnaissance and basic port-scanning techniques.
