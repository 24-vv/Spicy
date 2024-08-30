import os

def store_proxies(proxies, filename="output/output.txt"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        for proxy in proxies:
            file.write(f"{proxy}\n")
    print(f'\033[92m[ Success ]\033[0m Proxies stored in {filename}\n')

def load_stored_proxies(filename="output/output.txt"):
    if not os.path.exists(filename):
        print(f'\033[91m[ Error ]\033[0m No stored proxies found in {filename}\n')
        return []
    with open(filename, 'r') as file:
        proxies = file.read().splitlines()
    print(f'\033[92m[ Success ]\033[0m Loaded proxies from {filename}\n')
    return proxies
