 .context import uspto

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        uspto.crawl_patents()


if __name__ == '__main__':
    unittest.main()
