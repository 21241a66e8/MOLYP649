import requests

def fetch_quote_of_the_day():
    url = "https://api.quotefancy.com/v1/quote-of-the-day"
    response = requests.get(url)

    if response.status_code == 200:
        quote_data = response.json()
        return quote_data.get("quote", "Failed to fetch quote.")
    else:
        return "Failed to fetch quote."

def display_quote(quote):
    print("Quote of the Day:")
    print(quote)

# Example Usage:
quote_of_the_day = fetch_quote_of_the_day()
display_quote(quote_of_the_day)