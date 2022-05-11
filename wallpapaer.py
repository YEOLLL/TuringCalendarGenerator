from PIL import Image


def combine(calendar_image, wallpaper_image, zoom, pos):
    wallpaper_image = wallpaper_image.convert('RGBA')

    width = int(calendar_image.size[0] * zoom)
    height = int(calendar_image.size[1] * zoom)
    calendar_image = calendar_image.resize((width, height))

    temp_image = Image.new('RGBA', wallpaper_image.size, (255, 255, 255, 0))
    temp_image.paste(calendar_image, pos)

    wallpaper_image.alpha_composite(temp_image)
    return wallpaper_image
