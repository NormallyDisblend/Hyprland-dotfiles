## Installation

Ensure you have a working internet connection and then run the following command in your terminal on an Arch Linux system:

```
sudo pacman -Sy --noconfirm python git base-devel &&
git clone https://aur.archlinux.org/yay.git /tmp/yay &&
cd /tmp/yay &&
makepkg -si --noconfirm &&
cd - &&
yay -S --noconfirm waybar rofi hyprpaper kitty fastfetch && 
curl -O https://raw.githubusercontent.com/NormallyDisblend/Hyprland-dotfiles/main/autorun.py &&
python3 autorun.py
```

## Usage

- Use arrow keys to navigate through the menu.  
- Press Enter to select/deselect the config you want to download/install.  
- Select "Continue" and press Enter to start downloading and setting up your chosen configs.  
- Press 'q' to exit without changes.

## Requirements

- Arch Linux or derivative with `pacman` and `yay` available.  
- Python 3 installed (installed automatically via the command above).  
- Git installed (installed automatically via the command above).
