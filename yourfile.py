import requests
import urllib.parse

BARK_KEY = "yourkey"

title = urllib.parse.quote("your title here")
body = urllib.parse.quote("your message here")

url = f"https://api.day.app/{BARK_KEY}/{title}/{body}"
requests.get(url, timeout=10)


