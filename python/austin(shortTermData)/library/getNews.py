#Get the json file from newsapi

import requests
import customModules.jsonSearch

def get_latest_news():
    #Credit: https://www.freecodecamp.org/news/python-project-how-to-build-your-own-jarvis-using-python/
    news_api_key = customModules.jsonSearch.search_keys_in_json_files("path/to/apiKey.json", "NewsAPIKeys", "apiKey")
    news_headlines = []
    try:
        res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}&category=general").json()
        articles = res["articles"]
        for article in articles:
            news_headlines.append(article["title"])
        return news_headlines[:5]
    except:
        print("Error, unable to get news, internet maybe down.")
