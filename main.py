from PIL import Image
from calendar import generate as calendar_generate
from wallpapaer import generate as wallpaper_generate
from config import load_config


config = load_config(config_path='example/asm.toml')
calendar_image = calendar_generate(config, transparent=False)
calendar_image.save('output/'+config['calendar']['output'], 'png')

calendar_image = calendar_generate(config, transparent=True)
wallpaper_image = Image.open('images/wallpaper.png')
wallpaper_image = wallpaper_generate(calendar_image, wallpaper_image, config)
wallpaper_image.save('output/'+config['wallpaper']['output'], 'png')
