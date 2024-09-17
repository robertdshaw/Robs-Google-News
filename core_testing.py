import unittest
from NewsAPIClient import NewsAPIClient

class TestNewsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = 'e4f24353cb9442dc8edf45fe5b6d975e'
        self.news_client = NewsAPIClient(self.api_key)
    
    def test_fetch_news(self):
        """Test fetching news articles from NewsAPI."""
        articles = self.news_client.fetch_news(query="heat exchangers")
        self.assertIsNotNone(articles, "No articles were fetched.")
        self.assertIsInstance(articles, list, "Articles should be returned as a list.")
    
    def test_process_news(self):
        """Test processing fetched news articles."""
        sample_data = [{'title': 'Test Title', 'description': 'Test Desc', 'url': 'http://fakenews.com', 'publishedAt': '2024-01-13T12:00:00Z'}]
        processed_data = self.news_client.process_news(sample_data)
        self.assertEqual(len(processed_data), 1, "The processed data should contain one article.")
        self.assertEqual(processed_data[0]['title'], 'Test Title', "The title was processed incorrectly.")
        self.assertEqual(processed_data[0]['publishedAt'], '2024-01-13', "The published date was processed incorrectly.")

if __name__ == '__main__':
    unittest.main()
