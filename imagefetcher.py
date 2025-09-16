"""
Giltech Online Cyber - Ubuntu-Inspired Image Fetcher
"I am because we are" - Ubuntu Philosophy

Branded for Giltech Online Cyber:
- Community: Connects to the wider web
- Respect: Handles errors gracefully
- Sharing: Organizes and stores resources
- Practicality: A tool useful for cyber café and digital users
"""

import requests
import os
import hashlib
from urllib.parse import urlparse
from datetime import datetime

def get_filename_from_url(url):
    """Extract filename from URL or generate one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or "." not in filename:
        filename = f"giltech_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    return filename

def is_duplicate(filepath, content):
    """Check if file already exists (duplicate detection by hash)."""
    if not os.path.exists(filepath):
        return False
    with open(filepath, "rb") as f:
        existing_hash = hashlib.md5(f.read()).hexdigest()
    new_hash = hashlib.md5(content).hexdigest()
    return existing_hash == new_hash

def fetch_images(urls):
    print("🌐 Welcome to Giltech Online Cyber")
    print("Ubuntu-Inspired Image Fetcher")
    print("Mindfully collecting and organizing images for our community.\n")

    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        try:
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            # Precaution: ensure content is image
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipping {url} (Not an image, Content-Type: {content_type})")
                continue

            filename = get_filename_from_url(url)
            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicates
            content = response.content
            if os.path.exists(filepath) and is_duplicate(filepath, content):
                print(f"✗ Skipping {filename} (Duplicate already exists)")
                continue

            # Save the image
            with open(filepath, "wb") as f:
                f.write(content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("\n🤝 Connection strengthened. Community enriched.")
    print("💻 Powered by Giltech Online Cyber\n")

def main():
    urls_input = input("Enter image URLs (separate with commas): ").strip()
    urls = [u.strip() for u in urls_input.split(",") if u.strip()]
    fetch_images(urls)

if __name__ == "__main__":
    main()
