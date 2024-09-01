import requests, random, socket


ROOT_URLS = [
"https://amazon.com/",
"https://baidu.com/",
"https://bilibili.com/",
"https://bing.com/",
"https://chatgpt.com/",
"https://discord.com/",
"https://docomo.ne.jp/",
"https://duckduckgo.com/",
"https://dzen.ru/",
"https://ebay.com/",
"https://facebook.com/",
"https://fandom.com/",
"https://google.com/",
"https://instagram.com/",
"https://linkedin.com/",
"https://live.com/",
"https://mail.ru/",
"https://max.com/",
"https://microsoft.com/",
"https://microsoftonline.com/",
"https://naver.com/",
"https://netflix.com/",
"https://office.com/",
"https://pinterest.com/",
"https://pornhub.com/",
"https://qq.com/",
"https://quora.com/",
"https://reddit.com/",
"https://roblox.com/",
"https://samsung.com/",
"https://sharepoint.com/",
"https://stripchat.com/",
"https://t.me/",
"https://tiktok.com/",
"https://turbopages.org/",
"https://twitch.tv/",
"https://twitter.com/",
"https://vk.com/",
"https://weather.com/",
"https://whatsapp.com/",
"https://wikipedia.org/",
"https://x.com/",
"https://xhamster.com/",
"https://xhamster.desi/",
"https://xnxx.com/",
"https://xvideos.com/",
"https://yahoo.co.jp/",
"https://yahoo.com/",
"https://yandex.ru/",
"https://youtube.com/"
	]

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
while True:
    url = random.choice(ROOT_URLS)
    fqdn = url.split('/')[2]
    try:
        response = requests.get(url, headers=headers)
        print(f"Grabbing: {url}. IP: {socket.gethostbyname(fqdn)}")
        print(response)
    except:
        print(f"Grabbing: {url}. IP: Unresolved")
        print("Skipped")