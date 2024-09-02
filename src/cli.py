import os, json
from src.generator import generate_proxies
from src.validator import validate_proxy, auto_deletion
from src.store import store_proxies, load_stored_proxies

auto_store = False
theme_color = "\033[91m"
success_color = "\033[92m"
proxy_type = "http"

def set_theme_color(color):
    global theme_color
    theme_color = color

def set_proxy_type(p_type):
    global proxy_type
    proxy_type = p_type

def save_settings():
    settings = {
        "auto_store": auto_store,
        "theme_color": theme_color,
        "proxy_type": proxy_type,
    }
    with open("src/settings/settings.json", "w") as f:
        json.dump(settings, f)

def load_settings():
    global auto_store, theme_color, proxy_type
    if os.path.exists("src/settings/settings.json"):
        with open("src/settings/settings.json", "r") as f:
            settings = json.load(f)
            auto_store = settings.get("auto_store", False)
            theme_color = settings.get("theme_color", "\033[91m")
            proxy_type = settings.get("proxy_type", "http")

def display_ascii_art():
    print(theme_color)
    print(r"   _____       _                  |  [ 1 ] Generate Proxies")
    print(r"  /  ___|     (_)                 |  [ 2 ] Validate Proxies")
    print(r"  \ `--. _ __  _  ___ _   _       |  [ 3 ] Settings")
    print(r"   `--. \ '_ \| |/ __| | | |      |  [ 4 ] Open Output File")
    print(r"  /\__/ / |_) | | (__| |_| |      |  [ 5 ] Exit")
    print(r"  \____/| .__/|_|\___|\__, |      |")
    print(r"        | |            __/ |      |")
    print(r"        |_|           |___/ v1.2  |")
    print(r"                                  |  Made with ♥ by .24vv and .next")
    print("\033[0m")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def settings():
    global auto_store
    while True:
        clear_console()
        display_ascii_art()
        print(f"{theme_color}[ SETTINGS ]\033[0m")
        print()
        print(f"{theme_color} [ 1 ] Enable Auto Store\033[0m")
        print(f"{theme_color} [ 2 ] Disable Auto Store\033[0m")
        print(f"{theme_color} [ 3 ] Change Theme\033[0m")
        print(f"{theme_color} [ 4 ] Change Proxy Type\033[0m")
        print(f"{theme_color} [ 5 ] Back to Main Menu\033[0m")
        print()
        choice = input(f"{theme_color}[ SPICY ]\033[0m > \033[97m").strip()
        print()
        if choice == "1":
            auto_store = True
            print(f"{success_color}[ Success ]\033[0m Auto Store enabled")
            print()
            input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")
        elif choice == "2":
            auto_store = False
            print(f"{success_color}[ Success ]\033[0m Auto Store disabled")
            print()
            input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")
        elif choice == "3":
            print(f"{theme_color}[ SPICY ]\033[0m Choose a theme:")
            print()
            print(f"{theme_color} [ 1 ] Red\033[0m")
            print(f"{theme_color} [ 2 ] Purple\033[0m")
            print(f"{theme_color} [ 3 ] Yellow\033[0m")
            print(f"{theme_color} [ 4 ] Orange\033[0m")
            print(f"{theme_color} [ 5 ] Blue\033[0m")
            print()
            choice = input(f"{theme_color}[ SPICY ]\033[0m > \033[97m").strip()
            if choice == "1":
                set_theme_color("\033[91m")
            elif choice == "2":
                set_theme_color("\033[95m")
            elif choice == "3":
                set_theme_color("\033[93m")
            elif choice == "4":
                set_theme_color("\033[33m")
            elif choice == "5":
                set_theme_color("\033[94m")
            else:
                print(f"{theme_color}[ ERROR ]\033[0m Unknown theme. Type '1', '2', '3', '4', or '5'.")
                input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")
                continue
            print()
            print(f"{success_color}[ Success ]\033[0m Theme color changed")
            print()
            input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")
        elif choice == "4":
            print(f"{theme_color}[ SPICY ]\033[0m Choose a proxy type:")
            print()
            print(f"{theme_color} [ 1 ] HTTP\033[0m")
            print(f"{theme_color} [ 2 ] SOCKS5\033[0m")
            print(f"{theme_color} [ 3 ] HTTPS\033[0m")
            print()
            choice = input(f"{theme_color}[ SPICY ]\033[0m > \033[97m").strip()
            if choice == "1":
                set_proxy_type("http")
            elif choice == "2":
                set_proxy_type("socks5")
            elif choice == "3":
                set_proxy_type("https")
            else:
                print(f"{theme_color}[ ERROR ]\033[0m Unknown proxy type. Type '1', '2', or '3'.")
                input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")
                continue
            print()
            print(f"{success_color}[ Success ]\033[0m Proxy type changed")
            print()
            input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")
        elif choice == "5":
            save_settings()
            clear_console()
            display_ascii_art()
            break
        else:
            print(f"{theme_color}[ ERROR ]\033[0m Unknown command. Type '1', '2', '3', '4', or '5'.")
            print()
            input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")

