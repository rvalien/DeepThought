import unittest
import logging

logger = logging.getLogger(__name__)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(9, 9)


if __name__ == "__main__":
    unittest.main()
