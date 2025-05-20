import os
import re
from bs4 import BeautifulSoup

INPUT_FILE = os.path.join("data", "chime_s1.html")
OUTPUT_FILE = os.path.join("data", "chime_s1.txt")


def html_to_text(html_file: str) -> str:
    with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f, "html.parser")
    text = soup.get_text(separator="\n")
    return text


def clean_text(text: str) -> str:
    text = re.sub(r"\s+\n", "\n", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    return text.strip()


def save_text(text: str, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    raw = html_to_text(INPUT_FILE)
    cleaned = clean_text(raw)
    save_text(cleaned, OUTPUT_FILE)
    print(f"Extracted text saved to {OUTPUT_FILE}")