def main():
    load_settings()
    window = "mode 89,35"
    os.system(window)
    os.system('title "Spicy | v1.2"')

    display_ascii_art()

    while True:
        command = input(f"{theme_color}[ SPICY ]\033[0m > ").strip().lower().split()
        if command[0] == "1":
            num = command[1] if len(command) > 1 and command[1].isdigit() else input(f"{theme_color}[ GENERATOR ]\033[0m Enter the number of proxies to generate: \033[97m")
            proxies = generate_proxies(int(num), proxy_type)
            print()
            if auto_store:
                store_proxies(proxies)
                print(f'{success_color}[ Success ]\033[0m Successfully Generated {len(proxies)} proxies')
            else:
                for proxy in proxies:
                    print(f'{success_color}[ Success ]\033[0m Successfully Generated {proxy}')
            print()
            input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")
            clear_console()
            display_ascii_art()
        elif command[0] == "2":
            if auto_store:
                choice = input(f"{theme_color}[ VALIDATOR ]\033[0m Validate proxies inside output.txt? (y/n): \033[97m").strip().lower()
                print()
                if choice == 'y':
                    proxies = load_stored_proxies()
                    for proxy in proxies:
                        is_valid = validate_proxy(proxy, proxy_type)
                        print(f'{theme_color}[ VALIDATOR ]\033[0m Proxy {proxy} is \033[97m{"valid" if is_valid else "invalid"}')
                    auto_deletion()
                else:
                    proxy = input(f"{theme_color}[ VALIDATOR ]\033[0m Enter the proxy to validate: \033[97m")
                    is_valid = validate_proxy(proxy, proxy_type)
                    print(f'{theme_color}[ VALIDATOR ]\033[0m Proxy {proxy} is \033[97m{"valid" if is_valid else "invalid"}')
            else:
                proxy = input(f"{theme_color}[ VALIDATOR ]\033[0m Enter the proxy to validate: \033[97m")
                print()
                is_valid = validate_proxy(proxy, proxy_type)
                print(f'{theme_color}[ VALIDATOR ]\033[0m Proxy {proxy} is \033[97m{"valid" if is_valid else "invalid"}')
                print()
            input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")
            clear_console()
            display_ascii_art()
        elif command[0] == "3":
            settings()
        elif command[0] == "4":
            os.system('notepad output/output.txt')
            input(f"{theme_color}[ SPICY ]\033[0m Press Enter to continue...")
            clear_console()
            display_ascii_art()
        elif command[0] == "5":
            print()
            print(f"{success_color}[ Success ]\033[0m Goodbye!")
            break
        else:
            print()
            print(f"{theme_color}[ ERROR ]\033[0m Unknown command. Type '1', '2', '3', '4', or '5'.")
            print()

if __name__ == '__main__':
    main()