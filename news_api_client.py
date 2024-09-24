import requests
import logging
import sqlite3
import pandas as pd
from datetime import datetime

class NewsAPIClient:
    def __init__(self, api_key, db_name='news.db'):
        """Initialize the NewsAPIClient with an API key and a database name."""
        self.api_key = api_key
        self.base_url = 'https://newsapi.org/v2/'
        self.db_name = db_name

    def fetch_news(self, query="heat AND exchanger"):
        """Fetch news articles from News API service (https://newsapi.org) based on a query."""
        url = f'{self.base_url}everything?q={query}&apiKey={self.api_key}'
        print(f"Requesting URL: {url}")  
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get('status') == 'ok' and response.status_code == 200:
                logging.info(f"Fetched {len(data['articles'])} articles.")
                return data['articles']
            else:
                logging.error(f"API Error: {data['message']}")
                return []
        except requests.exceptions.RequestException as e:
            logging.error(f"Request Error: {e}")
            return []

    def process_news(self, articles):
        """Process and format news articles, converting 'publishedAt' field to 'yyyy-mm-dd' format."""
        processed_articles = []
        for article in articles:
            published_at_raw = article.get('publishedAt')
            if published_at_raw:
                try:
                    published_at = datetime.strptime(published_at_raw, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
                except ValueError:
                    published_at = ''
            else:
                published_at = ''

            processed_articles.append({
                'title': article.get('title', 'No title'),
                'description': article.get('description', 'No description'),
                'url': article.get('url', 'No URL'),
                'publishedAt': published_at,  
                'source': article.get('source', {}).get('name', 'Unknown')
            })
        processed_articles_sorted = sorted(
        processed_articles, 
            key=lambda x: x['publishedAt'], 
            reverse=True
        )      
        return processed_articles_sorted
            
    def display_news(self, processed_articles_sorted):
        """Display the processed news articles in a readable format."""
        if not processed_articles_sorted:
            print("No news articles available.")
            return
        for index, article in enumerate(processed_articles_sorted, start=1):
            print(f"{index}. {article['title']}")
            print(f"   Published on: {article['publishedAt'] if article['publishedAt'] else 'No date available'}")
            print(f"   Description: {article['description']}")
            print(f"   URL: {article['url']}")
            print(f"   Source: {article['source']}")  
            print()  

    def save_to_database(self, processed_articles_sorted):
        """Save the processed articles to the SQLite database."""
        df = pd.DataFrame(processed_articles_sorted)
        try:
            with sqlite3.connect(self.db_name) as con:
                df.to_sql('news', con, if_exists='append', index=False)
                logging.info(f"Inserted {len(df)} new articles into the database.")
                print(f"Success: {len(df)} articles were inserted into the database.")
        except Exception as e:
            logging.error(f"Error saving to database: {e}")
            print(f"Error: Could not save articles to the database. Check log file for details.")

    def fetch_and_save_news(self, query="heat AND exchanger"):
        """Combine fetching, processing, saving, and display news articles in one method."""
        articles = self.fetch_news(query=query)
        if articles:
            processed_articles_sorted = self.process_news(articles)
            self.save_to_database(processed_articles_sorted)
            self.display_news(processed_articles_sorted)  
        else:
            logging.info("No new articles fetched.")
            print("No new articles were fetched.")
            return 0