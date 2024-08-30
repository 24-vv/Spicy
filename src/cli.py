import os
from src.generator import generate_proxies
from src.validator import validate_proxy, auto_deletion
from src.store import store_proxies, load_stored_proxies

auto_store = False

def display_ascii_art():
    print("\033[91m")
    print(r"  _____       _                  |  [ 1 ] Generate Proxies")
    print(r" /  ___|     (_)                 |  [ 2 ] Validate Proxies")
    print(r" \ `--. _ __  _  ___ _   _       |  [ 3 ] Settings")
    print(r"  `--. \ '_ \| |/ __| | | |      |  [ 4 ] Exit")
    print(r" /\__/ / |_) | | (__| |_| |      |")
    print(r" \____/| .__/|_|\___|\__, |      |")
    print(r"       | |            __/ |      |")
    print(r"       |_|           |___/ v1.0  |")
    print(r"                                 |  Made with ♥ by .24vv")
    print("\033[0m")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def settings():
    global auto_store
    while True:
        clear_console()
        display_ascii_art()
        print("\033[91m[ SETTINGS ]\033[0m")
        print()
        print("\033[93m [ 1 ] Enable Auto Store\033[0m")
        print("\033[93m [ 2 ] Disable Auto Store\033[0m")
        print("\033[93m [ 3 ] Back to Main Menu\033[0m")
        print()
        choice = input("\033[91m[ SPICY ]\033[0m > \033[97m").strip()
        print()
        if choice == "1":
            auto_store = True
            print("\033[92m[ Success ]\033[0m Auto Store enabled")
            print()
            input("\033[91m[ INFO ]\033[0m Press Enter to continue...")
        elif choice == "2":
            auto_store = False
            print("\033[92m[ Success ]\033[0m Auto Store disabled")
            print()
            input("\033[91m[ INFO ]\033[0m Press Enter to continue...")
        elif choice == "3":
            clear_console()
            display_ascii_art()
            break
        else:
            print("\033[91m[ ERROR ]\033[0m Unknown command. Type '1', '2', or '3'.")
            print()
            input("\033[91m[ INFO ]\033[0m Press Enter to continue...")

def main():
    window = "mode 89,13"
    os.system(window)
    os.system('title "Spicy | v1.0"')

    display_ascii_art()

    while True:
        command = input("\033[91m[ SPICY ]\033[0m > ").strip().lower().split()
        if command[0] == "1":
            num = command[1] if len(command) > 1 and command[1].isdigit() else input("\033[91m[ GENERATOR ]\033[0m Enter the number of proxies to generate: \033[97m")
            proxies = generate_proxies(int(num))
            print()
            if auto_store:
                store_proxies(proxies)
                print(f'\033[92m[ Success ]\033[0m Successfully Generated {len(proxies)} proxies')
            else:
                for proxy in proxies:
                    print(f'\033[92m[ Success ]\033[0m Successfully Generated {proxy}')
            print()
        elif command[0] == "2":
            if auto_store:
                choice = input("\033[91m[ VALIDATOR ]\033[0m Validate proxies inside output.txt? (y/n): \033[97m").strip().lower()
                print()
                if choice == 'y':
                    proxies = load_stored_proxies()
                    for proxy in proxies:
                        is_valid = validate_proxy(proxy)
                        print(f'\033[91m[ VALIDATOR ]\033[0m Proxy {proxy} is \033[97m{"valid" if is_valid else "invalid"}')
                    auto_deletion()
                else:
                    proxy = input("\033[91m[ VALIDATOR ]\033[0m Enter the proxy to validate: \033[97m")
                    is_valid = validate_proxy(proxy)
                    print(f'\033[91m[ VALIDATOR ]\033[0m Proxy {proxy} is \033[97m{"valid" if is_valid else "invalid"}')
            else:
                proxy = input("\033[91m[ VALIDATOR ]\033[0m Enter the proxy to validate: \033[97m")
                print()
                is_valid = validate_proxy(proxy)
                print(f'\033[91m[ VALIDATOR ]\033[0m Proxy {proxy} is \033[97m{"valid" if is_valid else "invalid"}')
                print()
        elif command[0] == "3":
            settings()
        elif command[0] == "4":
            print()
            print('\033[91m[ SPICY ]\033[0m Goodbye!')
            break
        else:
            print()
            print("\033[91m[ ERROR ]\033[0m Unknown command. Type '1', '2', '3', or '4'.")
            print()

if __name__ == '__': 
    main()
