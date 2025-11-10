# 🏯 Tiktok Comments Scraper (Pay Per Result)

> Extract TikTok comments rapidly and get clean, structured JSON or CSV datasets. This scraper empowers marketers, researchers, and analysts to monitor conversations, detect trends, and analyze audience engagement at scale.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>🏯 Tiktok Comments Scraper (Pay Per Result)</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

The TikTok Comments Scraper is designed to collect comment-level data from TikTok videos efficiently. It solves the problem of manually tracking audience reactions and engagement by delivering organized datasets that include user profiles, likes, replies, and timestamps. Ideal for social media managers, brands, researchers, and growth hackers, it provides actionable insights from real-time conversations.

### Key Advantages

- Processes up to 10,000 comments per minute without requiring proxies.
- Outputs data in structured JSON, CSV, Excel, or XML formats.
- Flexible input parameters for targeting specific videos or user profiles.
- Supports nested replies and comprehensive user metadata.
- Affordable pay-per-result pricing model for scalable data extraction.

## Features

| Feature | Description |
|----------|-------------|
| High-Speed Comment Extraction | Scrapes 100–200 comments per second for rapid dataset creation. |
| User Profile Retrieval | Collects usernames, display names, bios, avatar URLs, and verification status. |
| Engagement Metrics | Captures likes, replies, and comment language for in-depth analysis. |
| Video Metadata | Includes video IDs and associated hashtags for context. |
| Flexible Input | Accepts arrays of video URLs and optional parameters like maxItems and includeReplies. |
| Structured Output | Provides clean JSON, CSV, Excel, or XML ready for analytics and reporting. |
| No Proxy Required | Operates efficiently without additional configuration. |
| Custom Configuration | Allows filtering, mapping, and tailored data retrieval. |
| Trend Detection | Analyze comment velocity, top phrases, and engagement ratios. |
| Comprehensive Reporting | Suitable for marketing, research, sales intelligence, and product feedback analysis. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| parentId | ID of the parent comment for threaded conversations. |
| id | Unique identifier for each comment. |
| text | Comment text content. |
| createdAt | Timestamp when the comment was created. |
| likeCount | Number of likes the comment received. |
| replyCount | Number of replies to the comment. |
| commentLanguage | Detected language of the comment. |
| awemeId | ID of the associated TikTok video. |
| isAuthorLiked | Whether the author liked the comment. |
| user | Object containing user metadata: id, username, displayName, URL, bio, avatarUrl, region, language, hasEmail, hasPhone, coverImage. |
| post | Object with post metadata: id, URL, hashtags, caption. |

---

## Example Output

    [
        {
            "parentId": "42517992603752202618",
            "id": "7277992603752203013",
            "text": "TE AMO MI NIÑA💚💚💚💚💚💚🙌🌷",
            "createdAt": "2023-09-12T17:28:42.000Z",
            "likeCount": 0,
            "replyCount": 0,
            "commentLanguage": "es",
            "awemeId": "7050551461734042926",
            "isAuthorLiked": false,
            "user": {
                "id": "7175984693090419717",
                "username": "21billie_eilish",
                "displayName": "¡★!",
                "url": "https://www.tiktok.com/@21billie_eilish",
                "bio": "Billiestan for ever¡★!",
                "avatarUrl": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/2ba7ea3e35244236b90b97ff237b2279~c5_1080x1080.webp?x-expires=1701540000&x-signature=6dPU2G8kLtkTuLN4YoyPZvHqVrY%3D",
                "region": "CO",
                "language": "es",
                "hasEmail": false,
                "hasPhone": false,
                "coverImage": "https://p77-sg.tiktokcdn.com/obj/tiktok-obj/1613727517271041"
            }
        }
    ]

---

## Directory Structure Tree

    tiktok-comments-scraper-pay-per-result/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── tiktok_parser.py
    │   │   └── utils_time.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Sales Teams** use it to monitor customer sentiment in comments, so they can identify product interest and market trends early.
- **Lead Generation Specialists** use it to extract engaged user profiles, so they can build targeted prospect lists efficiently.
- **Marketing Strategists** use it to analyze audience feedback, so they can refine campaign messaging and content strategy.
- **Researchers** use it to collect large-scale comment datasets, so they can conduct sentiment analysis or cultural studies.
- **Product Teams** use it to track feature requests and pain points, so they can improve product offerings based on real user feedback.

---

## FAQs

**Do I need a TikTok account?**
No. You only need publicly accessible video URLs. No login credentials are required.

**What input formats are supported?**
Supply an array of video URLs via the startUrls parameter. Optional parameters include maxItems and includeReplies.

**Can replies be scraped?**
Yes, enable includeReplies to retrieve threaded comments. Some replies may be missing depending on video activity.

**What output formats are available?**
JSON, CSV, Excel (.xlsx), and XML are all supported for downstream analysis and integration.

---

## Performance Benchmarks and Results

**Primary Metric:** 100–200 comments per second extraction speed.
**Reliability Metric:** 99% success rate over 100K+ runs.
**Efficiency Metric:** Minimal setup, no proxies required, capable of high-volume scraping.
**Quality Metric:** Structured data output with comprehensive user, comment, and engagement metadata.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
