thonimport requests
from bs4 import BeautifulSoup
from src.extractors.utils_time import parse_timestamp

class TikTokScraper:
    def __init__(self, settings):
        self.settings = settings
        self.headers = {
            "User-Agent": settings.get("user_agent", "Mozilla/5.0")
        }

    def scrape_comments(self, video_url):
        response = requests.get(video_url, headers=self.headers, timeout=self.settings.get("request_timeout", 10))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

        comments_data = []
        comment_elements = soup.select("div.comment-item")
        for el in comment_elements:
            comment = {
                "id": el.get("data-id"),
                "text": el.select_one(".comment-text").get_text(strip=True),
                "createdAt": parse_timestamp(el.select_one(".comment-time").get_text(strip=True)),
                "likeCount": int(el.select_one(".like-count").get_text(strip=True)),
                "replyCount": int(el.select_one(".reply-count").get_text(strip=True)),
                "commentLanguage": el.get("data-lang"),
                "awemeId": el.get("data-aweme-id"),
                "isAuthorLiked": el.get("data-is-author-liked") == "true",
                "parentId": el.get("data-parent-id") or None,
                "user": {
                    "id": el.get("data-user-id"),
                    "username": el.get("data-username"),
                    "displayName": el.get("data-display-name"),
                    "url": el.get("data-profile-url"),
                    "bio": el.get("data-bio"),
                    "avatarUrl": el.get("data-avatar-url"),
                    "region": el.get("data-region"),
                    "language": el.get("data-language"),
                    "hasEmail": el.get("data-has-email") == "true",
                    "hasPhone": el.get("data-has-phone") == "true",
                    "coverImage": el.get("data-cover-image")
                },
                "post": {
                    "id": el.get("data-aweme-id"),
                    "url": video_url,
                    "hashtags": [tag.strip() for tag in el.get("data-hashtags", "").split(",") if tag.strip()],
                    "caption": el.get("data-caption", "")
                }
            }
            comments_data.append(comment)
        return comments_data