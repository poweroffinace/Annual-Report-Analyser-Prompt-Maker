import requests

def fetch_stock_homepage(url):
    """
    Fetches the HTML content of a given stock URL.
    """
    # Headers mimic a real browser to prevent standard anti-bot blocking (403 errors)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    print(f"Attempting to fetch: {url}")
    
    try:
        # Use a session or simple get request
        response = requests.get(url, headers=headers, timeout=10)
        
        # Raise an exception if the HTTP request returned an unsuccessful status code
        response.raise_for_status() 
        
        print(f"Success! HTTP Status Code: {response.status_code}")
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the URL. Error: {e}")
        return None

if __name__ == '__main__':
    # Test the script with a Screener URL
    stock_url = "https://www.screener.in/company/TCS/"
    
    html_content = fetch_stock_homepage(stock_url)
    
    if html_content:
        print(f"Successfully retrieved {len(html_content)} characters of HTML.")
        # Print the first 500 characters just to verify it's the actual webpage
        print("-" * 40)
        print(html_content[:500] + "\n...[Truncated]")
