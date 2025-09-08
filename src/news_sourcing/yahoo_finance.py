import feedparser

def getRecentStories(tickers: list[str]) -> list[tuple[str, str, str]]:
    '''
    Use yahoo finance to get recent stories for specific markets.
    Params:
        Tickers: list of tickers to return stories for 
        GSPC = S&P500
        DJI = Dow Jones Industrial Average
        IXIC = Nasdaq Composite
    Returns:
        List of tuples of articles containing the title, link, and publish date
    '''
    ticker_insert: str = ",^".join(tickers)
    print(ticker_insert)

    url: str = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s=^{ticker_insert}&region=US&lang=en-US"
    feed = feedparser.parse(url)

    results = [(str(entry.title), str(entry.link), str(entry.published)) for entry in feed.entries if entry]

    return results
