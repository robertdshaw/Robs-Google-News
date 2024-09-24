import logging
from news_api_client import NewsAPIClient
from create_db import NewsDatabase

# Set up logging
logging.basicConfig(
    filename='news_api.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

def main(api_key, query="heat AND exchanger"):
    """
    Initialize the NewsAPIClient and fetch news articles based on a query.

    Create a database, initialize the NewsAPIClient, and fetch
    and save news articles related to the specified query.
    """
    db = NewsDatabase()
    db.create_table()
    news_client = NewsAPIClient(api_key, db_name=db.db_name)
    news_client.fetch_and_save_news(query=query)

if __name__ == "__main__":
    API_KEY = 'e4f24353cb9442dc8edf45fe5b6d975e'
    main(API_KEY)
