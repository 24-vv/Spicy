import os
import aiohttp
import asyncio

success_color = "\033[92m"
theme_color = "\033[91m"

async def validate_proxy(proxy, proxy_type="http"):
    try:
        async with aiohttp.ClientSession() as session:
            proxies = {proxy_type: f"{proxy_type}://{proxy}"}
            async with session.get("http://www.google.com", proxy=proxies[proxy_type], timeout=5) as response:
                return response.status == 200
    except:
        return False

async def validate_proxies_concurrently(proxies, proxy_type="http", max_workers=1):
    valid_proxies = []
    tasks = []

    for proxy in proxies:
        tasks.append(validate_proxy(proxy, proxy_type))

    results = await asyncio.gather(*tasks)
    for proxy, is_valid in zip(proxies, results):
        if is_valid:
            valid_proxies.append(proxy)

    return valid_proxies

def auto_deletion(filename="output/output.txt"):
    if not os.path.exists(filename):
        print(f'{theme_color}[ Error ]\033[0m No stored proxies found in {filename}\n')
        return
    with open(filename, 'r') as file:
        proxies = file.read().splitlines()
    
    loop = asyncio.get_event_loop()
    valid_proxies = loop.run_until_complete(validate_proxies_concurrently(proxies))
    
    with open(filename, 'w') as file:
        for proxy in valid_proxies:
            file.write(f"{proxy}\n")
    print()
    print(f'{success_color}[ Success ]\033[0m Rewritten {filename} with only valid proxies\n')
