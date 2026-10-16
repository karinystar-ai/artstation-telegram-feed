
import json
import urllib.request
import urllib.error

URL = "https://www.artstation.com/search?sort_by=relevance&query=art"

request = urllib.request.Request(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml",
    },
)

try:
    with urllib.request.urlopen(request, timeout=20) as response:
        html = response.read().decode("utf-8", errors="replace")
        print("HTTP status:", response.status)
        print("HTML length:", len(html))
        print("Contains ArtStation:", "artstation.com" in html.lower())
        print("Contains project markers:", '"project"' in html.lower())
        print("Preview:", html[:500].replace("\n", " "))
except urllib.error.HTTPError as error:
    print("HTTP error:", error.code)
    print(error.read(1000).decode("utf-8", errors="replace"))
except Exception as error:
    print("Error:", repr(error))
