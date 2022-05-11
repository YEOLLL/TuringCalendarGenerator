import toml
from PIL import ImageFont


def load_config(config_path):
    with open(config_path, 'r') as f:
        config = toml.loads(f.read())

    for key in config.keys():
        if 'color' in config[key]:
            config[key]['color'] = tuple(config[key]['color'])
        if 'weekday_color' in config[key]:
            config[key]['weekday_color'] = tuple(config[key]['weekday_color'])
        if 'weekend_color' in config[key]:
            config[key]['weekend_color'] = tuple(config[key]['weekend_color'])
        if 'font' in config[key]:
            config[key]['font'] = ImageFont.truetype('assets/'+config[key]['font'], config[key]['font_size'])

    config['calendar']['today']['font'] = ImageFont.truetype(
        'assets/'+config['calendar']['today']['font'],
        config['calendar']['today']['font_size'])
    config['calendar']['date']['font'] = ImageFont.truetype(
        'assets/'+config['calendar']['date']['font'],
        config['calendar']['date']['font_size'])
    config['calendar']['date_cn']['font'] = ImageFont.truetype(
        'assets/'+config['calendar']['date_cn']['font'],
        config['calendar']['date_cn']['font_size'])

    return config
