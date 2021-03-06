from .context import uspto

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""
    print "here we go"

    def test_first_patent(self):
        uspto.print_first_patent()

    def test_patent_crawl(self):
        uspto.crawl_patents_with_aggregate()

    def test_map_reduce_to_state(self):
        uspto.map_reduce_applicant_by_state()

if __name__ == '__main__':
    unittest.main()
