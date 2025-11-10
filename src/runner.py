thonimport json
import argparse
from src.extractors.tiktok_parser import TikTokScraper
from src.outputs.exporters import JSONExporter, CSVExporter
from src.config.settings import load_settings

def main():
    parser = argparse.ArgumentParser(description="TikTok Comments Scraper")
    parser.add_argument("--input", type=str, required=True, help="Path to input file with video URLs")
    parser.add_argument("--output", type=str, default="data/output.json", help="Output file path")
    parser.add_argument("--format", type=str, choices=["json", "csv"], default="json", help="Output format")
    args = parser.parse_args()

    settings = load_settings()
    with open(args.input, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    all_comments = []
    scraper = TikTokScraper(settings)
    for url in urls:
        comments = scraper.scrape_comments(url)
        all_comments.extend(comments)

    if args.format == "json":
        exporter = JSONExporter(args.output)
    else:
        exporter = CSVExporter(args.output)

    exporter.export(all_comments)
    print(f"Scraping completed. {len(all_comments)} comments saved to {args.output}")

if __name__ == "__main__":
    main()