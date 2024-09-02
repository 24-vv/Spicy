import requests

def generate_proxies(num_proxies, proxy_type="http"):
    if proxy_type == "socks5":
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
    elif proxy_type == "https":
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all"
    else:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    
    response = requests.get(url)
    proxies = response.text.split('\n')
    proxy_list = []
    for proxy in proxies:
        if len(proxy_list) >= int(num_proxies):
            break
        if proxy.strip():
            proxy_list.append(proxy.strip())
            pass
    return proxy_list
