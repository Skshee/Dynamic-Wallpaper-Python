import ctypes
import os
import time
import random

user32 = ctypes.windll.user32
SPI_SETDESKWALLPAPER = 20

# Path
wallpaper_dir = "C:\\Users\\suvan\\OneDrive\\Pictures\\Wallpapers"


wallpapers = []

# Get all image files
for file in os.listdir(wallpaper_dir):
    if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        wallpapers.append(os.path.join(wallpaper_dir, file))

# Check if we found any wallpapers
if not wallpapers:
    print("No wallpaper images found!")
else:
    random.shuffle(wallpapers)
    # Main loop to cycle through wallpapers
    while True:
        for wallpaper in wallpapers:
            print(f"Setting wallpaper: {os.path.basename(wallpaper)}")
            user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER,
                0,
                wallpaper,
                0
            )
            # Wait before changing to next wallpaper
            time.sleep(30)