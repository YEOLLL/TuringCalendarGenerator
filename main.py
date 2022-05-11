from PIL import Image
from calendar import generate as calendar_generate
from wallpapaer import generate as wallpaper_generate
from config import load_config


config = load_config(config_path='config.toml')
calendar_image = calendar_generate(config, transparent=True)
calendar_image.save('output.png', 'png')
wallpaper_image = Image.open('images/mi3_solarized1_16x9.jpg')
wallpaper_image = wallpaper_generate(calendar_image, wallpaper_image, config)
# wallpaper_image.save(filename, 'png')
