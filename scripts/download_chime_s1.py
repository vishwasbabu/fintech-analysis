import os
import requests

URL = "https://www.sec.gov/Archives/edgar/data/1795586/000162828025025059/chimefinancialinc-sx1wq1da.htm"
OUTPUT_PATH = os.path.join("data", "chime_s1.html")


def download(url: str, output_path: str) -> None:
    """Download the given URL and save it to the output path."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(response.content)
    print(f"Saved {url} to {output_path}")


if __name__ == "__main__":
    download(URL, OUTPUT_PATH)
