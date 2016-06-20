import unittest
from localhostaddress import containsLocalHost

class LocalHostAddressTestCase(unittest.TestCase):
    def test_isnt_contains_localhost(self):
        self.assertFalse(containsLocalHost())

if __name__ == '__main__':
    unittest.main()