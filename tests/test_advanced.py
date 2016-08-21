from .context import uspto

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""
    print "here we go"


    def test_patent_crawl(self):
        uspto.crawl_patents()


if __name__ == '__main__':
    unittest.main()
