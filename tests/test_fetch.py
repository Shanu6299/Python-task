import unittest
from unittest.mock import patch
from get_papers.fetch import fetch_papers, fetch_paper_details

class TestFetch(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_papers(self, mock_get):
        # Mock the API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'esearchresult': {
                'idlist': ['123', '456']
            }
        }

        result = fetch_papers('test query')
        self.assertIsInstance(result, list)

    @patch('requests.get')
    def test_fetch_paper_details(self, mock_get):
        # Mock the API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'result': {
                '123': {
                    'title': 'Test Paper',
                    'pubdate': '2023',
                    'authors': [{
                        'name': 'Test Author',
                        'affiliation': 'Test University',
                        'email': 'test@example.com'
                    }]
                }
            }
        }

        result = fetch_paper_details(['123'], debug=False)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['Title'], 'Test Paper')

if __name__ == '__main__':
    unittest.main()