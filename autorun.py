import sys
import termios
import tty
import os
import subprocess
import shutil

options = [
    "Waybar",
    "Rofi",
    "Fastfetch",
    "Hyprland",
    "Kitty",
    "Hyprlock",
]

selected = [False] * len(options)
cursor_pos = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print("Use arrow keys to move, Enter to toggle/select, 'q' to quit\n")
    for i, opt in enumerate(["Continue"] + options):
        cursor = "→" if i == cursor_pos else " "
        if i == 0:
            print(f"{cursor} {opt}")
        else:
            checked = "[X]" if selected[i-1] else "[ ]"
            print(f"{cursor} {checked} {opt}")

def read_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == "\x1b":
            ch2 = sys.stdin.read(1)
            if ch2 == "[":
                ch3 = sys.stdin.read(1)
                return ch + ch2 + ch3
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def download_and_copy(option):
    repo_url = "https://github.com/NormallyDisblend/Hyprland-dotfiles.git"
    clone_dir = "/tmp/hyprland-dotfiles"
    dest_map = {
        "Waybar": os.path.expanduser("~/.config/waybar"),
        "Rofi": os.path.expanduser("~/.config/rofi"),
        "Fastfetch": os.path.expanduser("~/.config/fastfetch"),
        "Hyprland": os.path.expanduser("~/.config/hypr"),
        "Kitty": os.path.expanduser("~/.config/kitty"),
        "Hyprlock": os.path.expanduser("~/.config/hypr/hyprlock"),
    }
    config_subfolder_map = {
        "Waybar": "configs/waybar",
        "Rofi": "configs/rofi",
        "Fastfetch": "configs/fastfetch",
        "Hyprland": "configs/hyprland",
        "Kitty": "configs/kitty",
        "Hyprlock": "configs/hyprlock",
    }
    if option not in dest_map or dest_map[option] is None:
        print(f"Skipping {option}: no destination folder defined.")
        return
    dest_folder = dest_map[option]
    src_subfolder = config_subfolder_map[option]
    print(f"Processing {option}...")
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    subprocess.run(["git", "clone", "--depth", "1", repo_url, clone_dir], check=True)
    src_folder = os.path.join(clone_dir, src_subfolder)
    if not os.path.exists(src_folder):
        print(f"Source folder {src_folder} not found in repo. Skipping {option}.")
        shutil.rmtree(clone_dir)
        return
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
    shutil.copytree(src_folder, dest_folder)
    print(f"Copied {option} config to {dest_folder}")
    shutil.rmtree(clone_dir)

def main():
    global cursor_pos
    while True:
        print_menu()
        key = read_key()
        if key == "\x1b[A":
            cursor_pos = (cursor_pos - 1) % (len(options) + 1)
        elif key == "\x1b[B":
            cursor_pos = (cursor_pos + 1) % (len(options) + 1)
        elif key == "\r":
            if cursor_pos == 0:
                break
            else:
                selected[cursor_pos - 1] = not selected[cursor_pos - 1]
        elif key.lower() == "q":
            print("\nExiting without changes.")
            sys.exit(0)
    clear_screen()
    print("Starting download and setup for the selected configs:\n")
    for opt, sel in zip(options, selected):
        if sel:
            try:
                download_and_copy(opt)
            except Exception as e:
                print(f"Failed to process {opt}: {str(e)}")

if __name__ == "__main__":
    main()
