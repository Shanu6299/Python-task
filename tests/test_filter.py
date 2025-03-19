import unittest
from get_papers.filter import filter_non_academic_authors

class TestFilter(unittest.TestCase):
    def test_filter_non_academic_authors(self):
        test_papers = [{
            'PubmedID': '123',
            'Title': 'Test Paper',
            'Publication Date': '2023',
            'Authors': [{
                'name': 'John Doe',
                'affiliation': 'Pfizer Inc.',
                'email': 'john@pfizer.com'
            }, {
                'name': 'Jane Smith',
                'affiliation': 'Stanford University',
                'email': 'jane@stanford.edu'
            }]
        }]

        filtered_papers = filter_non_academic_authors(test_papers)
        self.assertEqual(len(filtered_papers), 1)
        self.assertEqual(filtered_papers[0]['PubmedID'], '123')

    def test_no_non_academic_authors(self):
        test_papers = [{
            'PubmedID': '456',
            'Title': 'Academic Paper',
            'Publication Date': '2023',
            'Authors': [{
                'name': 'Alice Brown',
                'affiliation': 'Harvard University',
                'email': 'alice@harvard.edu'
            }]
        }]

        filtered_papers = filter_non_academic_authors(test_papers)
        self.assertEqual(len(filtered_papers), 0)

if __name__ == '__main__':
    unittest.main()