# python3 test.py
import unittest

from lib.foo import foo

class TestLib(unittest.TestCase):
    def test_foo_hello(self):
        self.assertEqual(foo("hello"), "*hello*")

if __name__ == "__main__":
    unittest.main()
