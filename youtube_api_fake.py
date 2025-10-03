 # Fake YouTube API handler for demo purposes 🎬

def get_comments(video_id: str) -> list:
    """Return mock comments for a given video ID."""
    mock_data = {
        "video1": [
            "This video is amazing! Loved it ❤️",
            "I didn’t like it at all 👎",
            "It was okay, nothing special 🤔",
            "Super helpful, thanks a lot 🙌",
            "Terrible sound quality 🔇"
        ],
        "video2": [
            "Brilliant explanation 👌",
            "This is boring 😴",
            "Not bad, but could be better 👍",
            "Awesome tutorial! 🔥",
            "Worst video ever 😡"
        ]
    }
    return mock_data.get(video_id, ["No comments available."])

