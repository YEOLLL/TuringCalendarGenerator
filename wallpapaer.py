from PIL import Image


def generate(calendar_image, wallpaper_image, config):
    wallpaper_image = wallpaper_image.convert('RGBA')

    width = int(calendar_image.size[0] * config['wallpaper']['code_zoom'])
    height = int(calendar_image.size[1] * config['wallpaper']['code_zoom'])
    calendar_image = calendar_image.resize((width, height))
    temp_image = Image.new('RGBA', wallpaper_image.size, (255, 255, 255, 0))
    temp_image.paste(calendar_image, config['wallpaper']['code_pos'])
    wallpaper_image.alpha_composite(temp_image)
    wallpaper_image.save('output.png', 'png')
