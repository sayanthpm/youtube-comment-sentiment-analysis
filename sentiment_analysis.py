 from textblob import TextBlob

def analyze_comment(comment: str) -> dict:
    """Analyze the sentiment of a single YouTube comment."""
    blob = TextBlob(comment)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😀"
    elif polarity < 0:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    return {"comment": comment, "polarity": polarity, "sentiment": sentiment}

def analyze_comments(comments: list) -> dict:
    """Analyze a list of comments and return sentiment stats."""
    results = [analyze_comment(c) for c in comments]

    counts = {"Positive 😀": 0, "Negative 😡": 0, "Neutral 😐": 0}
    for r in results:
        counts[r["sentiment"]] += 1

    total = len(comments)
    percentages = {k: (v/total)*100 for k, v in counts.items()}

    return {"results": results, "percentages": percentages}

