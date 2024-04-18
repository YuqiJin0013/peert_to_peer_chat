import re

def validate_ip(ip):
    pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, ip))


def validate_port(port):
    return port.isdigit() and 0 <= int(port) <= 65535

# Example usage
ip = '10.239.128.59'
port = '5001'
if validate_ip(ip) and validate_port(port):
    # Proceed with SQL operation
    pass
else:
    # Handle invalid input
    pass
