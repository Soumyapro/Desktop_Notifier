import os

import requests as re
from dotenv import load_dotenv

load_dotenv()

class News:
    def __init__(self,url):
        self.url = url
        self.data = None
        self.new_data = None

    def get_news(self):
        try:
            self.data = re.get(self.url)
            return self.data.content
        except Exception as e:
            return e

    def save_json_file(self):
        with open('news.json','wb') as file:
            file.write(self.data.content)
            file.close()


if __name__ == "__main__":
    api_key = os.getenv('API_KEY')
    country_name = os.getenv('COUNTRY_NAME')
    news_url = f"https://newsapi.org/v2/top-headlines?country={country_name}&apiKey={api_key}"
    news = News(news_url)
    news_json_data = news.get_news()
    news.save_json_file()

