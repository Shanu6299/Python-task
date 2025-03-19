import unittest
from get_papers.utils import is_non_academic_affiliation

class TestUtils(unittest.TestCase):
    def test_is_non_academic_affiliation(self):
        # Test pharmaceutical companies
        self.assertTrue(is_non_academic_affiliation('Pfizer Inc.'))
        self.assertTrue(is_non_academic_affiliation('Moderna Therapeutics'))
        self.assertTrue(is_non_academic_affiliation('Johnson & Johnson'))

        # Test academic institutions
        self.assertFalse(is_non_academic_affiliation('Harvard University'))
        self.assertFalse(is_non_academic_affiliation('Stanford Medical School'))
        self.assertFalse(is_non_academic_affiliation('MIT'))

        # Test edge cases
        self.assertFalse(is_non_academic_affiliation(''))
        self.assertFalse(is_non_academic_affiliation(None))

if __name__ == '__main__':
    unittest.main()