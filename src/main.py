from news_sourcing import yahoo_finance as yf
import openai


def main() -> None:
    articles: list[tuple[str, str, str]] = yf.getRecentStories(["GSPC", "DJI", "IXIC"])

    chatGPT 


if __name__ == "__main__":
    main()