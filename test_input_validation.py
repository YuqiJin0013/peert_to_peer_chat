import unittest
from input_validation import validate_ip, validate_port

class TestInputValidation(unittest.TestCase):
    def test_validate_ip(self):
        valid_ips = ['192.168.1.1', '10.0.0.1', '172.16.0.1', '10.239.128.59']
        invalid_ips = ['256.168.1.1', 'abc.def.ghi.jkl', '192.168.1']

        for ip in valid_ips:
            self.assertTrue(validate_ip(ip))

        for ip in invalid_ips:
            self.assertFalse(validate_ip(ip))

    def test_validate_port(self):
        valid_ports = ['8080', '12345', '65535', '5001']
        invalid_ports = ['abc', '65536', '-1', '']

        for port in valid_ports:
            self.assertTrue(validate_port(port))

        for port in invalid_ports:
            self.assertFalse(validate_port(port))

if __name__ == '__main__':
    unittest.main()
