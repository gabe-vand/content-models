import feedparser

url: str = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^GSPC,^DJI,^IXIC&region=US&lang=en-US"
feed = feedparser.parse(url)

for entry in feed.entries: 
    print("Title:", entry.title)
    print("Link:", entry.link)
    print("Published:", entry.published, "\n")
