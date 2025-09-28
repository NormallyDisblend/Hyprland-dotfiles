## Installation

Ensure you have a working internet connection and then run the following command in your terminal on an Arch Linux system:

```
sudo pacman -Sy --noconfirm python git base-devel &&
git clone https://aur.archlinux.org/yay.git /tmp/yay &&
cd /tmp/yay &&
makepkg -si --noconfirm &&
cd - &&
yay -S --noconfirm waybar rofi hyprpaper kitty fastfetch swaync network-manager-applet networkmanager pacman-contrib jq wl-clipboard ttf-jetbrains-mono-nerd ttf-nerd-fonts-symbols &&
curl -O https://raw.githubusercontent.com/NormallyDisblend/Hyprland-dotfiles/main/autorun.py &&
python3 autorun.py

```

## Usage

- Use arrow keys to navigate through the menu.  
- Press Enter to select/deselect the config you want to download/install.  
- Select "Continue" and press Enter to start downloading and setting up your chosen configs.  
- Press 'q' to exit without changes.

<img width="1367" height="769" alt="image" src="https://github.com/user-attachments/assets/f7a8c375-bca7-4b31-a56b-5a020fb2a451" />


## Requirements

- Arch Linux or derivative with `pacman` and `yay` available.  
- Python 3 installed (installed automatically via the command above).  
- Git installed (installed automatically via the command above).

## Preview
<img width="1367" height="38" alt="image" src="https://github.com/user-attachments/assets/40360b34-fc1f-48c8-b6c7-bb49cb1e1ab8" />
<img width="524" height="298" alt="image" src="https://github.com/user-attachments/assets/5e64ab4d-0e58-4ea8-b082-4a8d5bf7952e" />
<img width="747" height="399" alt="image" src="https://github.com/user-attachments/assets/b1383f3d-e083-4f61-913f-e6f84c51c55e" />


## Keybinds

Super + Q = Open terminal
Super + C = Close terminal
Super + Space = Open rofi
Super + G = Hyprlock
Super + A = Screenshot

Others are the deafult hyprland configs.
