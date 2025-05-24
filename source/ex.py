import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def visualize_directory(directory_path: Path, indent: str = ""):
    if not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: {directory_path} не є директорією або не існує.")
        return

    for item in directory_path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.CYAN}{item.name}{Style.BRIGHT}")
            visualize_directory(item, indent + "  ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: необхідно вказати шлях до директорії.")
        sys.exit(1)

directory_path = Path(sys.argv[1])

visualize_directory(directory_path)
