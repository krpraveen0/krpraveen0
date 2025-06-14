import os
import requests

API_KEY = os.getenv("NEWS_API_KEY")
if not API_KEY:
    raise EnvironmentError("NEWS_API_KEY environment variable not set")

QUERY = "artificial intelligence"
API_URL = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&q={QUERY}"

response = requests.get(API_URL, timeout=10)
response.raise_for_status()
data = response.json()

articles = data.get("results", [])[:5]

lines = []
for article in articles:
    title = article.get("title")
    link = article.get("link")
    if title and link:
        lines.append(f"- [{title}]({link})")

news_content = "\n".join(lines)

README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "README.md")
START = "<!-- NEWS-START -->"
END = "<!-- NEWS-END -->"

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find(START)
end_idx = content.find(END, start_idx)

if start_idx == -1 or end_idx == -1:
    raise ValueError("News markers not found in README")

new_content = (
    content[: start_idx + len(START)]
    + "\n"
    + news_content
    + "\n"
    + content[end_idx:]
)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)
