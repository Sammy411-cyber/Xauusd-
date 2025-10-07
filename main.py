import requests
import time

# Telegram setup
BOT_TOKEN = "8013997009"
CHAT_ID = "8327329122"

# GPT and News API setup
GPT_API_KEY = "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"
NEWS_API_KEY = "be5f4b15732b4495bd15140e8533e2fb"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

def get_latest_news():
    url = f"https://newsapi.org/v2/top-headlines?q=gold+bitcoin&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    if not articles:
        return "No recent news found."
    return articles[0]["title"]

def generate_signal():
    # This is where GPT will analyze and give the trading signal
    # For now, it just simulates one
    return "📊 Signal: Buy Gold for +120 pips"

def main():
    while True:
        news = get_latest_news()
        signal = generate_signal()
        send_telegram_message(f"📰 {news}\n\n{signal}")
        time.sleep(3600)  # Sends every hour

if __name__ == "__main__":
    send_telegram_message("🤖 Bot is now running!")
    main()
