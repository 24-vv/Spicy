import requests
import os

def validate_proxy(proxy):
    try:
        response = requests.get("http://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        return response.status_code == 200
    except:
        return False

def auto_deletion(filename="output/output.txt"):
    if not os.path.exists(filename):
        print(f'\033[91m[ Error ]\033[0m No stored proxies found in {filename}\n')
        return
    with open(filename, 'r') as file:
        proxies = file.read().splitlines()
    
    valid_proxies = [proxy for proxy in proxies if validate_proxy(proxy)]
    
    with open(filename, 'w') as file:
        for proxy in valid_proxies:
            file.write(f"{proxy}\n")
    print()
    print(f'\033[92m[ Success ]\033[0m Rewritten {filename} with only valid proxies\n')
